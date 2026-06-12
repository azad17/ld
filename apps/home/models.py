from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class BaseModel(models.Model):

    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True

class LevelChoices(models.TextChoices):
        TOP = "top", "Top"
        MID = "mid", "Mid"
        LOW = "low", "Low"

class Departments(BaseModel):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="department")
    established = models.PositiveIntegerField()
    level = models.CharField(max_length=20,choices=LevelChoices.choices,default=LevelChoices.LOW)

    def __str__(self):
        return str(self.name)

class MessagePriority(models.TextChoices):
    HIGH = "high", " High"
    MEDIUM = " medium", "Medium"
    LOW = "low", "Low" 

class Messages(BaseModel):
    messsage = models.CharField(max_length=120)
    to = models.ManyToManyField(User,related_name="message")
    priority = models.CharField(max_length=20,choices=MessagePriority.choices,default=MessagePriority.LOW)

