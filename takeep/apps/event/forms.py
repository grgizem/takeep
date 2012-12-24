from django.forms import ModelForm

from apps.event.models import Event


class EventForm(ModelForm):
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
