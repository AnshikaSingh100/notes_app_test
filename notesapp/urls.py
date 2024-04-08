"""
URL configuration for notesapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import Note_cruds




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.user_CRUD_urls')),
    path('getallnotes',Note_cruds.getallnotes),
    path('getnote/<str:pk>/',Note_cruds.getanote),
    path('createnote',Note_cruds.createnote),
    path('updatenote/<str:pk>',Note_cruds.updatenote),
    path('deletenote/<str:pk>',Note_cruds.deleteanote)

]