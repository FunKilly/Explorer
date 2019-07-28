from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.event_create, name='event_create'),
]