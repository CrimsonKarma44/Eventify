from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('send_qrCode/', views.send_email_message, name="qrCode"),
    path('event-create/', views.event_create, name="create-event")
]
