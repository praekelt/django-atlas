from django.conf.urls.defaults import patterns, url, include

from tastypie.api import Api

from atlas.api import CountryResource, CityResource, LocationResource


'''v1_api = Api(api_name='v1')
v1_api.register(CountryResource())
v1_api.register(CityResource())
v1_api.register(LocationResource())'''


urlpatterns = patterns('',
    url(
        r'^set-location/$',
        'atlas.views.set_location',
        name='set-location'
    ),
)