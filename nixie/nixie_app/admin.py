from django.contrib import admin
from .models import Product
from .models import Review


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']

    prepopulated_fields = {'slug': ('name',)}


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'review_text', 'available']
    list_filter = ['available']
    list_editable = ['available']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
