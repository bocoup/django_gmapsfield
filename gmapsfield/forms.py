from django.forms import widgets
from django.template import Context, loader
from conf import settings

#===============================================================================
# Avoid jQuery to be loaded twice if it's there 
#===============================================================================



class GoogleMapsFormWidget(widgets.Widget):

    class Media:
        js = ('http://maps.google.com/maps/api/js?sensor=true', 
              settings.GMAP_JQUERY, 
              settings.GMAP_JQUERY_UI, 
              settings.STATIC_URL + 'admin/gmapsfield/admin.js',)

        css = {
            'all': (settings.GMAP_JQUERY_UI_CSS,),
        }

    def __init__(self, *args, **kwargs):
        super(GoogleMapsFormWidget, self).__init__(*args, **kwargs)
        self.inner_widget = widgets.HiddenInput()

    def render(self, name, value, *args, **kwargs):
        template = loader.get_template("admin.html")
        context = Context({ "name": name, "value": value })

        return template.render(context)
