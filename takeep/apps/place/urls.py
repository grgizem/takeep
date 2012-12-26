from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('apps.place.views',
    url(r'^places/', 'places', name='places'),
    url(r'^place/(?P<place_id>\d+)/$', 'place', name='place'),
    url(r'^create_place/', 'create_place', name='create_place'),

    url(r'^flag/(?P<place_id>\d+)/$', 'flag', name='flag'),
)
