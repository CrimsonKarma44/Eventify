from django.db import models
from Ticket.models import Ticket

# Create your models here.
class Payment(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    price = models.FloatField()
    email = models.CharField(max_length=100)
    code = models.CharField(max_length=60)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    transaction_id = models.BigIntegerField(verbose_name="Transaction Id")
    present = models.BooleanField(default=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        ticket_name = self.ticket_id
        return f"{self.email} {self.price} payment for {ticket_name}"
    
    @classmethod
    def get_payment_by_ticket_id(cls, ticket_id):
        try:
            payment = cls.objects.get(ticket_id=ticket_id)
            return payment
        except cls.DoesNotExist:
            return None
