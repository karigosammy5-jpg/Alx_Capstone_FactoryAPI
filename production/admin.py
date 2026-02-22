from django.contrib import admin
from .models import ProductionTask

@admin.register(ProductionTask)
class ProductionTaskAdmin(admin.ModelAdmin):
    # This defines the columns you see in the list
    list_display = ('production_date', 'series', 'lot_number', 'model_name', 'daily_target')
    
    # THIS creates the calendar timeline bar at the top
    date_hierarchy = 'production_date' 
    
    # THIS creates the "Series" and "Date" sidebar filters on the right
    list_filter = ('series', 'production_date') 
    
    # This adds the search bar
    search_fields = ('lot_number', 'model_name')