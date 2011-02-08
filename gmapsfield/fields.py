from types import FunctionType
from django.utils import simplejson
from django.db import models
from forms import GoogleMapsFormWidget
from django.template import Context, loader

# Convert obj to string
def filter_object(obj):
    return dict((name, getattr(obj, name)) for name in dir(obj) if not name.startswith('__'))

class GoogleMaps(object):
    coordinates = None
    size = None
    zoom = None
    markers = None

    def __str__(self):
        return simplejson.dumps(filter_object(self))
 
class GoogleMapsField(models.Field):
    ''' Google Maps Representation '''
    description = 'A Google Maps representation'
    __metaclass__ = models.SubfieldBase 
    widget = GoogleMapsFormWidget

    # Use TextField logic
    def get_internal_type(self):
        return 'TextField'

    # Convert to python class
    def to_python(self, value):
        # If value is already a GoogleMaps, return
        if isinstance(value, GoogleMaps):
            return value

        # Init new GoogleMaps class
        googlemap = GoogleMaps()

        # Load in JSON data
        try:
            mapdata = simplejson.loads(value)

            # No data
            if len(mapdata.keys()) == 0:
                return None

            # Coordinates
            if mapdata.get('coordinates'):
                googlemap.coordinates = mapdata.get('coordinates')
            # Size
            if mapdata.get('size'):
                googlemap.size = mapdata.get('size')
            # Zoom
            if mapdata.get('zoom'):
                googlemap.zoom = mapdata.get('zoom')
            # Markers
            if mapdata.get('markers'):
                googlemap.markers = mapdata.get('markers')

        except:
            googlemap = ''

        return googlemap

    # Reverse of to_python
    def get_prep_value(self, obj):
        try:
            return simplejson.dumps(filter_object(obj))
        except:
            return ""

    # Custom form field
    def formfield(self, **kwargs):
        # This is a standard way to set up some defaults
        # while letting the caller override them.
        defaults = { 'widget': GoogleMapsFormWidget }
        defaults.update(kwargs)
        return super(GoogleMapsField, self).formfield(**defaults)

    # Default unicode function
    def __unicode__(self):
        return ''
        return simplejson.dumps(filter_object(obj))
