from django.db import models

class User(models.Model):
    name=models.CharField(max_length=25)
    username=models.CharField(max_length=25)
    emailid=models.CharField(unique=True,max_length=100)
    phonenumber=models.CharField(max_length=10,unique=True)
    address=models.TextField(max_length=1000)
    dateofbirth=models.DateField()
