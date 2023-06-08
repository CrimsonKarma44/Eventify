from django.forms import ModelForm
from .models import Event
# from django import forms
# from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
