from django.db import models
from Ticket.models import Ticket

# Create your models here.
class Payment(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    price = models.FloatField()
    email = models.CharField(max_length=100)
    code = models.CharField(max_length=60)
    phone_no = models.CharField(max_length=20, blank=True, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ticket_id)
    
    @classmethod
    def get_payment_by_ticket_id(cls, ticket_id):
        try:
            payment = cls.objects.get(ticket_id=ticket_id)
            return payment
        except cls.DoesNotExist:
            return None
