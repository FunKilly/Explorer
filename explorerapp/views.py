from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import City, Category, Place
from .forms import RatingForm

def index(request):
    # Strona glowna.
    places = Place.objects.all()[:10]
    context = {'places': places}
    return render(request, 'explorer/index.html', context)


def place_detail(request, id, slug):
    place = get_object_or_404(Place, id=id, slug=slug)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            place.sum_of_rating += int(form.cleaned_data['Rating'])
            place.num_of_ratings += 1
            place.save()
            return redirect('explorer:place_detail', id=id, slug=slug)

    else:
        form = RatingForm

    context = {'place': place,'form':form}
    return render(request, 'explorer/place_detail.html', context)


def places_list_by_category(request):
    category = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    context = {'category': category}
    return render(request, 'explorer/category.html', context)