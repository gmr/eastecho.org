from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('club/<str:club_slug>', views.club, name='club'),
    path('clubs', views.clubs, name='clubs'),
    path('events', views.events, name='events'),
    path('this-week', views.this_week, name='this-week'),
]

