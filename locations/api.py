from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields

from locations.models import Country, City, Location


class CountryResource(ModelResource):
    
    class Meta:
        queryset = Country.objects.all()
        resource_name = "country"
        excludes = ['border']
        allowed_methods = ["get"]
        filtering = {
            'country_code': ('exact', ),
            'id': ('exact', )
        }


class CityResource(ModelResource):
    country = fields.ForeignKey(CountryResource, "country")
    
    class Meta:
        queryset = City.objects.all()
        resource_name = "city"
        allowed_methods = ["get"]
        filtering = {
            'id': ('exact', )
        }
        excludes = ['country']
        max_limit = None
        default_format = "application/json"


class LocationResource(ModelResource):
    
    class Meta:
        queryset = Location.objects.all()
        resource_name = "location"
        allowed_methods = ["get"]
        filtering = {
            'country': ALL_WITH_RELATIONS,
            'city': ALL_WITH_RELATIONS,
            'coordinates': ('distance_lte', ),
            'id': ('exact', )
        }
        max_limit = 20
        