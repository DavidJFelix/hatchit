from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'event_manager.views.home', name='home'),
    url(r'^s/$', 'event_manager.views.my_suggestions', name='suggestions'),
    url(r'^e/$', 'event_manager.views.my_events', name='events'),
    url(r'^api/(?P<type>[a-z]{1})/$', 'event_manager.views.api_get', name='api'),
    url(r'^admin/', include(admin.site.urls)),
)
