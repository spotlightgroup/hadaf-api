from django.contrib import admin
from api.models import Category, Subcategory, Product, Company, Contact, ProductImg, CategoryTranslation, Language


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'description', 'available_translations']

    def available_translations(self, obj):
        t = list(CategoryTranslation.objects.filter(category__id=obj.id))
        return t


class CategoryTranslationAdmin(admin.ModelAdmin):
    model = CategoryTranslation
    list_display = ['category_name', 'description', 'language_code']

    def language_code(self, obj):
        return obj.language.code

    def category_name(self, obj):
        return obj.category.name


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ['name', 'description', 'type', 'code', 'email']

    def email(self, obj):
        return obj.contact.email1


# Register your models here.
admin.site.register(Language)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryTranslation, CategoryTranslationAdmin)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact)
admin.site.register(ProductImg)
