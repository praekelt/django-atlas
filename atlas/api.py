import heapq

from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr
from django.conf import settings
from django.shortcuts import get_object_or_404

from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields

from atlas.models import Country, City, Location


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
        filters.pop('city', None)  # we don't want to exclude nearby cities
        orm_filters = super(LocationResource, self).build_filters(filters)

        return orm_filters
    
    def obj_get_list(self, request=None, **kwargs):
        if settings.DATABASES['default']['ENGINE'].rfind('mysql') == -1:
            return super(LocationResource, self).obj_get_list(request, **kwargs)
        # query that works on MySQL
        else:
            # do basic ORM filtering
            qs = super(LocationResource, self).get_object_list(request)
            city_dict = {}
            loc_heap = []
            point = None  # coordinates of the user
            if 'city' in request.GET:  # or geolocate them using GeoIP
                city = get_object_or_404(City, id=request.GET['city'])
                region_id = city.region.id
                if region_id is not None:
                    city_dict = dict(City.objects.filter(region=region_id).values_list('id', 'coordinates'))
                else:
                    city_dict = dict(City.objects.get(id=request.GET['city']).values_list('id', 'coordinates'))
                point = city.coordinates
            if 'location' in request.GET:
                lon, lat = request.GET['location'].split(' ')
                point = fromstr('POINT (%s %s)' % (lon, lat), srid=4326)
            if len(city_dict) > 0:
                qs = qs.filter(city__id__in=city_dict.keys())
            for loc in qs:
                point2 = loc.coordinates
                if point2 is None:
                   point2 = city_dict.get(loc.city_id, None)
                if point2 is not None:
                    heapq.heappush(loc_heap, (point.distance(point2), loc))
            qs = []
            limit = request.GET.get('limit', 20)
            offset = request.GET.get('limit', 0)
            num_items = limit + offset if limit + offset <= len(loc_heap) else len(loc_heap)
            if offset >= num_items:
                return qs
            else:
                for i in range(0, num_items):
                    qs.append(heapq.heappop(loc_heap)[1])
                return qs[offset:]
    
    def get_object_list(self, request):
        # do basic ORM filtering
        qs = super(LocationResource, self).get_object_list(request)
        # do advanced location filtering
        point = None
        if 'location' in request.GET:
            lon, lat = request.GET['location'].split(' ')
            point = fromstr('POINT (%s %s)' % (lon, lat), srid=4326)
        elif 'city' in request.GET:
            point = get_object_or_404(City, id=request.GET['city']).coordinates
        if point is not None:  # or geolocate them using GeoIP
            qs = qs.distance(point).order_by('distance')
        return qs
    
    def dehydrate_country(self, bundle):
        if bundle.obj.country:
            c = bundle.obj.country
            return {'name': c.name, 'country_code': c.country_code}
        return None
    
    def dehydrate_city(self, bundle):
        if bundle.obj.city:
           return bundle.obj.city.name
        return None
    
    def dehydrate_coordinates(self, bundle):
        if bundle.obj.coordinates:
            c = bundle.obj.coordinates
            return {'longitude': c.x, 'latitude': c.y}
        return None
    
    def dehydrate(self, bundle):
        if bundle.obj.photo:
            bundle.data['photo_uri'] = bundle.obj.photo.get_location_thumbnail_smart_url()
        return bundle
