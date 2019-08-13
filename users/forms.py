from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.EmailInput())
    confirm_email=forms.EmailField(widget=forms.EmailInput())
    bio = forms.Textarea()

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

    def clean(self):
        cleaned_data = super(UserProfileForm, self).clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        bio = cleaned_data.get("bio")

        if email != confirm_email:
            raise forms.ValidationError(
                "Emails must match!"
            )

        if len(bio) < 10:
            raise forms.ValidationError(
                "Bio must be 10 characters or longer!"
            )