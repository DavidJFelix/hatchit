from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #/ Homepage and hype page
    url(r'^$', 'event_manager.views.home', name='home'),
    
    #/suggestions/ to see pending suggestions and suggestion development
    url(r'^suggestions/$', 'event_manager.views.pending_suggestions', name='suggestions'),
    #/suggestions/add to add new suggestion
    url(r'^suggestion/add/$', 'event_manager.views.add_suggestion', name='add_suggestion'),
    #/suggestion/<suggestion>/ to view one suggestion
    #/suggestion/<suggestion>/delete/ to delete a suggestion
    #/suggestion/<suggestion>/like/ to like a suggestion
    #/suggestion/<suggestion>/dislike/ to dislike a suggestion
    #/suggestion/<suggestion>/maybe/ to mark a suggestion as indifferent
    #/me/suggestions/ to see your posted suggestions
    url(r'^me/suggestions/$', 'event_manager.views.my_suggestions', name='my_suggestions'),
    #/me/suggestions/liked/ to see your liked suggestions
    #/me/suggestions/disliked/ to see your disliked suggestions
    #/me/suggestions/maybe/ to see your maybe suggestions
    #/user/<username>/suggestions/ to see posted suggestions
    #/user/<username>/liked/ to see liked suggestions
    #/user/<username>/disliked/ to see disliked suggestions
    #/user/<username>/maybe/ to see indifferent suggestions
    
    #/events/ to see pending events and event development
    url(r'^events/$', 'event_manager.views.my_events', name='events'),
    #/events/add/ to form an event from a suggestion
    #/events/<event>/ to view one event
    #/events/<event>/accept/ to rsvp yes
    #/events/<event>/reject/ to rsvp no
    #/events/<event>/taccept/ to tentative yes rsvp
    #/events/<event>/treject/ to tentative no rsvp
    #/me/events/ to see all of your events
    #/me/events/upcoming/ to see all of your upcoming and current events
    #/me/events/past/ to see your past events
    #/me/events/accpeted/ to see your accepted events
    #/me/events/rejected/ to see your rejected events
    #/me/events/tentative/ to see your tentative events
    #/me/events/taccepted/ to see your tentatve yes events
    #/me/events/trejected/ to see your tentative no events
    #/user/<username>/events/ to view all events
    #/user/<username>/events/upcoming/ to view upcoming and current events
    #/user/<username>/events/past/ to view past events
    #/user/<username>/events/accepted/ to view accpeted events
    #/user/<username>/events/rejected/ to view rejected events
    #/user/<username>/events/tentative/ to view tentative events
    #/user/<username>/events/taccepted/ to view tentative yes events
    #/user/<username>/events/trejected/ to view tentative no events
    
    #/login/ to sign in to the application
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    #/logout/ to sign out of the application
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'login.html'}),
    #/me/ to see information about yourself (your profile?)
    
    #TODO: Add shortcuts
    
    #TODO: Add API get urls and post shortcuts
    
    #FIXME: remove admin pannel in production
    url(r'^admin/', include(admin.site.urls)),
)
