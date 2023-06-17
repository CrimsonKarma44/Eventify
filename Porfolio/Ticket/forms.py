from django import forms
from .models import Ticket

class TicketCreationForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_type', 'price', 'quantity_available']

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_type', 'price', 'quantity_available']
