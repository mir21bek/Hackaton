from rest_framework import serializers

from .models import Category, Menu


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug', 'image')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'slug', 'category', 'description', 'image', 'price', 'available', 'popular')

