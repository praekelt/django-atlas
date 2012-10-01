from functools import wraps

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.contrib.gis.geos import fromstr
from django.core.urlresolvers import reverse, resolve
from django.template import RequestContext

from atlas.models import Location
from atlas.utils import get_city
from atlas.forms import SelectLocationForm

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
                position = None
                if location and location != 'no-location':
                    position = fromstr("POINT (%s %s)" % tuple(location.split('+')), srid=4326)
                if ip and not position:
                    '''if position:
                        city = get_city(ip=ip, position=position)
                    else:'''
                    city = get_city(ip=ip)
                elif position:
                    city = get_city(position=position)
                
                if city:
                    request.session['location'] = {'city': city, 'position': position}
                    return func(request, *args, **kwargs)

                origin = getattr(resolve(request.get_full_path()), 'url_name', None)
                return HttpResponseRedirect("%s%s" % (reverse('select-location'), \
                    ('?view=%s' % origin) if origin else ''))

        return wraps(func)(inner_decorator)

    return decorator


@location_required(override_old=True)
def set_location(request):
    return HttpResponse(str(request.session['location']['city']))


def select_location(request):
    if request.method == 'POST':
        form = SelectLocationForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            redirect_to = form.cleaned_data['origin']
            if redirect_to != '/':
                redirect_to = reverse(redirect_to)
            return HttpResponseRedirect(redirect_to)
        
    else:
        form = SelectLocationForm(request=request)
    
    extra = {'form': form}
    return render_to_response("atlas/select_location.html", extra, context_instance=RequestContext(request))
    