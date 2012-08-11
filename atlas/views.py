from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.contrib.gis.geos import fromstr
from django.contrib.gis.geoip import GeoIP

from atlas.models import Location


def set_location(request):
    if 'atlas_id' in request.COOKIES:
        val = request.COOKIES['atlas_id']
        #if 
        if val == 'no-location':
            # IP geolocate the client
            pass
        else:
            lon, lat = val.split(',')
            point = fromstr("POINT (%s %s)" % (lon, lat), srid=4326)
            request.session['location'] = None
            
    return HttpResponseBadRequest()
    