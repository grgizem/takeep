from django import forms

from apps.place.models import Place


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        exclude = ["is_approved"]
