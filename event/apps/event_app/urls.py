from django.conf.urls.defaults import patterns, url
from django.conf.urls import patterns, include, url
from event_app.views import logout, home
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
)