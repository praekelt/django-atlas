from django.contrib.gis.geoip import GeoIP
from django.conf import settings

from atlas.models import City, Country


DB_ENGINE = settings.DATABASES['default']['ENGINE']

'''
Returns city based on either IP address or longitude/latitude position.
An IP address lookup is fairly fast while a position lookup is expensive.
'''
def get_city(ip=None, position=None):
    city = None
    if ip:
        city_dict = GeoIP().city(ip)
        qs = City.objects.filter(name=city_dict['city'],
                country__country_code=city_dict['country_code'])
        if 'region' in city_dict:
            qs = qs.filter(region__code=city_dict['region'])
        if qs:
            city = qs[0]
    
    if not city and position:
        # way too slow!!!!
        qs = City.objects.filter(country__border__contains=position)
        if not qs:
            qs = City.objects.filter(country__border__isnull=True)
        qs = qs.exclude(coordinates__isnull=True)
        if DB_ENGINE.rfind('mysql') >= 0:
            sql = 'distance_sphere(`atlas_city`.`coordinates`, geomfromtext(\'%s\', %d))' \
                    % (str(position), position.srid)
            qs = qs.extra(select={'distance': sql})
        else:
            qs = qs.distance(position)
        qs = qs.order_by('distance')
        if qs:
            city = qs[0]

    return city
        