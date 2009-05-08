
copyrev: 0e7fd61dc82fa816c60cac8045bb57adb72f8870
copy: test_project/urls.py

from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'api/', include('test_project.apps.testapp.urls'))
)
