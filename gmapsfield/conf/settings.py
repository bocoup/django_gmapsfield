from django.conf import settings

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEMPLATE_LOADERS = ( 
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MEDIA_ROOT = 'public'
MEDIA_URL = '/gmaps/media/'
MIDDLEWARE_CLASSES = ( 'django.middleware.common.CommonMiddleware', )
TEMPLATE_DIRS = ( 'templates', )
INSTALLED_APPS = ( 
    'django.contrib.contenttypes',
    'gmapsfield.templatetags',
)

# Alias 
STATIC_URL = settings.STATIC_URL
# Custom settings
GMAP_JQUERY = getattr(settings, 'GMAP_JQUERY', 'http://code.jquery.com/jquery-1.7.2.min.js')

GMAP_JQUERY_UI = getattr(settings, 'GMAP_JQUERY_UI', 
                         'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.min.js')

GMAP_JQUERY_UI_CSS = getattr(settings, 'GMAP_JQUERY_UI_CSS', 
                             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/themes/smoothness/jquery-ui.css')

GMAP_API = getattr(settings, 'GMAP_API', 'http://maps.google.com/maps/api/js?sensor=false')
GMAP_DEFAULT = getattr(settings, 'GMAP_DEFAULT', [-34.397, 150.644])
