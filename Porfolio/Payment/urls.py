from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('payment/', views.make_payment, name='make_payment'),
    path('callback/', views.payment_callback, name='payment_callback'),
    path('sendemail/', views.send_email, name='send_email'),
]
