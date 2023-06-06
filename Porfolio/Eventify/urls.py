from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('send_qrCode/', views.send_email_message, name="qrCode"),
    path('event-create/', views.event_create, name="create-event"),
    path('<event>/', views.eventpage, name="event"),
    path('<event>/update/', views.event_update, name="update-event"),
    path('<event>/delete/', views.event_delete, name="delete-event")
]
