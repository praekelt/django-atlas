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

# get full country dataset
f = open(os.path.join(base, "datasets/countries.json"))
countries = json.loads(f.read())
f.close()
sql_country = "INSERT INTO locations_country (id,name,country_code,border) VALUES ("
pk = 1
for country in countries:
    fields = country["fields"]
    code = fields["country_code"]
    fields["border"] = code_geom[code]["geom"] if code in code_geom else None
    if fields["border"] is not None and "MULTIPOLYGON" not in fields["border"]:
        fields["border"] = "MULTIPOLYGON (%s)" % fields["border"][8:]
    if code in code_geom:
        code_geom[code]["pk"] = pk
    else:
        code_geom[code] = {"pk": pk}
    sql_country += "(%d,'%s','%s',ST_GeomFromText('%s',4326))," \
        % (pk, fields['title'], fields['country_code'], fields['border'])
    pk += 1
sql_country = sql_country[:-1] + ");"

# get region data
f = open(os.path.join(base, "datasets/MaxMind Cities/fips10-4.csv"))
sql_region = "INSERT INTO locations_region (id,name,code,country_id) VALUES ("
pk = 1
r_code_pk = {}
for line in f:
    c_code = line[0:2]
    r_code = line[3:5]
    name = line[6:].rstrip().strip('"')
    r_code_pk["%s%s" % (c_code, r_code)] = pk
    sql_region += "(%d,'%s','%s',%d)," \
        % (pk, name, r_code, code_geom[c_code]["pk"])
    pk += 1
f.close()
sql_region = sql_region[:-1] + ");"

# get city data
f = open(os.path.join(base, "datasets/MaxMind Cities/worldcitiespop.csv"))
sql_city = "INSERT INTO locations_city (id,name,coordinates,region_id,country_id) VALUES ("
pk = 1
for line in f:
    els = line.split(",")
    if els[0] != 'Country':
        code = els[0].upper()
        city = els[2].decode('iso-8859-1')
        lat = els[5]
        lon = els[6].rstrip()
        sql_city += "(%d,'%s'," % (pk, city)
        if len(lat) > 0 and len(lon) > 0:
            sql_city += "ST_GeomFromText('%s',4326)," % ("POINT(%s %s)" % (lon, lat))
        else:
            sql_city += "null,"
        key = "%s%s" % (code, els[3])
        if key in r_code_pk:
            sql_city += "%d," % r_code_pk[key]
        else:
            sql_city += "null,"
        sql_city += "%d)," % (code_geom[code]["pk"], )
        pk += 1
        print(pk)
f.close()
sql_city = sql_city[:-1] + ");"

f = open(os.path.join(base, "datasets/data.sql"), 'w')
sql = sql_country + sql_region + sql_city
f.write(sql.encode('utf8'))
f.close()
