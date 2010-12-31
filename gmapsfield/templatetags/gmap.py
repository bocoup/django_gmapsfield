from django import template
register = template.Library()

def __init__():
    pass

@register.filter()
def show(value):
    t = template.loader.get_template("public.html")
    return t.render(template.Context({
        "obj": str(value)
    }))

# Include scripts
@register.tag()
def gmap_includes(parser, token):
    return IncludesNode()

class IncludesNode(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        t = template.loader.get_template("includes.html")
        return t.render(template.Context())

# Some point in the future it would be cool to show a map on demand with the config object
@register.tag()
def show_map(parser, token):
    return MapNode()

class MapNode(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        pass
