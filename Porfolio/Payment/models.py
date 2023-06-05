from django.db import models
from Ticket.models import Ticket

# Create your models here.
class Payment(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    price = models.FloatField()
    email = models.CharField(max_length=100)
    code = models.CharField(max_length=60)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.ticket_id)
