from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Category, Subcategory

""" Serializers define the API representation."""


# the user model serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# the category model serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'subcategories')


# the subcategory model serializer
class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'description', 'category')
