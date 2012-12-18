from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('apps.account.urls')),
    url(r'^event/', include('apps.event_app.urls')),
    url(r'^place/', include('apps.place.urls')),
)
