from django.contrib import admin
from .models import Review, Tickets, Payments, Categories, Events

# Register your models here.
admin.register(Review)
admin.register(Tickets)
admin.register(Payments)
admin.register(Categories)
admin.register(Events)
