
copyrev: 86219b569b2b1e799d0c69a907021e856115d51a
copy: test_project/apps/testapp/models.py

from django.db import models

class TestModel(models.Model):
    test1 = models.CharField(max_length=1, blank=True, null=True)
    test2 = models.CharField(max_length=1, blank=True, null=True)
    pass
