from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Category, Blog

# Create your views here.

from .serializers import CategorySerializer

    
class CategoryView(ModelViewSet):
  queryset  = Category.objects.all()
  serializer_class = CategorySerializer
  


class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = None