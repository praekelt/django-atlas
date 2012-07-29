from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from atlas.models import Location


def location_list(request):
    template = "atlas/location_list.html"
    extra = {'title': _('Locations')}
    return render_to_response(template, extra, context_instance=RequestContext(request))


def location_detail(request, id):   
    location = get_object_or_404(Location, id=id)
    template = "atlas/location_detail.html"
    extra = {'title': _('Locations'), 'location': location}
    return render_to_response(template, extra, context_instance=RequestContext(request))