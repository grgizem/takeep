from django import forms

from apps.place.models import Place, FlagPlace


class PlaceForm(forms.ModelForm):
    """
    Place form to create new places
    """
    class Meta:
        model = Place
        exclude = ["is_approved"]


class FlagPlaceForm(forms.ModelForm):
    """
    Place form to create new places
    """
    class Meta:
        model = FlagPlace
        exclude = ["place", "is_considered"]

    def save(self, request, place, commit=True):
        instance = super(FlagPlaceForm, self).save(commit=False)
        """
        super save method
        """
        instance.place = place
        """
        save the relation to the given place
        """
        if commit:
            instance.save()
        return instance
