from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('apps.accounts.urls')),
    url(r'^event/', include('apps.event.urls')),
    url(r'^place/', include('apps.place.urls')),
)
