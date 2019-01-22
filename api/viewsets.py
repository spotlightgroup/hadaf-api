from rest_framework import routers, viewsets
from django.contrib.auth.models import User
from api.models import Category, Subcategory, Product, Company, Contact
from api.serializers import UserSerializer, CategorySerializer, SubcategorySerializer, ProductSerializer, CompanySerializer, ContactSerializer


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


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
