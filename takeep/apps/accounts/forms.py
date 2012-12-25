import datetime

from django import forms
from django.forms.extras.widgets import SelectDateWidget

from apps.accounts.models import UserProfile


BIRTHDATE_YEARS = range(datetime.datetime.now().year,
                        datetime.datetime.now().year - 100,
                        - 1)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('gender', 'birthdate', 'address', 'photo',
            'location', 'bio')
        widgets = {
            'birthdate': SelectDateWidget(years=BIRTHDATE_YEARS),
        }