from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('get_event/<int:id>/', views.eventPage, name="getEvent"),
    path('get_event/<int:id>/delete/', views.delete_event, name='delete-event'),
    path('events/category/<str:type>/', views.eventCategory, name="categoryEvents"),
    path('get_myEvents/', views.myEvents, name="myEvents"),
    path('Events/getall', views.allEvents, name="allEvents"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/update/', views.profile_update_view, name='profile_update'),
    path('event/create/', views.create_event, name='create-event'),
    path('event/update/<int:id>', views.updateEvent, name='updateEvent'),
    path('logout/', views.logout_view, name='logout'),
    path('all_events/', views.allEvents, name='all_events'),
    path('get_tickets/<int:id>/', views.eventTickets, name='viewEventTickets'),
    path('api/events/search/<str:query>', views.searchEvent, name='searchEvent')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
