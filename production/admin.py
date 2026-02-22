from django.contrib import admin
from .models import ProductionTask

@admin.register(ProductionTask)
class ProductionTaskAdmin(admin.ModelAdmin):
    list_display = ('lot_number', 'model_name', 'daily_target', 'total_units', 'prd_customer')
    search_fields = ('lot_number', 'model_name', 'prd_customer')
