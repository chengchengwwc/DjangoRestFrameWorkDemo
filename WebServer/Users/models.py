from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class UserProfile(models.Model):
    """
    User
    """
    name = models.CharField(max_length=100,null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)
    mobile = models.CharField(max_length=6,choices=(('male','man'),('female','woman')))
    gender = models.CharField(max_length=11)
    email = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"
    
    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=6,choices=(('male','man'),('female','woman')))
    add_time = models.DateTimeField(default=datetime.now,)









