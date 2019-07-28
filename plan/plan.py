from decimal import Decimal
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
import json
from explorerapp.models import Place
import datetime


class Plan(object):

    def __init__(self, request):
        """
        Initialize the plan.
        :param request:
        """
        self.request = request
        self.session = request.session
        plan = self.session.get(settings.PLAN_SESSION_ID)
        if not plan:
            # save an empty plan in session
            plan = self.session[settings.PLAN_SESSION_ID] = {}
        self.plan = plan

    def add(self, place):
        """
        Add a place do plan.
        :return:
        """
        place_id = str(place.id)
        self.plan[place_id] = {'quantity': 1, 'cost': str(place.cost),
                               }
        self.save()

    def save(self):
        # mark the session as modified to make sure it gets saved
        self.session.modified = True

    def remove(self, place):
        """
        Remove a place from the plan
        :param place:
        :return:
        """
        place_id = str(place.id)
        if place_id in self.plan:
            del self.plan[place_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the plan and get the places from the database
        :return:
        """
        place_ids = self.plan.keys()
        # get the place objects and add them to the cart
        places = Place.objects.filter(id__in=place_ids)

        plan = self.plan.copy()
        for place in places:
            plan[str(place.id)]['place'] = place

        for item in plan.values():
            item['cost'] = Decimal(item['cost'])
            item['total_cost'] = item['cost'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all places in the plan.
        :return:
        """
        return sum(item['quantity'] for item in self.plan.values())

    def get_total_price(self):
        return sum(Decimal(item['cost']) * item['quantity'] for item in self.plan.values())

    def clear(self):
        # remove plan from session
        del self.session[settings.PLAN_SESSION_ID]
        self.save()