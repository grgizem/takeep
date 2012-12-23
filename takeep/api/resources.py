from django.contrib.auth.models import User

from api.forms import UserForm
from api.validation import ModelFormValidation
from account.forms import UserProfileForm
from account.models import UserProfile
from event.forms import EventForm, ParticipantForm
from event.models import Event, Participant
from place.forms import PlaceForm
from place.models import Place

from tastypie import fields
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.cache import SimpleCache
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.serializers import Serializer


class UserResource(ModelResource):
    class Meta:
        # Related model of resource.
        queryset = User.objects.filter()
        # Optional but in case to be sure.
        resource_name = 'user'
        # Restrictions.
        allowed_methods = ['get', 'post', 'put']
        # Return data when created.
        always_return_data = True
        # Fields that served by system.
        fields = ['username']
        # Every mobile client will have a unique apikey inorder to have ability,
        # -- to create users for system.
        # Authentication module.
        authentication = ApiKeyAuthentication()
        # Permissions
        authorization = DjangoAuthorization()
        # System cache.
        cache = SimpleCache()
        # Support all available formats, such as xml, json, yaml.
        serializer = Serializer()
        # Fields that allowed to be filtered through.
        filtering = {
            'id': ALL,
            'username': ALL,
        }
        # Validation of data that send.
        validation = ModelFormValidation(form_class=UserForm)
        #validation = CleanedDataFormValidation(form_class=UserForm)


class UserProfileResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)

    class Meta:
        # Related model of resource.
        queryset = UserProfile.objects.all()
        # Optional but in case to be sure.
        resource_name = 'UserProfile'
        # Restrictions.
        allowed_methods = ['get', 'post', 'put']

        # Fields that served by system.
        # In this case all of them.
        # fields = [] or exclude = []
        # Fields that allowed to be filtered through.

        filtering = {
            'id': ALL,
        }
        # Return data when created.
        always_return_data = True
        # Authentication module.
        authentication = BasicAuthentication()
        # Permissions
        authorization = Authorization()
        # System cache.
        cache = SimpleCache()
        # Support all available formats.
        serializer = Serializer()
        # Validation of data that send.
        validation = ModelFormValidation(form_class=UserProfileForm)
        #validation = CleanedDataFormValidation(form_class=PlaceForm)

        def apply_authorization_limits(self, request, object_list):
            return object_list.filter(user=request.user)


class PlaceResource(ModelResource):

    class Meta:
        # Related model of resource.
        # Return list of all Places.
        queryset = Place.objects.filter()
        # Optional but in case to be sure.
        resource_name = 'place'

        # Fields that excluded by system.
        # excludes = []

        # Restrictions.
        allowed_methods = ['get', 'post']
        # Fields that allowed to be filtered through.
        filtering = {
            'id': ALL,
            'name': ALL,
        }
        # Return data when created.
        always_return_data = True
        # Authentication module.
        authentication = BasicAuthentication()
        # Permissions
        authorization = DjangoAuthorization()
        # System cache.
        cache = SimpleCache()
        # Support all available formats.
        serializer = Serializer()
        # Validation of data that send.
        validation = ModelFormValidation(form_class=PlaceForm)
        #validation = CleanedDataFormValidation(form_class=PlaceForm)


class EventResource(ModelResource):
    host = fields.ForeignKey(UserResource, 'user', full=True)
    location = fields.ForeignKey(PlaceResource, 'place', full=True)

    class Meta:
        # Related model of resource.
        queryset = Event.objects.filter(status='O').order_by("time")
        # Optional but in case to be sure.
        resource_name = 'event'

        # Fields that excluded by system.
        # Not needed for now but better to keep a template.
        # excludes = []

        # Restrictions.
        allowed_methods = ['get', 'post', 'put']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        # Fields that allowed to be filtered through.
        filtering = {
            'id': ALL,
            'user': ALL_WITH_RELATIONS,
        }
        # Authentication module.
        authentication = BasicAuthentication()
        # Permissions
        authorization = Authorization()
        # System cache.
        cache = SimpleCache()
        # Support all available formats.
        serializer = Serializer()
        # Validation of data that send.
        validation = ModelFormValidation(form_class=EventForm)
        #validation = CleanedDataFormValidation(form_class=EventForm)


class ParticipantResource(ModelResource):
    event = fields.ForeignKey(EventResource, 'event')
    guest = fields.ForeignKey(UserResource, 'user')

    class Meta:
        # Related model of resource.
        queryset = Participant.objects.filter()
        # Optional but in case to be sure.
        resource_name = 'participant'

        # Fields that excluded by system.
        # excludes = []

        # Restrictions.
        allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        # Fields that allowed to be filtered through.
        filtering = {
            'id': ALL,
        }
        # Return data when created.
        always_return_data = True
        # Authentication module.
        authentication = BasicAuthentication()
        # Permissions
        authorization = Authorization()
        # System cache..
        cache = SimpleCache()
        # Support all available formats.
        serializer = Serializer()
        # Validation of data that send.
        validation = ModelFormValidation(form_class=ParticipantForm)
        #validation = CleanedDataFormValidation(form_class=ParticipantForm)

        def obj_create(self, bundle, request=None, **kwargs):
            if self.event.is_host == request.user:
                return super(ParticipantResource, self).obj_create(
                bundle, request)
            else:
                return

        def apply_authorization_limits(self, request, object_list):
            if self.event.is_host == request.user:
                return object_list.filter()
            else:
                return
