from django.db import models
from Users.models import UserProfile
from Goods.models import Goods
from datetime import datetime

# Create your models here.

class ShoppingCart(models.Model):
    user = models.ForeignKey(UserProfile)
    goods = models.ForeignKey(Goods)
    goods_num = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=datetime.now)


class OrderInfo(models.Model):
    user = models.ForeignKey(UserProfile)
    order_sn = models.CharField(max_length=100,null=True,blank=True,unique=True)
    trade_no = models.CharField(max_length=100,null=True,blank=True,unique=True)
    pay_status = models.CharField(max_length=100,null=True,blank=True)
    pay_time = models.DateTimeField(default=datetime.now)
    address = models.CharField(max_length=100,null=True,blank=True)
    signer_name = models.CharField(max_length=100,null=True,blank=True)
    signer_mobile = models.CharField(max_length=100,null=True,blank=True)
    add_time = models.DateTimeField(default=datetime.now)


class OrderGoods(models.Model):
    order = models.ForeignKey(OrderInfo)
    goods = models.ForeignKey(Goods)
    goods_num = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=datetime.now)


    
