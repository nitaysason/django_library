from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from base import views

urlpatterns = [
    path('', views.index),

    path('login/', TokenObtainPairView.as_view()),
    path('register/', views.register),
    #  path('librarian/', views.LibrarianView.as_view()),
    path('librarian/', views.librarian_view),
    path('librarian/<int:id>', views.librarian_view),
]
