DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEMPLATE_LOADERS = ( 
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MEDIA_ROOT = "public"
MEDIA_URL = "/gmaps/media/"
MIDDLEWARE_CLASSES = ( 'django.middleware.common.CommonMiddleware', )
TEMPLATE_DIRS = ( 'templates', )
INSTALLED_APPS = ( 
    'django.contrib.contenttypes',
    'gmapsfield.templatetags',
)
