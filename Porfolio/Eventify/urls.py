from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('get_event/<int:id>/', views.eventPage, name="getEvent"),
    path('get_myEvents/', views.myEvents, name="myEvents"),
]
