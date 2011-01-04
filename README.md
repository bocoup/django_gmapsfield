django_gmapsfield
=================

Django Google Maps Field is a robust way to customize and display a Google Map in Django, and use it as a UI for selecting/displaying location information in the Django admin.

Developed By Tim Branyen, Bocoup LLC for Community Planit on behalf of Engagement Game Labs

Features
--------
This project is currently under development and has not yet reached a beta phase.  It should be treated and used as alpha within development environments.  Features will be added
as the host project work continues.

So far several features exist:
* Custom admin site field.
* Custom public template filter
* Customizable properties:
    - Zoom
    - Width/Height
    - Center coordinates

Simple to use:
==============

Installation
-------------
Its simple to install - use this command to upgrade as well:
    #  python setup.py install
Or
    # easy_install django_gmapsfield

/settings.py
------------

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        ...
        'gmapsfield', # Make sure to register this
        ...
    )

/urls.py
--------

    # Add this to serve correct admin js
    (r'^admin/gmapsfield/public/(?P<file>.*)$', 'gmapsfield.views.serve'),

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
