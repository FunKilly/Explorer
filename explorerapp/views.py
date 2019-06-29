from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import City, Category, Place


def index(request):
    # Strona glowna.
    places = Place.objects.all()[:10]
    context = {'places': places}
    return render(request, 'explorer/index.html', context)


def place_detail(request, id, slug):
    place = get_object_or_404(Place, id=id, slug=slug)
    context = {'place': place}
    return render(request, 'explorer/place_detail.html', context)

def places_list_by_category(request):
    category = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    context = {'category': category}
    return render(request, 'explorer/category.html', context)