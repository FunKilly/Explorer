from django.shortcuts import render
from django.views.generic import ListView
from .models import Place, Event
from .forms import EventCreateForm
from plan.plan import Plan


def event_create(request):
    plan = Plan(request)
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            event = form.save()
            for place in plan:
                Place.objects.create(event=event,
                                     place=place['place'],
                                     price=place['cost'],
                                     quantity=place['quantity'])
            # clearing the plan
            plan.clear()
            context = {'event': event}
            return render(request, 'planninghistory/event/created.html', context)
    else:
        form = EventCreateForm()
        context = {'plan': plan, 'form': form}
        return render(request, 'planninghistory/event/create.html', context)


class EventHistory(ListView):
    template_name = 'event_list.html'
    queryset = Event.objects.all()
    context_object_name = 'events'
    paginate_by = 3
    ordering = ['-created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['places'] = Place.objects.all()
        return context