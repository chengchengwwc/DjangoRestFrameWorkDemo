from datetime import datetime
from django.db import models

# Create your models here.


class GoodsCategory(models.Model):
    CATEGORY_TYPE = (
        (1,'First'),
        (2,'Second'),
        (3,'Third'),
    )


    name = models.CharField(max_length=30,null=True,blank=True)
    code = models.CharField(max_length=30,null=True,blank=True)
    desc = models.TextField()
    category_type = models.IntegerField(choices=CATEGORY_TYPE)
    parent_category = models.ForeignKey("self",null=True,blank=True)
    is_tab = models.BooleanField(default=False,help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name='Goods'
    
    def __str__(self):
        return self.name



class GoodsCategoryBrand(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    desc = models.TextField()
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Brand'

    def __str__(self):
        return self.name


class Goods(models.Model):
    
    category = models.ForeignKey(GoodsCategory)
    goods_sn = models.CharField(max_length=30,null=True,blank=True)
    name = models.CharField(max_length=30,null=True,blank=True)
    click_num = models.IntegerField(default=0)
    sold_num = models.IntegerField(default=0)
    fav_num = models.IntegerField(default=0)
    goods_num = models.IntegerField(default=0)
    market_price = models.FloatField(default=0)
    shope_price = models.FloatField(default=0)
    goods_brief = models.TextField()
    goods_desc = models.TextField()
    ship_free = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)


class GoodsImage(models.Model):
    goods = models.ForeignKey(Goods)
    add_time = models.DateTimeField(datetime.now)

    class Meta:
        verbose_name='Picture'

    def __str__(self):
        return self.name

class Banner(models.Model):
    goods = models.ForeignKey(Goods)
    index = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.goods.name
