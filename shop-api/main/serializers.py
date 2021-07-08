from rest_framework import serializers

from mainapp.models import Product, Cart, Customer, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer

    class Meta:
        model = Product
        fields = '__all__'

