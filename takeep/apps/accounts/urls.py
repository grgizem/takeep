from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('apps.accounts.views',
    url(r'^profile/', 'profile', name='profile'),
    url(r'^edit_profile/', 'edit_profile', name='edit_profile'),
    url(r'^my_events/', 'my_events', name='my_events'),
    url(r'^my_event/(?P<event_id>\d+)/$', 'my_event', name='my_event'),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name' : 'accounts/login.html'}, name='login'),
    # to logout
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        name="logout"),

    # to change the password for logged-in user
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'accounts/password_change.html'},
        name='password_change'),
    url(r'^parola-degistirildi/$',
        'django.contrib.auth.views.password_change_done',
        {'template_name': 'accounts/password_change_done.html'},
        name='password_change_done'),

    # to reset the password for anonymous user
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset',
        name='password_reset'),
    url(r'^password_reset_done/$',
        'django.contrib.auth.views.password_reset_done',
        name='password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^password_reset_complete/$',
        'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),
)
