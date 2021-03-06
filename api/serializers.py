from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Category, Subcategory, Product, Company, Contact, ProductImg, Order, Language, CategoryTranslation

""" Serializers define the API representation."""


# the language model serializer
class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'code', 'name')


# the user model serializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_staff')


# the subcategory model serializer
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'description', 'category')


# the category model serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


# the category translation model serializer
class CategoryTranslationSerializer(serializers.ModelSerializer):
    language = serializers.SlugRelatedField(
        read_only=True,
        slug_field='code'
    )
    category = CategorySerializer()

    class Meta:
        model = CategoryTranslation
        fields = ('category', 'name', 'language',
                  'description')


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'address1', 'address2', 'email1', 'email2',
                  'phone1', 'phone2', 'fax', 'zipCode', 'city', 'country')


class CompanySerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'code', 'type', 'contact')


# the product model serializer
class ProductImgSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImg
        fields = ('id', 'url', 'product')


# the product model serializer
class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer()
    company = CompanySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'unit', 'quantity',
                  'price', 'priority', 'subcategory', 'company', 'productImgs')


# the order model serializer
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'id', 'email', 'description', 'quantity', 'product', 'user')
