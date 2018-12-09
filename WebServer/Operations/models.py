from django.db import models
from Users.models import UserProfile
from Goods.models import Goods
from datetime import datetime
# Create your models here.


class UserFaw(models.Model):
    user = models.ForeignKey(UserProfile)
    goods = models.ForeignKey(Goods)
    add_time = models.DateTimeField(default=datetime.now)


class UserLeavingMessage(models.Model):
    MESSAGE_CHOICES = (
        (1,'留言'),
        (2,'投诉'),
        (3,'咨询'),
        (4,'售后'),
        (5,'求购')
    )

    user = models.ForeignKey(UserProfile)
    message_type = models.IntegerField(default=1,choices=MESSAGE_CHOICES)
    subject = models.CharField(max_length=100,null=True,blank=True)
    message = models.TextField()
    add_time = models.DateTimeField(default=datetime.now)


class UserAddress(models.Model):
    user = models.ForeignKey(UserProfile)
    address = models.CharField(max_length=100,null=True,blank=True)
    signer_name = models.CharField(max_length=100,null=True,blank=True)
    singer_mobile = models.CharField(max_length=100,null=True,blank=True)
    add_time = models.DateTimeField(default=datetime.now)







