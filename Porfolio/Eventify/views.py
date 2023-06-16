import qrcode
import io
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

from Ticket.models import Ticket
from .forms import EventForm, ProfileUpdateForm, LoginForm
from .models import Event


# Create your views here.


def home(request):
    events = Event.objects.all()
    title = 'Home'
    context = {'events': events[:3], 'title': title}
    return render(request, 'home.html', context)


def eventPage(request, id):
    title = 'Event page'
    data = Event.objects.get(id=id)
    tickets = Ticket.objects.filter(event_id=data.id)
    context = {'event': data, 'tickets': tickets, 'title': title}
    return render(request, 'eventpage.html', context)


def eventCategory(request, type):
    title = f'{type} Events'
    fullType = type
    if type == 'Concert':
        type = 'Con'
    elif type == 'Communities':
        type = 'Com'
    elif type == 'Classes':
        type = 'Cl'
    elif type == 'Parties':
        type = 'P'
    elif type == 'Sport':
        type = 'S'
    events = Event.objects.filter(type=type)
    # print(events)
    context = {'events': events, 'mainType': fullType, 'title': title}
    return render(request, 'eventCategory.html', context)


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
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    form = EventForm()
    context = {'form': form}
    return render(request, 'event-create.html', context)


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


def logout_view(request):
    logout(request)
    return redirect('/')


def myEvents(request):
    title = 'My Events'
    return HttpResponse("This are my events")


def allEvents(request):
    title = 'All Events'
    events = Event.objects.all()
    context = {'events': events, 'title': title}
    return render(request, 'events.html', context)
