from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput


class PlanAddPlaceForm(forms.Form):
    start_date = forms.DateTimeField(widget=DateTimePickerInput())
    end_date = forms.DateTimeField(widget=DateTimePickerInput())
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)