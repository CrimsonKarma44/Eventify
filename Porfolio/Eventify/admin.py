from django.contrib import admin
from .models import Category, Event, UserProfile

# Register your models here.
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(UserProfile)
