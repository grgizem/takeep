from django import forms

from apps.event.models import Event


class EventForm(forms.ModelForm):
    start_time = forms.DateField()
    end_time = forms.DateField(widget=forms.DateInput(format = '%d.%m.%Y'), input_formats=('%d.%m.%Y',))

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
