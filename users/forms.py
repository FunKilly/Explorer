from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Profile
        fields = [
            'avatar',
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'bio',
            'city',
            'state',
            'country',
        ]
        labels = {
            'first_name': _('Imię'),
            'last_name': _('Nazwisko'),
            'birth_date': _('Data urodzenia'),
            'city': _('Miasto'),
            'state': _('Województwo'),
            'country': _('Kraj')}

    def clean(self):
        cleaned_data = super(UserProfileForm, self).clean()
        bio = cleaned_data.get("bio")


        if len(bio) < 10:
            raise forms.ValidationError(
                "Bio must be 10 characters or longer!"
            )