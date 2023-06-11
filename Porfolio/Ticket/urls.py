from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('', views.ticketList, name='ticket_list'),
    path('create/', views.createTicket, name='ticket_create'),
    path('<int:pk>/', views.ticketDetail, name='ticket_detail'),
    path('<int:pk>/update/', views.updateTicket, name='ticket_update'),
    path('<int:pk>/delete/', views.deleteTicket, name='ticket_delete'),
    path('<int:id>/purchase/', views.purchaseTicket, name='ticket_purchase'),
]
