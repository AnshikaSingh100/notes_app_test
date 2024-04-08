from django.db import models


# Create your models here.


# Create your models here.
class Users(models.Model):
    Email = models.CharField(max_length=320, unique=True)
    Password = models.CharField(max_length=100)

class Notes(models.Model):
    Title = models.TextField(default='Your Title here')
    Content = models.TextField(default='Your Content here')
    Timestamp = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False,null=False)


