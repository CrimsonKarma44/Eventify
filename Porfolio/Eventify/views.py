import qrcode
import io
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

from Ticket.models import Ticket
from .forms import EventForm, ProfileUpdateForm, LoginForm
from .models import Event


# Create your views here.


def home(request):
    events = Event.objects.all()
    context = {'events': events[:3]}
    return render(request, 'home.html', context)


def eventPage(request, id):
    data = Event.objects.get(id=id)
    tickets = Ticket.objects.filter(event_id=data.id)
    context = {'event': data, 'tickets': tickets}
    return render(request, 'eventpage.html', context)

def myEvents(request):
    return HttpResponse('This is my events')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            profile_form = ProfileUpdateForm(request.POST)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
            return redirect('/')
    else:
        form = RegistrationForm()
        profile_form = ProfileUpdateForm()

    context = {
        'form': form,
        'profile_form': profile_form
    }

    return render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile_update')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def profile_update_view(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile_update')
    else:
        form = ProfileUpdateForm(instance=user.userprofile)
    
    return render(request, 'profile_update.html', {'form': form})
