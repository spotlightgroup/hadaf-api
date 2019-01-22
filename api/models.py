from django.db import models


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
