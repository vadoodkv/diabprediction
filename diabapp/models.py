from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class signup(models.Model):
    username=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    address=models.CharField(max_length=250)
    dob=models.DateField(max_length=250)
    phone=models.IntegerField(max_length=250)
    password=models.CharField(max_length=250)
    
    def __str__(self):
        return self.username  
    

    
    

    