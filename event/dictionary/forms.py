mport datetime
from django import forms
from dictionary.models import Events, Participant
from ajax_select.fields import AutoCompleteField

class EventForm(forms.ModelForm):
    class Meta:
    	model = Event
    	exclude = ["host", "location", "is_private", "tags", "start_time", "end_time"]

    def save(self, request):
        event = Event(title = self.cleaned_data["Title"])
        event = Event(details = self.cleaned_data["Details"])
        event.save()
        return event
    
    def saveAs(self, request, event):
	event.title = self.cleaned_data["Title"]
	event.details = self.cleaned_data["Details"]
	event.save()
	return event

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        exclude = ["guest", "is_approved"]

    def save(self, request):
        participant = Participant(event = self.cleaned_data["Event"], guest = request.user)
        participant.save()
        return participant

    def saveAs(self, request, participant):
        participant.event = self.cleaned_data["Event"]
        participant.save()
        return participant


class SearchForm(forms.Form):

    query = AutoCompleteField(
            'event',
            required=True,
            attrs={'size': 100})