from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Librarian(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    id = models.BigAutoField(primary_key=True)
    book = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    author = models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['book','author']
 
    def __str__(self):
           return self.book