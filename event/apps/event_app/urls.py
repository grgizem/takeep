from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('apps.event_app.views',
	url(r'^events/', 'events', name='events'),
	url(r'^event/', 'event', name='event'),
	url(r'^edit_event/', 'edit_event', name='edit_event'),
	url(r'^create_event/', 'create_event', name='create_event'),
)
