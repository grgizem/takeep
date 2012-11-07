from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'event.views.home', name='home'),
    # url(r'^event/', include('event.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
