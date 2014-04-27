from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'event_manager.views.home', name='home'),
    url(r'^s/$', 'event_manager.views.my_suggestions', name='suggestions'),
    url(r'^e/$', 'event_manager.views.my_events', name='events'),
    url(r'^ejson/$', 'event_manager.views.my_events_json', name='eventjson'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'template_name': 'login.html'}),
    url(r'^event/add/', 'event_manager.views.api.new', name='add'),
    url(r'^api/(?P<type>[a-z]{1})/$', 'event_manager.views.api_get', name='api'),
)
