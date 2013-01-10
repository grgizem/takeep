from django import forms
from django.contrib.auth.models import User

from apps.event.models import Participant


class UserForm(forms.ModelForm):
    class Meta:
        model = User


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
