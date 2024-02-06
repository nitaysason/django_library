from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import Librarian
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
# Create your views here.



@api_view(['GET'])
def index(req):
    return Response('hello')

@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")


class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'

@permission_classes([IsAuthenticated])
class LibrarianView(APIView):

    def get(self, request):
     
        user= request.user
        my_model = user. librarian_set.all()
        serializer = LibrarianSerializer(my_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET','POST','DELETE','PUT','PATCH'])
def librarian_view(req,id=-1):
     if req.method =='GET':
        if id > -1:
            try:
                temp_librarian=Librarian.objects.get(id=id)
                return Response (LibrarianSerializer( temp_librarian,many=False).data)
            except Librarian.DoesNotExist:
                return Response ("not found")
        all_Librarian=LibrarianSerializer(Librarian.objects.all(),many=True).data
        return Response (all_Librarian)
     if req.method =='POST':
        librarian_serializer = LibrarianSerializer(data=req.data)
        if  librarian_serializer.is_valid():
            librarian_serializer.save()
            return Response ("post...")
        else:
            return Response (LibrarianSerializer.errors)
     if req.method =='DELETE':
        try:
             temp_librarian=Librarian.objects.get(id=id)
        except Librarian.DoesNotExist:
            return Response ("not found")    
       
        temp_librarian.delete()
        return Response ("del...")
     if req.method =='PUT':
        try:
             temp_librarian=Librarian.objects.get(id=id)
        except Librarian.DoesNotExist:
            return Response ("not found")
       
        ser = LibrarianSerializer(data=req.data)
        old_librarian = Librarian.objects.get(id=id)
        res = ser.update( old_librarian, req.data)
        return Response('upd')   


