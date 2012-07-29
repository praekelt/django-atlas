import random
import math

from atlas.models import Country, Region, City, Location


'''
Generate locations in and around the selected cities, using the area of Cape Town as a guide.
The probability of locations is higher towards the center of the city, tapering off further away.
'''
def generate():
    # select Cape Town, Stellenbosch, Worcester and Johannesburg
    country_id = Country.objects.get(country_code='ZA').id
    cities = City.objects.filter(country=country_id, \
        name__in=('Cape Town', 'Stellenbosch', 'Worcester', 'Johannesburg')).exclude( \
        region__name='Limpopo').values_list('id', 'name', 'coordinates')
    # span of cape town
    lon = (18.39111328125, 18.689117431640625)
    x_max = (lon[1] - lon[0]) / 2  # radius on 'x'
    lat = (-34.031038397347814, -33.82023008524739)
    y_max = (lat[1] - lat[0]) / 2  # radius on 'y'
    # ellipse equation - t ranges from 0 to 2PI
    x = lambda t, a: a * math.cos(t)
    y = lambda t, b: b * math.sin(t)
    objects = []
    for city in cities:
        center_x = city[2].x
        center_y = city[2].y
        for i in range(1, 1001):
            t = random.random() * math.pi * 2
            fraction = math.fabs(random.normalvariate(0, 0.5))
            x_new = center_x + x(t, fraction * x_max)
            y_new = center_y + y(t, fraction * y_max)
            objects.append({
                "model": "atlas.Location",
                "fields": {
                    "name": ("%s_%d" % (city[1], i)).encode("ascii"),
                    "country": {"model": "atlas.Country", "fields": {"id": int(country_id)}},
                    "city": {"model": "atlas.City", "fields": {"id": int(city[0])}},
                    "coordinates": "POINT(%f %f)" % (x_new, y_new),
                },
            })       
    return objects