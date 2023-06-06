import qrcode
import io
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from .forms import EventForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def event_create(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'event-create.html', context)


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
