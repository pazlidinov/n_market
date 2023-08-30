from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(StatusProduct)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'manager']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ["id", 'brand_name', 'inn']
    prepopulated_fields = {"slug": ("brand_name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", 'title', 'slug']
    prepopulated_fields = {"slug": ("title",)}
