from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('<int:id>/purchase/', views.purchaseTicket, name='ticket_purchase'),
    path('tickets/all', views.allTickets, name='all_tickets')
]
