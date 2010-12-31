from gmapsfield.fields import GoogleMapsField

from django.db import models
from django.contrib import admin

class Test(models.Model):
    map = GoogleMapsField()

class TestAdmin(admin.ModelAdmin): pass

try:
    admin.site.register(Test, TestAdmin)
except: pass
