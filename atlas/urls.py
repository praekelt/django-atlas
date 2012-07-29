from django.conf.urls.defaults import patterns, url, include

from tastypie.api import Api

from atlas.api import CountryResource, CityResource, LocationResource


v1_api = Api(api_name='v1')
v1_api.register(CountryResource())
v1_api.register(CityResource())
v1_api.register(LocationResource())


urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    url(
        r'^$',
        'atlas.views.location_list',
        name='location-list'
    ),
    url(
        r'^(?P<id>\d+)/$',
        'atlas.views.location_detail',
        name='location-detail'
    ),
)