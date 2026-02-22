from django.db import models

class ProductionTask(models.Model):
    lot_number = models.CharField(max_length=20)
    model_name = models.CharField(max_length=100)
    ckd_arrival_iea = models.CharField(max_length=100, blank=True)
    prd_customer = models.CharField(max_length=100, blank=True)
    daily_target = models.IntegerField(default=0)
    total_units = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.lot_number} - {self.model_name}"

