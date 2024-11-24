from django import forms

from accounts.models import Interest, DatingUser


class FilterMembersForm(forms.Form):
    interests = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'form-check-input'}),
        choices={interest.name: interest
                 for interest in Interest.objects.all()}
    )
    gender = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(
            attrs={'class': 'form-check-input'}),
        choices=DatingUser.Gender
    )
    min_age = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices={value: value
                 for value in range(18, 99)}
    )
    max_age = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices={value: value
                 for value in range(19, 100)}
    )
    city = forms.MultipleChoiceField(
        required=False,
        widget=forms.SelectMultiple,
        choices={city: city
                 for city in DatingUser.objects\
                     .values_list('city', flat=True)
                 if city is not None}
    )
