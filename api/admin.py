from django.contrib import admin
from api.models import Category, Subcategory, Product, Company, Contact, ProductImg, CategoryTranslation, Language, SubcategoryTranslation, ProductTranslation


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


class CategoryTranslationAdmin(admin.ModelAdmin):
    model = CategoryTranslation
    list_display = ['category_name', 'translated_name',
                    'language_code', 'language_name']

    def language_code(self, obj):
        return obj.language.code

    def language_name(self, obj):
        return obj.language.name

    def category_name(self, obj):
        return obj.category.name

    def translated_name(self, obj):
        return obj.name


class SubcategoryTranslationAdmin(admin.ModelAdmin):
    model = SubcategoryTranslation
    list_display = ['subcategory_name', 'translated_name',
                    'language_code', 'language_name']

    def language_code(self, obj):
        return obj.language.code

    def subcategory_name(self, obj):
        return obj.subcategory.name

    def translated_name(self, obj):
        return obj.name

    def language_name(self, obj):
        return obj.language.name


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ['name', 'description', 'type', 'code', 'email']

    def email(self, obj):
        return obj.contact.email1


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['company', 'email1', 'email2', 'phone1',
                    'phone2', 'address1', 'address2', 'fax', 'zipCode', 'country', 'city']

    def company(self, obj):
        return Company.objects.filter(contact__id=obj.id).first()


class LanguageAdmin(admin.ModelAdmin):
    model = Language
    list_display = ['name', 'code']


class ProductImgAdmin(admin.ModelAdmin):
    model = ProductImg
    list_display = ['product', 'url']


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'description', 'unit',
                    'quantity', 'price', 'category', 'subcategory', 'company', 'priority']

    def category(self, obj):
        return obj.subcategory.category


class ProductTranslationAdmin(admin.ModelAdmin):
    model = ProductTranslation
    list_display = ['product_name', 'translated_name',
                    'language_code', 'language_name']

    def product_name(self, obj):
        return obj.product.name

    def language_code(self, obj):
        return obj.language.code

    def translated_name(self, obj):
        return obj.name

    def language_name(self, obj):
        return obj.language.name


# Register your models here.
admin.site.register(Language, LanguageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductTranslation, ProductTranslationAdmin)
admin.site.register(CategoryTranslation, CategoryTranslationAdmin)
admin.site.register(SubcategoryTranslation, SubcategoryTranslationAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ProductImg, ProductImgAdmin)
