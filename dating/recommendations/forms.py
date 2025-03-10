from django import forms


class CreateRecommendationForm(forms.Form):
    """Form to get keep target id from POST request from js"""
    target_id = forms.IntegerField()
