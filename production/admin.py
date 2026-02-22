from django.contrib import admin
from .models import ProductionTask

@admin.register(ProductionTask)
class ProductionTaskAdmin(admin.ModelAdmin):
    list_display = ('series', 'lot_number', 'model_name', 'daily_target', 'total_units', 'prd_customer')
    search_fields = ('lot_number', 'model_name', 'prd_customer')
list_filter = ('series', 'production_date')
date_hierarchy = 'production_date'