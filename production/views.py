from django.shortcuts import render
# Make sure your actual model name is imported here!
from .models import ProductionTask 

def dashboard_view(request):
    # Fetch the tasks
    tasks = ProductionTask.objects.all().order_by('series', 'production_date') 
    
    # Send them to the template
    return render(request, 'production/dashboard.html', {'tasks': tasks})
