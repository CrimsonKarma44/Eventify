# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket

def purchaseTicket(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    context = {'ticket': ticket}
    return render(request, 'ticket_purchase.html', context)

def allTickets(request):
    title = 'All tickets'
    tickets = Ticket.objects.all()
    context = {'tickets': tickets, 'title': title}
    return render(request, 'tickets.html', context)
