from django.db import models
from django.contrib.auth import get_user_model #this wont work as its app not initialized yet
from django.conf import settings
# Create your models here.


User = settings.AUTH_USER_MODEL


class MajorTeam(models.Model):
    name = models.CharField(max_length=150,unique=True)
    short_name = models.CharField(max_length=10)
    estd = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name)


class Career(models.Model):
    start = models.PositiveIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='careers')
    goals = models.PositiveIntegerField()
    club = models.ForeignKey(MajorTeam,on_delete=models.CASCADE,related_name='careers')

    def is_scorer(self):
        if self.goals > 100:
            return True
        return False
    
    @classmethod
    def get_inactive_count(cls):
        return cls.objects.select_related('user').filter(user__is_active).count()

    def __str__(self):
        return str(self.user)

    class Meta:
        unique_together = ["user", "club", "start"]