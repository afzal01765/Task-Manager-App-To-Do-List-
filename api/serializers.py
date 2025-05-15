from rest_framework import serializers 
from .models import Category , TodoTask 


class ToDoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask 
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"