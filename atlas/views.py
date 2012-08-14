from functools import wraps

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.contrib.gis.geos import fromstr
from django.core.urlresolvers import reverse
from django.template import RequestContext

from atlas.models import Location
from atlas.utils import get_city


'''
This decorator tries to geolocate the client and adds the location
to the session data. If the client cannot be geolocated it redirects
to a 'select-location' page.
'''
def location_required(override_old=False):
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):
            if 'location' in request.session and not override_old:
                return func(request, *args, **kwargs)
            else:
                ip = request.META['REMOTE_ADDR'] if 'REMOTE_ADDR' \
                    in request.META else None
                location = request.COOKIES['atlas_id'] if 'atlas_id' \
                    in request.COOKIES else None

                city = None
                position = location
                if ip:
                    city = get_city(ip=ip)
                if location and location != 'no-location':
                    lon, lat = location.split(',')
                    position = fromstr("POINT (%s %s)" % (lon, lat), srid=4326)
                    if not city:
                        city = get_city(position=position)
                
                if city:
                    request.session['location'] = {'city': city, 'position': position}
                    return func(request, *args, **kwargs)

                return HttpResponseRedirect(reverse('select-location'))

        return wraps(func)(inner_decorator)

    return decorator


@location_required(override_old=True)
def set_location(request):
    return HttpResponse(str(request.session['location']['city']))


def select_location(request):
    return render_to_response("atlas/select_location.html", context_instance=RequestContext(request))
    