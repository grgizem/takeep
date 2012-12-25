from django import forms

from apps.event.models import Event


class EventForm(forms.ModelForm):
    start_time = forms.DateField()
    end_time = forms.DateField()

    class Meta:
        model = Event
        exclude = ["host", "status"]

    def save(self, user, commit=True):
        instance = super(EventForm, self).save(commit=False)
        instance.host = user
        instance.status = "O"
        if commit:
            instance.save()
        return instance
