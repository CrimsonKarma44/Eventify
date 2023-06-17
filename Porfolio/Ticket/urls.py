from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('<int:id>/purchase/', views.purchaseTicket, name='ticket_purchase'),
    path('tickets/all', views.allTickets, name='all_tickets'),
    path('create/<str:event_name>/', views.create_ticket, name='create_ticket'),
    path('update/<int:id>/', views.update_ticket, name='update_ticket'),
    path('delete/<int:id>/', views.delete_ticket, name='delete_ticket'),
]
