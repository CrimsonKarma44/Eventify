from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('get_event/<int:id>/', views.eventPage, name="getEvent"),
    path('events/category/<str:type>/', views.eventCategory, name="categoryEvents"),
=======
    path('get_myEvents/', views.myEvents, name="myEvents"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/update/', views.profile_update_view, name='profile_update'),
>>>>>>> 34d5d098221f6cfb4fa220d90b19f1c24a7f9292
]
