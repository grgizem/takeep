from django import forms

from apps.event.models import Event, EventReport


class EventForm(forms.ModelForm):
    """
    Form model of the event,
    use for create and edit an event
    """
    start_time = forms.DateField()
    end_time = forms.DateField()

    class Meta:
        model = Event
        """
        host and status fields do'nt assign by the form request
        status:
        - save as OPEN when the new object created
        - remain same when the object updated
        """
        exclude = ["host", "status"]

    def save(self, request, commit=True):
        instance = super(EventForm, self).save(commit=False)
        """
        super save method
        """
        user = request.user
        instance.host = user
        """
        requested user will be host of the event
        """
        if commit:
            instance.save()
        return instance


class EventReportForm(forms.ModelForm):
    """
    Form to report about an event,
    - can be created by users as this form
    - can be check and update from admin page by superusers
    """
    reason = forms.CharField(widget=forms.Textarea(attrs={'rows': '10'}))

    class Meta:
        model = EventReport
        exclude = ["user", "event", "is_considered"]
        """
        user, event and is_considered fields don't assign by the form request
        is_considered:
        - save as False when the new object created
        """

    def save(self, user, event, commit=True):
        instance = super(EventReportForm, self).save(commit=False)
        """
        super save method
        """
        instance.user = user
        """
        requested user will be the reporter
        """
        instance.event = event
        """
        report save with the related to an event
        """
        if commit:
            instance.save()
        return instance
