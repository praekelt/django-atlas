import math

from django.contrib.gis.geoip import GeoIP
from django.contrib.gis.geos import fromstr
from django.conf import settings
from django.db.models.query import Q

from atlas.models import City, Region, Country


DB_ENGINE = settings.DATABASES['default']['ENGINE']
RADIUS_EARTH = 6378100  # radius of earth in metres

'''
Returns city based on either IP address or longitude/latitude position.
An IP address lookup is fairly fast while a position lookup is expensive.
'''
def get_city(ip=None, position=None):
    city = None
    qs = None
    
    # narrow location down to a country using IP address
    if ip:
        city_geoip = GeoIP().city(ip)
        if city_geoip:
            qs = City.objects.filter(country__country_code=city_geoip['country_code'])
            # if no gps coordinates, use the city obtained from IP address
            if not position:
                qs = qs.filter(name=city_geoip['city'])
                if 'region' in city_geoip:
                    qs = qs.filter(region__code=city_geoip['region'])
                if qs:
                    city = qs[0]
    
    # find closest city based on GPS coordinates
    if position:
        # if we don't have a country-filtered queryset (no IP address or IP lookup failed)
        if not qs:
            if DB_ENGINE.rfind('mysql') >= 0:
                # select 5 closest countries
                closest_countries = Country.objects.exclude(coordinates__isnull=True).extra(select={'distance': \
                    'distance_sphere(`atlas_country`.`coordinates`, geomfromtext(\'%s\', %d))' \
                    % (str(position), position.srid)})
                closest_countries = closest_countries.order_by('distance')[:5]
                # cannot use values_list
                closest_countries = [c.id for c in closest_countries]
                # select closest countries' regions
                regions = Region.objects.exclude(coordinates__isnull=True).filter(country__in=closest_countries)
                regions = regions.extra(select={'distance': \
                    'distance_sphere(`atlas_region`.`coordinates`, geomfromtext(\'%s\', %d))' \
                    % (str(position), position.srid)}).order_by('distance')
            else:
                # select 5 closest countries
                closest_countries = Country.objects.exclude(coordinates__isnull=True).distance(position).order_by( \
                        'distance')[:5]
                # cannot use values_list
                closest_countries = [c.id for c in closest_countries]
                # select closest countries' regions
                regions = Region.objects.exclude(coordinates__isnull=True).filter(country__in=closest_countries \
                        ).distance(position).order_by('distance')

            # remove countries that are divided into regions with coordinates
            for region in regions:
                    try:
                        closest_countries.remove(region.country_id)
                    except:
                        pass
            regions = regions[:5] if len(regions) > 5 else regions
            closest_regions = [r.id for r in regions]

            qs = City.objects.filter(Q(region__in=closest_regions) | Q(country__in=closest_countries))
        
        # select cities within a minimum bounding rectangle of 100km radius
        qs = qs.filter(coordinates__within=)
        
        # order cities by their distance
        if DB_ENGINE.rfind('mysql') >= 0:
            qs = qs.extra(select={'distance': \
                'distance_sphere(`atlas_city`.`coordinates`, geomfromtext(\'%s\', %d))' \
                % (str(position), position.srid)}).order_by('distance')
        else:
            qs = qs.distance(position).order_by('distance')
        
        # select closest city
        if qs:
            city = qs[0]

    return city


"""CREATE FUNCTION `distance_sphere`
                            (a POINT, b POINT)
                            RETURNS double DETERMINISTIC
                            RETURN 6378100 * 2 * ASIN(SQRT( POWER(SIN((y(a) - y(b)) *
                            pi()/180 / 2), 2) +COS(y(a) * pi()/180) * COS(y(b) *
                            pi()/180) * POWER(SIN((x(a) - x(b)) * pi()/180 / 2), 2)));"""
def get_mbr_for_radius(point, radius):
    theta = (radius / RADIUS_EARTH) * (180 / math.pi)
    norm_x = point.x + 180
    norm_y = point.y + 90
    min_lon = norm_x - theta
    min_lon = 360 - min_lon - 180 if min_lon < 0 else min_lon - 180
    max_lon = (norm_x + theta) % 360 - 180
    min_lat = norm_x - theta
    min_lat = 180 - min_lat - 90 if min_lat < 0 else min_lat - 90
    max_lat = norm_x + theta
    fromstr("POLYGON((%f %f, %f %f, %f %f, %f %f, %f %f))" % \
        (min_lon, min_lat, min_lon, max_lat, max_lon, max_lat, max_lon, min_lat, min_lon, min_lat), \
        point.srid)