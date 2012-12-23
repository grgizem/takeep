from django.conf.urls import patterns, url, include

from api.resources import UserResource, EventResource, UserProfileResource
from api.resources import PlaceResource, ParticipantResource

from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EventResource())
v1_api.register(UserProfileResource())
v1_api.register(ParticipantResource())
v1_api.register(PlaceResource())

urlpatterns = patterns('',
    url(r'^', include(v1_api.urls)),
)
