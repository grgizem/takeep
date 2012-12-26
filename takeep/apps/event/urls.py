from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('apps.event.views',
	url(r'^events/', 'events', name='events'),
	url(r'^event/(?P<event_id>\d+)/$', 'event', name='event'),
    url(r'^create_event/', 'create_event', name='create_event'),

    url(r'^join/(?P<event_id>\d+)/$', 'join', name='join'),

	url(r'^edit_event/(?P<event_id>\d+)/$', 'edit_event', name='edit_event'),
    url(r'^cancel_event/(?P<event_id>\d+)/$', 'cancel_event', name='cancel_event'),

    url(r'^approve/(?P<event_id>\d+)(?P<user_id>\d+)/$', 'approve', name='approve'),
    url(r'^disapprove/(?P<event_id>\d+)(?P<user_id>\d+)/$', 'disapprove', name='disapprove'),

    url(r'^report/(?P<event_id>\d+)/$', 'report', name='report'),
)
