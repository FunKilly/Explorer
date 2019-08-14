from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput


class PlanAddPlaceForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class EventAdd(forms.Form):
    start_date = forms.DateTimeField(widget=DateTimePickerInput(), initial="Data rozpoczęcia")
    end_date = forms.DateTimeField(widget=DateTimePickerInput(), required=False)
