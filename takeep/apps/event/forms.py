from django import forms

from apps.event.models import Event, EventReport


class EventForm(forms.ModelForm):
    start_time = forms.DateField()
    end_time = forms.DateField()

    class Meta:
        model = Event
        exclude = ["host", "status"]

    def save(self, request, commit=True):
        instance = super(EventForm, self).save(commit=False)
        user = request.user
        instance.host = user
        instance.status = "O"
        if commit:
            instance.save()
        return instance


class EventReportForm(forms.ModelForm):

    class Meta:
        model = EventReport
        exclude = ["user", "is_considered"]

    def save(self, user, event, commit=True):
        instance = super(EventReportForm, self).save(commit=False)
        instance.user = user
        instance.event = event
        if commit:
            instance.save()
        return instance
