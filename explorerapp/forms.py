from django import forms
from .models import Comment

class RatingForm(forms.Form):
    OPTIONS = [
        (1, 'Okropna Nuda!'),
        (2, 'Nieciekawe'),
        (3, 'Można obejrzeć'),
        (4, 'Ciekawe'),
        (5, 'Świetne!')
    ]
    Rating = forms.ChoiceField(widget=forms.RadioSelect, choices=OPTIONS)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')