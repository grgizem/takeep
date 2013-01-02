import datetime

from django import forms
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget

from apps.accounts.models import UserProfile


BIRTHDATE_YEARS = range(datetime.datetime.now().year,
                        datetime.datetime.now().year - 100,
                        - 1)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ('gender', 'birthdate', 'address', 'photo',
            'location', 'bio')
        widgets = {
            'birthdate': SelectDateWidget(years=BIRTHDATE_YEARS),
        }
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.fields["gender"].required = True
        self.fields["birthdate"].required = True
        self.fields["bio"].required = True

    def save(self):
        super(UserProfileForm, self).save()
        self.instance.user.gender = self.cleaned_data.get('gender')
        self.instance.user.birthdate = self.cleaned_data.get('birthdate')
        self.instance.user.bio = self.cleaned_data.get('bio')
        self.instance.user.save()