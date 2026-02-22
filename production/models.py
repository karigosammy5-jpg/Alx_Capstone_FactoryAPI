from django.db import models
from django.utils import timezone

class ProductionTask(models.Model):
   # Choices for the dropdown
    SERIES_CHOICES = [
        ('N', 'N-Series (Light Duty)'),
        ('F', 'F-Series (Medium Duty)'),
    ]
    
    # New Field
    series = models.CharField(
        max_length=1, 
        choices=SERIES_CHOICES, 
        default='F'
    )
   # The "When" - adding the date field
    production_date = models.DateField(default=timezone.now)

    lot_number = models.CharField(max_length=20)
    model_name = models.CharField(max_length=100)
    ckd_arrival_iea = models.CharField(max_length=100, blank=True)
    prd_customer = models.CharField(max_length=100, blank=True)
    daily_target = models.IntegerField(default=0)
    total_units = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.lot_number} - {self.model_name}"

