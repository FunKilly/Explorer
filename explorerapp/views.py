from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import City, Category, Place, Comment
from .forms import RatingForm, CommentForm
from .filters import PlaceFilter

def index(request):
    # Strona glowna.
    places = Place.objects.all()[:10]
    context = {'places': places}
    return render(request, 'explorer/index.html', context)


class PlaceView(View):
    template_name = 'explorer/place_detail.html'

    def place_detail(self):
        place = get_object_or_404(Place, id=self.kwargs['id'], slug=self.kwargs['slug'])
        return place

    def comments_get(self):
        place = get_object_or_404(Place, id=self.kwargs['id'], slug=self.kwargs['slug'])
        comments = place.comments.filter(active=True)
        return comments

    def get_context_data(self,  **kwargs):

        kwargs['place'] = self.place_detail()
        kwargs['comments'] = self.comments_get()
        if 'rating_form' not in kwargs:
            kwargs['rating_form'] = RatingForm()
        if 'comment_form' not in kwargs:
            kwargs['comment_form'] = CommentForm()
        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        ctxt = {}

        if 'rating' in request.POST:
            rating_form = RatingForm(request.POST)

            if rating_form.is_valid():
                place = get_object_or_404(Place, id=self.kwargs['id'], slug=self.kwargs['slug'])
                place.sum_of_rating += int(rating_form.cleaned_data['Rating'])
                place.num_of_ratings += 1
                place.save()
                return redirect('explorer:place_detail', id=self.kwargs['id'], slug=self.kwargs['slug'])
            else:

                ctxt['rating_form'] = rating_form

        elif 'comment' in request.POST:
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                place = self.place_detail()
                new_comment.place = place
                new_comment.save()

                return redirect('explorer:place_detail', id=self.kwargs['id'], slug=self.kwargs['slug'])
            else:
                ctxt['comment_form'] = comment_form
        return render(request, self.template_name, self.get_context_data(**ctxt))


def places_list_by_category(request,category_slug):
    category = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    context = {'category': category}
    return render(request, 'explorer/category_list.html', context)



class PlacesList(ListView):
    model = Place
    template_name = 'explorer/places_list.html'
    context_object_name = 'places'
    paginate_by = 5
    queryset = Place.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PlaceFilter(self.request.GET,  queryset=self.get_queryset())

        return context


def places_list(request):
    page_list = Place.objects.all()
    place_filter = PlaceFilter(request.GET, queryset=page_list)
    place_list = place_filter.qs

    paginator = Paginator(place_list, 4)
    page = request.GET.get('page', 1)
    try:
        places = paginator.page(page)
    except PageNotAnInteger:
        places = paginator.page(1)
    except EmptyPage:
        places = paginator.page(paginator.num_pages )
    context = {'paginator':paginator, 'filter':place_filter, 'places':places}
    return render(request, 'explorer/places_list.html', context)


