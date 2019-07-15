from django.urls import path
from . import views

app_name = 'plan'

urlpatterns = [
    path('', views.plan_detail, name='plan_detail'),
    path('add/<int:place_id>/',
         views.plan_add,
         name='plan_add'),
    path('remove/<int:place_id>/',
         views.plan_remove,
         name='plan_remove'),
    ]