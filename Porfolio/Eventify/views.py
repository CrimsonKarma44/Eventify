import qrcode
import io
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from .forms import EventForm
from .models import Event



# Create your views here.


def home(request):
    events = Event.objects.all()
    context = {'events': events[:3]}
    return render(request, 'home.html', context)


def eventPage(request, id):
    data = Event.objects.get(id=id)
    context = {'event': data}
    return render(request, 'eventpage.html', context)

def myEvents(request):
    return HttpResponse('This is my events')
