from django.contrib import admin
from api import models

# setting the header
admin.site.site_header = 'HadafOnline Admin Dashboard'


class CategoryTranslationInline(admin.TabularInline):
    model = models.CategoryTranslation
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryTranslationInline]
    model = models.Category
    list_display = ['name', 'description', 'available_translations']

    def available_translations(self, obj):
        return list(models.CategoryTranslation.objects.filter(category__id=obj.id))


class SubcategoryTranslationInline(admin.TabularInline):
    model = models.SubcategoryTranslation
    extra = 1


class SubcategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryTranslationInline]
    model = models.Subcategory
    list_display = ['name', 'description',
                    'category', 'available_translations']

    def available_translations(self, obj):
        return list(models.SubcategoryTranslation.objects.filter(subcategory__id=obj.id))


class CompanyAdmin(admin.ModelAdmin):
    model = models.Company
    list_display = ['name', 'description', 'type', 'code', 'email']

    def email(self, obj):
        return obj.contact.email1


class LanguageAdmin(admin.ModelAdmin):
    model = models.Language
    list_display = ['name', 'code']


class ProductImgInline(admin.TabularInline):
    model = models.ProductImg
    extra = 1


class ProductTranslationInline(admin.TabularInline):
    model = models.ProductTranslation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    model = models.Product
    inlines = [ProductImgInline, ProductTranslationInline]
    list_display = ['name', 'description', 'unit',
                    'quantity', 'price', 'category', 'subcategory', 'company', 'priority', 'available_translations']

    def category(self, obj):
        return obj.subcategory.category

    def available_translations(self, obj):
        return list(models.ProductTranslation.objects.filter(product__id=obj.id))


# Register your models here.
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Subcategory, SubcategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Order)
