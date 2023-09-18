from django.contrib import admin
from .models import *
# Register your models here.




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'manager']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'slug']
    prepopulated_fields = {"slug": ("name",)}




@admin.register(SaledProduct)
class SaledProductAdmin(admin.ModelAdmin):
    list_display = ["id", 'cashier', 'product','count_product','time']
    
