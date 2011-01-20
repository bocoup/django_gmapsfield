from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Context
from gmapsfield.conf import settings

def serve(request, file):
    if request.user.is_authenticated():
        t = loader.get_template('admin/'+ file)
        return HttpResponse(t.render(Context({
            "settings": settings
        })))
    else:
        return HttpResponse(status=403)
