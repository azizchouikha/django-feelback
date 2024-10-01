from django.db import models

# Create your models here.
from django.db import models

class Order(models.Model):
    order_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Response(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='responses')
    delivery_time_rating = models.IntegerField()
    package_condition_rating = models.IntegerField()
    courier_behavior_rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
