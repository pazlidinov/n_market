from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(DeliveredItem)
class DeliveredItem(admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ("name",)}

@admin.register(DeliveringCompany)
class DeliveringCompany(admin.ModelAdmin):
  
    prepopulated_fields = {"slug": ("company_name",)}