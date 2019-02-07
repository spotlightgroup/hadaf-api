from django.contrib import admin
from api.models import Category, Subcategory, Product, Company, Contact, ProductImg, CategoryTranslation, Language, SubcategoryTranslation, ProductTranslation


# setting the header
admin.site.site_header = 'HadafOnline Admin Dashboard'


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'description', 'available_translations']

    def available_translations(self, obj):
        return list(CategoryTranslation.objects.filter(category__id=obj.id))


class SubcategoryAdmin(admin.ModelAdmin):
    model = Subcategory
    list_display = ['name', 'description',
                    'category', 'available_translations']

    def available_translations(self, obj):
        return list(SubcategoryTranslation.objects.filter(subcategory__id=obj.id))


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ['name', 'description', 'type', 'code', 'email']

    def email(self, obj):
        return obj.contact.email1


class LanguageAdmin(admin.ModelAdmin):
    model = Language
    list_display = ['name', 'code']


class ProductImgInline(admin.TabularInline):
    model = ProductImg
    extra = 3


class ProductTranslationInline(admin.TabularInline):
    model = ProductTranslation
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ProductImgInline, ProductTranslationInline]
    list_display = ['name', 'description', 'unit',
                    'quantity', 'price', 'category', 'subcategory', 'company', 'priority', 'available_translations']

    def category(self, obj):
        return obj.subcategory.category

    def available_translations(self, obj):
        return list(ProductTranslation.objects.filter(product__id=obj.id))


# Register your models here.
admin.site.register(Language, LanguageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Company, CompanyAdmin)
