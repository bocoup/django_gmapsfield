django\_gmapsfield
==================

Django Google Maps Field is a robust way to customize and display a Google Map
in Django, and use it as a UI for selecting/displaying location information in
the Django admin.

Developed By Tim Branyen, Bocoup LLC for Community Planit on behalf of
Engagement Game Labs

Features
--------
This project is currently under development and has not yet reached a beta
phase.  It should be treated and used as alpha within development environments.
Features will be added as the host project work continues.

So far several features exist:
* Custom admin site field.
  - Specify a JSON-formatted defaults
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

``` bash
python setup.py install
```

Or

``` bash
easy_install django_gmapsfield
```

/settings.py
------------

``` python
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    ...
    'gmapsfield', # Make sure to register this
    ...
)
```

/urls.py
--------

``` python
# Note: the following approach is non-standand, while it remains functional
# there are many disadvantages that django 1.3 static file handling will
# correct.

# Add this to serve correct admin js
(r'^admin/gmapsfield/admin/(?P<file>.*)$', 'gmapsfield.views.serve'),

# Optionally symlink this folder to your admin media path
```

/models.py
----------

``` python
from gmapsfield.fields import GoogleMapsField

from django.db import models
from django.contrib import admin

class Test(models.Model):
    map = GoogleMapsField()

    # Can optionally specify defaults via JSON string
    #map2 = GoogleMapsField(default="{ coordinates: [-40, 50], zoom: 10, size: [400, 200] }")

admin.site.register(Test)
```

/views.py
---------

``` python
from demo.map.models import Test

from django.template import RequestContext, loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template("index.html")

    # Grab the first map if one exists - for purposes of example 
    test = (Test.objects.all() and Test.objects.all()[0]) or { "map": { show: "No maps defined" } }

    return HttpResponse(template.render(RequestContext(request, {
        "test": test
    })))
```

/template.html
--------------

``` html
<!-- Required to view result in a template -->
{% load gmap %}

<!-- Will display the actual map -->
{{ test.map|show }}

<!-- Includes the necessary scripts on the page, place anywhere, but only once and do not forget! -->
{% gmap_includes %}
```

Development Notes:
------------------
* 1/04/11: Updated path to serve admin.js to be called admin instead of public.
* 1/19/11: Two new settings added GMAP_JQUERY and GMAP_API which are string urls pointing to the respective resources.  Fixed bug with dumpdata.  Can now set global defaults in models via JSON.
