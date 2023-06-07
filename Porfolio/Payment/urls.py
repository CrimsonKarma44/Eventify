from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('payment/', views.make_payment, name='make_payment'),
    path('payment/callback/', views.payment_callback, name='payment_callback'),
]
