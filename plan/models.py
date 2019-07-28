'''from django.db import models

class PlanEvent(models.Model):
    name = models.CharField(max_length=60)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)

class PlanHistory(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()'''


