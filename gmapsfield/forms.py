from django.forms import widgets
from django.template import Context, loader

class GoogleMapsFormWidget(widgets.Widget):

    def __init__(self, *args, **kwargs):
        super(GoogleMapsFormWidget, self).__init__(*args, **kwargs)
        self.inner_widget = widgets.HiddenInput()

    def render(self, name, value, *args, **kwargs):
        template = loader.get_template("admin.html")
        context = Context({ "name": name, "value": value })

        return template.render(context)
