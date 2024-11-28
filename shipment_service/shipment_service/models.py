# shipment_service/models.py
from django.db import models

class Shipment(models.Model):
    order_id = models.IntegerField()
    shipped_at = models.DateTimeField(auto_now_add=True)

class ShipmentItem(models.Model):
    shipment = models.ForeignKey(Shipment, related_name='items', on_delete=models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
