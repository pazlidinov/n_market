from django.contrib import admin
from .models import DeliveredItem, DeliveringCompany
# Register your models here.

@admin.register(DeliveringCompany)
class DeliveringCompanyAdmin(admin.ModelAdmin):
    list_display = ["id", 'company_name', 'code']
    prepopulated_fields = {"slug": ("company_name",)}


@admin.register(DeliveredItem)
class DeliveredItemAdmin(admin.ModelAdmin):
    list_display = ["id", 'company_name', 'recipient']