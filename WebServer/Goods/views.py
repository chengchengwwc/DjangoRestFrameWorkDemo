from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Goods.models import *
from rest_framework import mixins
from rest_framework import generics
from Goods.serializer import GoodsSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from Goods.filters import ProductFilter
from rest_framework import filters

# Create your views here.

# class GoodsList(APIView):

#     def get(self,request,format=None):
#         goods = Goods.objects.all()[:10]
#         goods_json = GoodsSerializer(goods,many=True)
#         return Response(goods_json.data)

#     def post(self,request,format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100



class GoodsListView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination


    
class GoodsDemoView(mixins.ListModelMixin,viewsets.GenericViewSet):
    #queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        quertset = Goods.objects.all()
        price_min = self.request.query_params.get("price_min",0)
        if price_min:
            quertset = Goods.objects.filter(shop_price__gt=price_min)
        return quertset


class GoodsDemoView1(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filter_class = ProductFilter
    search_fields = ('name','goods_brief','goods_desc')





