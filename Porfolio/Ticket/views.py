# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Event
from .forms import TicketCreationForm, TicketUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers import serialize
from django.http import JsonResponse


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
    title = 'Create ticket'
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
    
    return render(request, 'create_ticket.html', {'form': form, 'event_name':event_name, 'title': title})

@login_required
def update_ticket(request, id):
    title = 'Edit ticket'
    ticket = Ticket.objects.get(id=id)
    
    if request.method == 'POST':
        form = TicketUpdateForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            event = Event.objects.get(name=ticket.event_id)
            return redirect('viewEventTickets', id=event.id)
    else:
        form = TicketUpdateForm(instance=ticket)
    
    return render(request, 'update_ticket.html', {'form': form, 'ticket': ticket, 'title': title})

@login_required
def delete_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    ticket.delete()
    event = Event.objects.get(name=ticket.event_id)
    return redirect('viewEventTickets', id=event.id)


@csrf_exempt
def searchTicket(request, query):
    results = Ticket.objects.filter(name__icontains=query)
    json_data = serialize('json', results)
    parsed_data = json.loads(json_data)
    for obj in parsed_data:
        # print(obj['fields']['event_id'])
        event = Event.objects.get(id=obj['fields']['event_id'])
        img = str(event.img)
        # print(img)
        obj['fields']['img'] = img
        # print(obj)
    updated_json_data = json.dumps(parsed_data)
    updated_parsed_data = json.loads(updated_json_data)
    # print(updated_parsed_data)
    return JsonResponse(updated_parsed_data, safe=False)
