import qrcode
import io
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from Ticket.models import Ticket
from .forms import EventForm
from .models import Event



# Create your views here.


def home(request):
    events = Event.objects.all()
    context = {'events': events[:3]}
    return render(request, 'home.html', context)


def eventpage(request, event):
    data = Event.objects.get(name=event)
    tickets = Ticket.objects.filter(event_id=data.id)
    context = {'event': data, 'tickets': tickets}
    return render(request, 'eventpage.html', context)
