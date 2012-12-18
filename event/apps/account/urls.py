from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('apps.account.views',
    url(r'^profile/', 'profile', name='profile'),
    url(r'^edit_profile/', 'edit_profile', name='edit_profile'),
    url(r'^my_events/', 'my_events', name='my_events'),
    url(r'^my_event/', 'my_event', name='my_event'),

    url(r'^login/', 'login', name='login'),
    url(r'^register/', 'register', name='register'),
    url(r'^logout/', 'logout', name='logout'),
)
