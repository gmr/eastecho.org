from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('club/<str:club_slug>', views.club, name='club'),
]

