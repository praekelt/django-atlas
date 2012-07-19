import os
import simplejson as json

from django.contrib.gis.gdal import DataSource

base = os.path.dirname(os.path.abspath(__file__))

# extract geometry of each country
ds = DataSource(os.path.join(base, "datasets/TM_WORLD_BORDERS-0.3/TM_WORLD_BORDERS-0.3.shp"))
layer = ds[0]
code_geom = {}
for feature in layer:
    code_geom[feature.get("ISO2")] = {"geom": feature.geom.wkt}
    

# get full country dataset from foundry
f = open(os.path.join(base, "../../jmbo-foundry/foundry/fixtures/countries.json"))
countries = json.loads(f.read())
f.close()
pk = 1
for country in countries:
    fields = country["fields"]
    del fields["slug"]
    del fields["minimum_age"]
    name = fields["title"]
    del fields["title"]
    fields["name"] = name
    code = fields["country_code"]
    fields["border"] = code_geom[code]["geom"] if code in code_geom else None
    if fields["border"] is not None and "MULTIPOLYGON" not in fields["border"]:
        fields["border"] = "MULTIPOLYGON (%s)" % fields["border"][8:]
    if code in code_geom:
        code_geom[code]["pk"] = pk
    else:
        code_geom[code] = {"pk": pk}
    country["model"] = "locations.country"
    country["pk"] = pk
    pk += 1

city_file = open(os.path.join(base, "datasets/MaxMind Cities/worldcitiespop.txt"))
pk = 1
city_groups = []
cities = []
count = 0
for line in city_file:
    els = line.split(",")
    if els[0] != 'Country':
        code = els[0].upper()
        city = els[2].decode("utf-8", "replace")
        lat = els[5]
        lon = els[6].rstrip()
        city = {
            "pk": pk,
            "model": "locations.city",
            "fields": {
                "name": city,
                "country": code_geom[code]["pk"]
            }
        }
        if len(lat) > 0 and len(lon) > 0:
            city['fields']['coordinates'] = "POINT(%s %s)" % (lon, lat)
        cities.append(city)
        pk += 1
        count += 1
        if count >= 100000:
            count = 0
            city_groups.append(cities)
            cities = []
city_groups.append(cities)
    
city_file.close()
f = open(os.path.join(base, "fixtures/countries.json"), "w")
f.write(json.dumps(countries))
f.close()
count = 1
for cities in city_groups:
    f = open(os.path.join(base, "fixtures/cities_%d.json" % count), "w")
    f.write(json.dumps(cities))
    f.close()
    count += 1
