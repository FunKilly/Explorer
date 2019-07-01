from django import forms


class RatingForm(forms.Form):
    OPTIONS = [
        (1, 'Okropna Nuda!'),
        (2, 'Nieciekawe'),
        (3, 'Można obejrzeć'),
        (4, 'Ciekawe'),
        (5, 'Świetne!')
    ]
    Rating = forms.ChoiceField(widget=forms.RadioSelect, choices=OPTIONS)