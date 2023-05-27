from django.contrib import admin
from .models import Review, Tickets, Payments, Categories, Events

# Register your models here.
admin.site.register(Review)
admin.site.register(Tickets)
admin.site.register(Payments)
admin.site.register(Categories)
admin.site.register(Events)
