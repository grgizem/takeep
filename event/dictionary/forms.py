import datetime
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from dictionary.models import Events, Participant

class NewUserCreationForm(UserCreationForm):
	email = forms.EmailField(required = True)
	
	class Meta:
		model = User
		fields = ("username","email","password")

	def save(self):
        	user = User.objects.create_user(self.cleaned_data["username"],self.cleaned_data["email"],self.cleaned_data["password"])
		user.is_active=False
		user.save()
		
class EventForm(forms.ModelForm):
    class Meta:
    	model = Event
    	exclude = ["host", "location", "is_private", "tags", "start_time", "end_time"]

    def save(self, request):
        event = Event(title = self.cleaned_data["Title"], details = self.cleaned_data["Details"], host = request.user)
        event.save()
    
    def saveAs(self, request, event):
	event.title = self.cleaned_data["Title"]
	event.details = self.cleaned_data["Details"]
	event.save()


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