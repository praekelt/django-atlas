from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr

from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields

from locations.models import Country, City, Location


class CountryResource(ModelResource):
    
    class Meta:
        queryset = Country.objects.all()
        resource_name = "country"
        excludes = ('border', )
        # not directly exposed via api
        allowed_methods = []
        filtering = {
            'country_code': ('exact', ),
            'id': ('exact', )
        }


class CityResource(ModelResource):
    country = fields.ForeignKey(CountryResource, "country")
    
    class Meta:
        queryset = City.objects.all()
        resource_name = "city"
        # not directly exposed via api
        allowed_methods = []
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
        excludes = ('id', )
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
    
    def dehydrate_country(self, bundle):
        if bundle.obj.country:
            c = bundle.obj.country
            return {'name': c.name, 'country_code': c.country_code}
        return None
    
    def dehydrate_city(self, bundle):
        if bundle.obj.city:
            bundle.obj.city.name
        return None
    
    def dehydrate_coordinates(self, bundle):
        if bundle.obj.coordinates:
            c = bundle.obj.coordinates
            return {'longitude': c.x, 'latitude': c.y}
        return None
    
    def dehydrate(self, bundle):
        if bundle.obj.photo:
            bundle.data['photo_uri'] = bundle.obj.photo.get_location_thumbnail_smart_url()
        if bundle.obj.category:
            bundle.data['category'] = bundle.obj.category.name
        return bundle
