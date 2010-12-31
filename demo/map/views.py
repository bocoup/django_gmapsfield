from demo.map.models import Test

from django.template import RequestContext, loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template("index.html")

    test = (Test.objects.all() and Test.objects.all()[0]) or { "map": { show: "No maps defined" } }

    return HttpResponse(template.render(RequestContext(request, {
        "test": test
    })))
