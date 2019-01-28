from rest_framework import routers, viewsets
from django.contrib.auth.models import User
from api.models import Category, Subcategory, Product, ProductImg, Company, Contact, Order, Language
from api.serializers import LanguageSerializer, UserSerializer, CategorySerializer, SubcategorySerializer, ProductSerializer, CompanySerializer, ContactSerializer, ProductImgSerializer, OrderSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProductImgViewSet(viewsets.ModelViewSet):
    queryset = ProductImg.objects.all()
    serializer_class = ProductImgSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
