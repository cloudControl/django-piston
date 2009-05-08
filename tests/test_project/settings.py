
copyrev: 8a424c4ac3d6f7fca51a1e11adc43d25f4fdedd2
copy: test_project/settings.py

import os
DEBUG = True
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/piston.db'
INSTALLED_APPS = (
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'piston',
    'test_project.apps.testapp',
)
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)
ROOT_URLCONF = 'test_project.urls'
