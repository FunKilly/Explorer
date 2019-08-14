from django import forms
from .models import Event


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date']
        widgets = {'start_date': forms.SelectDateWidget(),
                   'end_date': forms.SelectDateWidget()}

