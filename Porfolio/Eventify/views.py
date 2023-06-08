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
    evemts = Event.objects.all()
    context = {'events': evemts[:3]}
    return render(request, 'home.html', context)


def eventpage(request, event):
    data = Event.objects.get(name=event)
    context = {'event': data}
    return render(request, 'eventpage.html', context)


def event_create(request):
    form = EventForm()
    if request.method == 'POST':
        print(request.POST)
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('home')
        # return HttpResponse(form)
    context = {
        'form': form
    }
    return render(request, 'event-create.html', context)


def event_update(request, event):
    data = Event.objects.get(name=event)
    form = EventForm(instance=data)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=data)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'event-create.html', context)


def event_delete(request, event):
    data = Event.objects.get(name=event)
    if request.method == 'POST':
        data.delete()
        return redirect('home')
    context = {
        'form': data
    }
    return render(request, 'event-delete.html', context)


def send_email_message(request):
    # generate qrcode
    data = 'ikenna@gmail.com_1001'

    # Generate the QR code image
    qr_code = qrcode.make(data)

    byte_stream = io.BytesIO()
    qr_code.save(byte_stream, format='PNG')

    # Set the byte stream position to the beginning
    byte_stream.seek(0)

    # Return the QR code image as a Django HttpResponse
    response = HttpResponse(byte_stream, content_type="image/png")
    return response
