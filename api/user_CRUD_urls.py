from django.contrib import admin
from django.urls import path
from api import User_Login_Cruds

urlpatterns = [

    path('getusers',User_Login_Cruds.getallusers),
    path('getauser/<str:pk>',User_Login_Cruds.getauser),
    path('createauser',User_Login_Cruds.createauser),
    path('updateauser/<str:pk>',User_Login_Cruds.updateauser),
    path('deleteuser/<str:pk>',User_Login_Cruds.deleteauser)

]
