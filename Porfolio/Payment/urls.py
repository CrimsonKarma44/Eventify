from django.urls import path
from . import views

urlpatterns = [
    path('ticket/<int:id>/purchase/', views.payment, name='payment'),
    path('payment/<int:id>/', views.make_payment, name='make_payment'),
    path('callback/<int:user_id>', views.payment_callback, name='payment_callback'),
    path('sendemail/', views.send_email, name='send_email'),
    path('present/<str:email>/<str:code>/', views.present, name='present'),
]
