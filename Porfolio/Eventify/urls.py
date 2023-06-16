from django.urls import path
from . import views

# app_name = 'event'

urlpatterns = [
    path('', views.home, name="home"),
    path('get_event/<int:id>/', views.eventPage, name="getEvent"),
    path('events/category/<str:type>/', views.eventCategory, name="categoryEvents"),
    # path('get_myEvents/', views.myEvents, name="myEvents"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/update/', views.profile_update_view, name='profile_update'),
    path('events/all', views.allEvents, name= 'all_events')
]
