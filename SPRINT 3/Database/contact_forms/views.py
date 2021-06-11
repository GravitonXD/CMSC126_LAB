from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^contact_form/create/$', 'dj10.views.contact_form'),
    url(r'^admin/', include(admin.site.urls)),
)