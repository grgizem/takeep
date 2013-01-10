from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('apps.accounts.urls')),
    url(r'^event/', include('apps.event.urls')),
    url(r'^place/', include('apps.place.urls')),
    url(r'^api/', include('api.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),

)

# static files serve settings for testing server
#urlpatterns += patterns('',
#        (r'^static/(?P<path>.*)$',
#    'django.views.static.serve', {'document_root' : settings.STATIC_ROOT}))


# static files (images, css, javascript, etc.)
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT}))
