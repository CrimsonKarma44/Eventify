# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Event
from .forms import TicketCreationForm, TicketUpdateForm
from django.contrib.auth.decorators import login_required


def purchaseTicket(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    context = {'ticket': ticket}
    return render(request, 'ticket_purchase.html', context)

def allTickets(request):
    title = 'All tickets'
    tickets = Ticket.objects.all()
    context = {'tickets': tickets, 'title': title}
    return render(request, 'tickets.html', context)

@login_required
def create_ticket(request, event_name):
    if request.method == 'POST':
        event = Event.objects.get(name=event_name)
        form = TicketCreationForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.avail_status = True
            ticket.event_id = event
            ticket.save()
            return redirect('viewEventTickets', id=event.id)
    else:
        form = TicketCreationForm()
    
    return render(request, 'create_ticket.html', {'form': form, 'event_name':event_name})

@login_required
def update_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    
    if request.method == 'POST':
        form = TicketUpdateForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            event = Event.objects.get(name=ticket.event_id)
            return redirect('viewEventTickets', id=event.id)
    else:
        form = TicketUpdateForm(instance=ticket)
    
    return render(request, 'update_ticket.html', {'form': form, 'ticket': ticket})

@login_required
def delete_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    ticket.delete()
    event = Event.objects.get(name=ticket.event_id)
    return redirect('viewEventTickets', id=event.id)