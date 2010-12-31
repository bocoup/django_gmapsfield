django_gmapsfield
=================

Django Google Maps Field is the most robust way to customize and display a Google Maps map.

Its simple to install:

    #  python setup.py install

Simple to use:
==============

/settings.py
------------

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        ...
        'gmapsfield', # Make sure to register this
        ...
    )

/models.py
----------

    from gmapsfield.fields import GoogleMapsField
    
    from django.db import models
    from django.contrib import admin
    
    class Test(models.Model):
        map = GoogleMapsField()
    
    admin.site.register(Test)

/views.py
---------

    from demo.map.models import Test
    
    from django.template import RequestContext, loader
    from django.http import HttpResponse
    
    def index(request):
        template = loader.get_template("index.html")
    
        # Grab the first map if one exists
        test = (Test.objects.all() and Test.objects.all()[0]) or { "map": { show: "No maps defined" } }
    
        return HttpResponse(template.render(RequestContext(request, {
            "test": test
        })))

/template.html
--------------

    <!-- Required to view result in a template -->
    {% load gmap %}

    <!-- Will display the actual map -->
    {{ test.map|show }}

    <!-- Includes the necessary scripts on the page, place anywhere, but only once and do not forget! -->
    {% gmap_includes %}
