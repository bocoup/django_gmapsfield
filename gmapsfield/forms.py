from django.forms import widgets
from django.template import Context, loader
from django.conf import settings

class GoogleMapsFormWidget(widgets.Widget):

    class Media:
        js = ('http://maps.google.com/maps/api/js?sensor=false', 'http://code.jquery.com/jquery.min.js', 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.min.js', '/admin/gmapsfield/admin/admin.js',)
        css = {
            'all': ('http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/themes/smoothness/jquery-ui.css',),
        }

    def __init__(self, *args, **kwargs):
        super(GoogleMapsFormWidget, self).__init__(*args, **kwargs)
        self.inner_widget = widgets.HiddenInput()

    def render(self, name, value, *args, **kwargs):
        template = loader.get_template("admin.html")
        context = Context({ "name": name, "value": value })

        return template.render(context)
