from django.db import models
from Eventify.models import Event

# Create your models here.

class Ticket(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    ticket_type =  models.CharField(max_length=100)
    price = models.FloatField()
    quantity_available = models.PositiveIntegerField()
    avail_status = models.BooleanField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def is_sold_out(self):
        return self.quantity_available <= 0
