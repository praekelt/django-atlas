from functools import wraps

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse, resolve
from django.views.decorators.csrf import csrf_exempt

from atlas.utils import locate
from atlas.forms import SelectLocationForm


def location_required(func=None, override_old=False):
    '''
    This decorator tries to geolocate the client and adds the location
    to the session data. If the client cannot be geolocated it redirects
    to a 'select-location' page.
    '''
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):
            if 'location' in request.session and not override_old:
                return func(request, *args, **kwargs)
            else:
                locate(request)
                if 'location' in request.session:
                    return func(request, *args, **kwargs)

                origin = getattr(resolve(request.get_full_path()), 'url_name', None)
                return HttpResponseRedirect("%s%s" % (reverse('select-location'),
                                            ('?view=%s' % origin) if origin else ''))

        return wraps(func)(inner_decorator)

    if func:
        return decorator(func)
    return decorator


@csrf_exempt
def set_location(request):
    # force the location to be overridden
    if 'location' in request.session:
        del request.session['location']
    locate(request)

    if 'location' in request.session:
        return HttpResponse(str(request.session['location']['city']))
    if 'REMOTE_ADDR' in request.META:
        if 'atlas_id' in request.COOKIES:
            return HttpResponseBadRequest('Client cannot be located using IP %s and location %s' %
                                          (request.META['REMOTE_ADDR'], request.COOKIES['atlas_id']))
        return HttpResponseBadRequest('Client cannot be located using IP %s' %
                                      request.META['REMOTE_ADDR'])
    elif 'atlas_id' in request.COOKIES:
        return HttpResponseBadRequest('Client cannot be located using location %s' %
                                      request.COOKIES['atlas_id'])
    return HttpResponseBadRequest('Client cannot be located without IP or location cookie')


def select_location(request, form_class=SelectLocationForm):
    if request.method == 'POST':
        form = form_class(request.POST, request=request)
        if form.is_valid():
            form.save()
            redirect_to = form.cleaned_data['origin']
            if redirect_to != '/':
                redirect_to = reverse(redirect_to)
            return HttpResponseRedirect(redirect_to)

    else:
        form = form_class(request=request)

    extra = {'form': form}
    return render_to_response("atlas/select_location.html", extra, context_instance=RequestContext(request))
