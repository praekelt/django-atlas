from django.conf.urls.defaults import patterns, url, include

from tastypie.api import Api

from locations.api import CountryResource, CityResource, LocationResource


v1_api = Api(api_name='v1')
v1_api.register(CountryResource())
v1_api.register(CityResource())


urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)