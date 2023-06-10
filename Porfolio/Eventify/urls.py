from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('get_event/', views.eventpage, name="get_event"),
]
