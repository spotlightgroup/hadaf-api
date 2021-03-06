from django.db import models
from django.contrib.auth.models import User


# language model
class Language(models.Model):

    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.code


# category model
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# subcategory model
class Subcategory(models.Model):
    class Meta:
        verbose_name_plural = 'Subcategories'

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1, related_name='subcategories')

    def __str__(self):
        return self.name


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'contacts'

    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    email1 = models.CharField(max_length=50)
    email2 = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    zipCode = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.email1


# company model
class Company(models.Model):
    class Meta:
        verbose_name_plural = 'companies'

    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, default=1, related_name='company')

    def __str__(self):
        return self.name


# product model
class Product(models.Model):
    class Meta:
        verbose_name_plural = 'products'

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    unit = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.IntegerField()
    priority = models.IntegerField()
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, default=1, related_name='products')
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, default=1, related_name='product')

    def __str__(self):
        return self.name


# product image model
class ProductImg(models.Model):
    url = models.ImageField(upload_to="imgs/products")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=1, related_name='productImgs')

    def __str__(self):
        return self.url.url


# order model
class Order(models.Model):
    class Meta:
        verbose_name_plural = 'orders'

    email = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=1, related_name='orders')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, related_name='orders')

    def __str__(self):
        return self.product.name


# models translations ==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=----
# category translation model
class CategoryTranslation(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.language.code


# subcategory translation model
class SubcategoryTranslation(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=1)
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.language.code


# Product translation model
class ProductTranslation(models.Model):
    class Meta:
        verbose_name_plural = 'products translations'

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    unit = models.CharField(max_length=20)
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.language.code
