
copyrev: 1d4cf18af95f536273d0e53a608a36488a64cb78
copy: test_project/apps/testapp/urls.py

from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication

from test_project.apps.testapp.handlers import EntryHandler

auth = HttpBasicAuthentication(realm='TestApplication')

entries = Resource(handler=EntryHandler, authentication=auth)

urlpatterns = patterns('',
    url(r'^entries/$', entries),
    url(r'^entries/(?P<pk>.+)/$', entries),
    url(r'^entries\.(?P<emitter_format>.+)', entries),
    url(r'^entry-(?P<pk>.+)\.(?P<emitter_format>.+)', entries),
)


