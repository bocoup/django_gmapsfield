from django.conf.urls.defaults import *
from demo.map import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^demo/', include('demo.foo.urls')),
    (r'^$', views.index),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Add this to serve correct admin js
    (r'^admin/gmapsfield/public/(?P<file>.*)$', 'gmapsfield.views.serve'),
)
