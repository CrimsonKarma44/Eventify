# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket

def ticketList(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'tickets/ticket_list.html', context)

def createTicket(request):
    # Logic to handle ticket creation form submission
    if request.method == 'POST':
        pass
        # Process the submitted data and create a new ticket
        # Redirect to the ticket detail page or ticket list page

    # Render the ticket creation form template
    return render(request, 'tickets/ticket_create.html')

def ticketDetail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    context = {'ticket': ticket}
    return render(request, 'tickets/ticket_detail.html', context)

def updateTicket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    # Logic to handle ticket update form submission
    if request.method == 'POST':
        pass
        # Process the submitted data and update the ticket
        # Redirect to the ticket detail page or ticket list page

    # Render the ticket update form template
    context = {'ticket': ticket}
    return render(request, 'tickets/ticket_update.html', context)

def deleteTicket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    # Logic to handle ticket deletion confirmation
    if request.method == 'POST':
        pass
        # Delete the ticket from the database
        # Redirect to the ticket list page

    # Render the ticket deletion confirmation template
    context = {'ticket': ticket}
    return render(request, 'tickets/ticket_delete.html', context)

def purchaseTicket(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    context = {'ticket': ticket}
    return render(request, 'ticket_purchase.html', context)
