from django.contrib import admin
from api.models import Category, Subcategory, Product, Company, Contact, ProductImg, CategoryTranslation, Language


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['id', 'name', 'description', 'available_translations']

    def available_translations(self, obj):
        t = list(CategoryTranslation.objects.filter(category__id=obj.id))
        return t


# Register your models here.
admin.site.register(Language)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryTranslation)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(ProductImg)
