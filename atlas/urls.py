from django.conf.urls import patterns, url, include

from tastypie.api import Api

from atlas.api import CountryResource, RegionResource, CityResource
from atlas import views


v1_api = Api(api_name='v1')
v1_api.register(CountryResource())
v1_api.register(RegionResource())
v1_api.register(CityResource())


urlpatterns = patterns('',
    (
        r'^atlas-api/',
        include(v1_api.urls)
    ),
    url(
        r'^set-location/$',
        views.set_location,
        name='set-location'
    ),
    url(r'^select-location/$',
        views.select_location,
        name='select-location',
    ),
)
