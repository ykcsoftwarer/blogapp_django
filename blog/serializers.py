from rest_framework import serializers
from .models import Category, Blog


class CategorySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Category
        fields = (
            'id',
            'nane'
        )
        
        
class BlogSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'content',
            'category',
            'is_published',
            'created_date',            
        )
    