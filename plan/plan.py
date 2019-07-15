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
        self.session = request.session
        plan = self.session.get(settings.PLAN_SESSION_ID)
        if not plan:
            # save an empty plan in session
            plan = self.session[settings.PLAN_SESSION_ID] = {}
        self.plan = plan

    def add(self, place, start_date, end_date, update_date=False):
        """
        Add a place do plan.
        :return:
        """
        start_date = json.dumps(start_date, cls=DjangoJSONEncoder)
        end_date = json.dumps(end_date, cls=DjangoJSONEncoder)
        place_id = str(place.id)
        if place_id not in self.plan:
            self.plan[place_id] = {'quantity': 1, 'cost': str(place.cost),
                                   'start_date': start_date, 'end_date': end_date}
        if update_date:
            self.plan[place_id]['start_date'] = start_date
            self.plan[place_id]['end_date'] = end_date
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
            item['start_date'] = datetime.datetime.strptime((item['start_date']),'"%Y-%m-%dT%H:%M:%SZ"')
            item['end_date'] = datetime.datetime.strptime((item['end_date']),'"%Y-%m-%dT%H:%M:%SZ"')
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