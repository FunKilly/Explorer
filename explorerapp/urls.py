from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/<slug:slug>/', views.PlaceView.as_view(), name='place_detail'),
    path('places/', views.places_list, name='places_list'),
    path('<slug:category_slug>/', views.places_list_by_category, name='places_list_by_category'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)