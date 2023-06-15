from django.urls import path
from . import views

urlpatterns = [
    path('ticket/<int:id>/purchase/', views.payment, name='payment'),
    path('payment/<int:id>/', views.make_payment, name='make_payment'),
    path('callback/', views.payment_callback, name='payment_callback'),
    path('sendemail/', views.send_email, name='send_email'),
    path('getcode/', views.getCode, name='getcode'),
    path('present/<str:email>/<str:code>/', views.present, name='present'),
]
