from django.contrib.gis.geoip import GeoIP
from django.conf import settings
from django.db.models.query import Q

from atlas.models import City, Region, Country


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
        
        if DB_ENGINE.rfind('mysql') >= 0:
            qs = qs.extra(select={'distance': \
                'distance_sphere(`atlas_city`.`coordinates`, geomfromtext(\'%s\', %d))' \
                % (str(position), position.srid)}).order_by('distance')
        else:
            qs = qs.distance(position).order_by('distance')

        if qs:
            city = qs[0]

    return city
        