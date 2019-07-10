import django_filters
from django.utils.translation import gettext_lazy as _
from .models import Place, Category


class PlaceFilter(django_filters.FilterSet):
    class Meta:
        model = Place
        fields = {'name':['exact'],
                  'cost':['lt','gt'],
                  'address__city':['exact'],
                  'category':['exact']
                  }

