from django.contrib import admin
from api.models import Category, Subcategory, Product, Company, Contact, ProductImg, CategoryTranslation, Language

# Register your models here.


admin.site.register(Language)
admin.site.register(Category)
admin.site.register(CategoryTranslation)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(ProductImg)
