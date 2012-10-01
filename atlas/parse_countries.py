import os
try:
    import simplejson as json
except:
    import json
from StringIO import StringIO

from django.contrib.gis.gdal import DataSource


base = os.path.dirname(os.path.abspath(__file__))
sql = StringIO()

# extract geometry of each country
ds = DataSource(os.path.join(base, "datasets/TM/TM_WORLD_BORDERS-0.3.shp"))
layer = ds[0]
code_geom = {}
for feature in layer:
    code_geom[feature.get("ISO2")] = {"geom": feature.geom.wkt}

# get centroid of each country
f = open(os.path.join(base, "datasets/MaxMind/country_coords.csv"))
for line in f:
    vals = line.split(",")
    if vals[0] in code_geom:
        code_geom[vals[0]]['centroid'] = 'POINT (%s %s)' % (vals[2].strip(), vals[1])
    else:
        code_geom[vals[0]] = {"centroid": 'POINT (%s %s)' % (vals[2].strip(), vals[1])}
f.close()

# get full country dataset
f = open(os.path.join(base, "datasets/countries.json"))
countries = json.loads(f.read())
f.close()
sql_country = "INSERT INTO atlas_country (id,name,country_code,border,coordinates) VALUES "
pk = 1
for country in countries:
    fields = country["fields"]
    code = fields["country_code"]
    fields["border"] = code_geom[code]["geom"] if code in code_geom else None
    if fields["border"] is not None and "MULTIPOLYGON" not in fields["border"]:
        fields["border"] = "MULTIPOLYGON(%s)" % fields["border"][8:]
        sql_country += "(%d,'%s','%s',GeometryFromText('%s', 4326),%s)," \
        % (pk, fields['title'].replace("'", "''"), fields['country_code'], fields['border'], \
            "GeometryFromText('%s', 4326)" % code_geom[code]['centroid'] if \
            (code in code_geom and 'centroid' in code_geom[code]) else 'null')
    else:
        sql_country += "(%d,'%s','%s',null,%s)," \
        % (pk, fields['title'].replace("'","''"), fields['country_code'], \
            "GeometryFromText('%s', 4326)" % code_geom[code]['centroid'] if \
            (code in code_geom and 'centroid' in code_geom[code]) else 'null')
    if code in code_geom:
        code_geom[code]["pk"] = pk
    else:
        code_geom[code] = {"pk": pk}
    pk += 1
sql_country = sql_country[:-1] + ";\n"
sql.write(sql_country)

# get region data
r_code_centroid = {}
f = open(os.path.join(base, "datasets/MaxMind/us_regions_coords.csv"))
for line in f:
    vals = line.split(",")
    r_code_centroid["%s%s" % ('US', vals[0])] = 'POINT (%s %s)' % (vals[2].strip(), vals[1])
f.close()

region_files = ("datasets/MaxMind/fips10-4.csv", "datasets/MaxMind/us_regions.csv")
pk = 1
r_code_pk = {}
for f_name in region_files:
    f = open(os.path.join(base, f_name))
    sql_region = "INSERT INTO atlas_region (id,name,code,country_id,coordinates) VALUES "
    fips = f_name.rfind('fips10-4.csv') > -1
    for line in f:
        c_code = line[0:2]
        # use fips codes for everything except US states
        if (fips and c_code != 'US') or (not fips and c_code == 'US'):
            r_code = line[3:5]
            name = line[6:].rstrip().strip('"')
            key = "%s%s" % (c_code, r_code)
            r_code_pk[key] = pk
            sql_region += "(%d,'%s','%s',%d, %s)," \
                % (pk, name.replace("'","''"), r_code, code_geom[c_code]["pk"], \
                "GeometryFromText('%s', 4326)" % r_code_centroid[key] if key in r_code_centroid else 'null')
            pk += 1
    f.close()
    sql_region = sql_region[:-1] + ";\n"
    sql.write(sql_region)

# get city data
f = open(os.path.join(base, "datasets/MaxMind/worldcitiespop.csv"))
sql.write("INSERT INTO atlas_city (id,name,coordinates,region_id,country_id) VALUES ")
pk = 1
counter = 0
for line in f:
    els = line.split(",")
    if els[0] != 'Country':
        code = els[0].upper()
        city = els[2].decode('iso-8859-1').replace("'","''")
        lat = els[5]
        lon = els[6].rstrip()
        sql.write("(%d,'%s'," % (pk, city))
        if len(lat) > 0 and len(lon) > 0:
            sql.write("GeometryFromText('POINT(%s %s)',4326)," % (lon, lat))
        else:
            sql.write("null,")
        key = "%s%s" % (code, els[3])
        if key in r_code_pk:
            sql.write("%d," % r_code_pk[key])
        else:
            sql.write("null,")
        sql.write("%d)" % (code_geom[code]["pk"], ))
        if pk != 3173958 and counter < 1000:
            sql.write(",")
        else:
            sql.write(";")
            if pk != 3173958: 
                sql.write("\nINSERT INTO atlas_city (id,name,coordinates,region_id,country_id) VALUES ")
            counter = 0
        counter += 1
        pk += 1
        print("%d / 3173958" % pk)
f.close()

f = open(os.path.join(base, "data.sql"), 'w')
f.write(sql.getvalue().encode('utf8'))
f.close()
