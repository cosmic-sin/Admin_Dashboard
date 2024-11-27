from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#Model for roles

class Roles(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(blank=True)
    permissions = models.ManyToManyField('permission',related_name='roles')

    def __str__(self):
        return self.name
    
#Model for Permission

class Permission(models.Model):
    name = models.CharField(max_length=50,unique=True)
    code = models.CharField(max_length=50,unique=True) # to del or read user

    def __str__(self):
        return self.name
    
#Model fo User

class CustomUser(AbstractUser):
    role = models.ForeignKey(Roles,on_delete=models.SET_NULL,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
