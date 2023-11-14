from django.contrib import admin
from app.models import Product, Category, Modifier


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['iico_id',
                    'category',
                    'name',
                    'weight',
                    'energyAmount',
                    'energyFullAmount',
                    'currentPrice',
                    'description',
                    'proteinsAmount',
                    'fatAmount',
                    'carbohydratesAmount',
                    'proteinsFullAmount',
                    'fatFullAmount',
                    'carbohydratesFullAmount',
                    'additionalInfo',
                    'imageLinks']
    list_filter = ['category']
    list_editable = ['name', 'description', 'additionalInfo', 'imageLinks']


@admin.register(Category)
class AdminProduct(admin.ModelAdmin):
    list_display = ['iico_id',
                    'slug',
                    'name']
    list_editable = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Modifier)
class AdminProduct(admin.ModelAdmin):
    list_display = ['iico_id',
                    'name']
    list_editable = ['name']

