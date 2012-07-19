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
    if code in code_geom:
        code_geom[code]["pk"] = pk
    else:
        code_geom[code] = {"pk": pk}
    country["model"] = "locations.country"
    country["pk"] = pk
    pk += 1

city_file = open(os.path.join(base, "datasets/MaxMind Cities/worldcitiespop.txt"))
pk = 1
cities = []
for line in city_file:
    els = line.split(",")
    if els[0] != 'Country':
        code = els[0].upper()
        city = els[1]
        lat = els[5]
        lon = els[6]
        cities.append({
            "pk": pk,
            "model": "locations.city",
            "fields": {
                "name": city,
                "coordinates": "POINT (%s %s)" % (lat, lon),
                "country": code_geom[code]["pk"]
            }
        })
        pk += 1
    
city_file.close()
f = open(os.path.join(base, "fixtures/countries.json"), "w")
output = json.dumps(countries + cities)
output.encode("utf-8")
f.write(output)
f.close()