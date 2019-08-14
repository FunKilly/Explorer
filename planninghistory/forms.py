from django import forms
from .models import Event
from datetime import date

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date']
        widgets = {'start_date': forms.SelectDateWidget(),
                   'end_date': forms.SelectDateWidget()}

    def clean(self):
        cleaned_data = super(EventCreateForm, self).clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date > end_date:
            raise forms.ValidationError(
                "Data początkowa nie może być większa od daty końcowej!")
        elif start_date < date.today():
            raise forms.ValidationError(
                "Data początkowa nie może być mniejsza od daty dzisiejszej!")
        return cleaned_data