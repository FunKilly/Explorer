from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import City, Category, Place, Comment
from .forms import RatingForm, CommentForm

def index(request):
    # Strona glowna.
    places = Place.objects.all()[:10]
    context = {'places': places}
    return render(request, 'explorer/index.html', context)


'''def place_detail(request, id, slug):
    place = get_object_or_404(Place, id=id, slug=slug)
    if request.method == 'POST' and form.is_valid():
        form = RatingForm(request.POST)
        if form.is_valid():
            place.sum_of_rating += int(form.cleaned_data['Rating'])
            place.num_of_ratings += 1
            place.save()
            return redirect('explorer:place_detail', id=id, slug=slug)
    if request.method == 'POST':
    else:
        form = RatingForm

    context = {'place': place,'form':form}
    return render(request, 'explorer/place_detail.html', context)'''

class PlaceView(View):
    template_name = 'explorer/place_detail.html'

    def place_detail(self):
        place = get_object_or_404(Place, id=self.kwargs['id'], slug=self.kwargs['slug'])
        return place


    def comments_get(self):
        place = get_object_or_404(Place, id=self.kwargs['id'], slug=self.kwargs['slug'])
        comments = place.comments.filter(active=True)
        return comments


    def get_context_data(self,**kwargs):
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


def places_list(request):
    object_list = Place.objects.all()
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        places = paginator.page(page)
    except PageNotAnInteger:
        places = paginator.page(1)
    except EmptyPage:
        places = paginator.plage(paginator.num_pages)

    context = {'places': places,'page':page}
    return render(request, 'explorer/places_list.html', context)


