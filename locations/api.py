from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr

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


class LocationResource(ModelResource):
    country = fields.ForeignKey(CountryResource, "country")
    city = fields.ForeignKey(CityResource, "city", null=True)
    
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
        default_format = "application/json"

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
        orm_filters = super(LocationResource, self).build_filters(filters)
        
        if 'location' in filters:
            lon, lat = filters['location'].split(' ')
            point = fromstr('POINT (%s %s)' % (lon, lat), srid=4326)
            dist = float(filters['distance']) if 'distance' in filters else 5000
            orm_filters["coordinates__distance_lte"] = (point, dist)

        return orm_filters
        