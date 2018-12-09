

import django_filters
from Goods.models import *

class ProductFilter(django_filters.rest_framework.FilterSet):
    
    price_min = django_filters.NumberFilter(name='shop_price',lookup_expr='gt')
    price_max = django_filters.NumberFilter(name='shop_price',lookup_expr='lt')
    name = django_filters.CharFilter(name='name',lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price_min','price_max','name']


