from rest_framework import routers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from api import models, serializers


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def list(self, request):
        language = request.GET.get('lang')
        if language is None or language.lower() == 'en':
            categories = models.Category.objects.all()
            serializer = serializers.CategorySerializer(
                categories, many=True)
            return Response(serializer.data)

        else:
            categories = models.CategoryTranslation.objects.filter(
                language__code=language.upper())
            serializer = serializers.CategoryTranslationSerializer(
                categories, many=True)
            return Response(serializer.data)


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Subcategory.objects.all()
    serializer_class = serializers.SubcategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class ProductImgViewSet(viewsets.ModelViewSet):
    queryset = models.ProductImg.objects.all()
    serializer_class = serializers.ProductImgSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
