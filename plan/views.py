from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from explorerapp.models import Place
from .plan import Plan
from .forms import PlanAddPlaceForm


@require_POST
def plan_add(request, place_id):
    plan = Plan(request)
    place = get_object_or_404(Place, id=place_id)
    plan_form = PlanAddPlaceForm(request.POST)
    if plan_form.is_valid():
        cd = plan_form.cleaned_data
        plan.add(place=place)
    else:
        return render(request, 'explorer/place_detail.html', {'place': place, 'plan_form': plan_form})
    return redirect('plan:plan_detail')


def plan_remove(request, place_id):
    plan = Plan(request)
    place = get_object_or_404(Place, id=place_id)
    plan.remove(place)
    return redirect('plan:plan_detail')


def plan_detail(request):
    plan = Plan(request)
    context = {'plan': plan}
    return render(request, 'plan/detail.html', context)
