from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from apps.team.models import MajorTeam
# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    team = models.ForeignKey(MajorTeam,on_delete=models.CASCADE,related_name='users',blank=True,null=True)
    age = models.IntegerField(null=True,blank=True)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return str(self.email)
