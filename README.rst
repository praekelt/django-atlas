django-atlas
===============

Geolocation models, data and tools using GeoDjango

Requirements
------------

The following were used for development/testing:

1. Django 1.3
2. PostgreSQL 9.1
3. PostGIS 1.5.2
4. SQLite 3.7.9
5. libspatialite3
6. django-photologue 2.7 (fork maintained by Praekelt at https://github.com/praekelt/django-photologue)
7. django-category 0.1 (at https://github.com/praekelt/django-category)
8. django-tastypie 0.9.11
9. libgeoip1 1.4.8

You might need to apply a PostGIS patch to Django that can be found here: https://code.djangoproject.com/ticket/16778. If you get a database encoding error when loading
initial data, your version of Django has not been patched. You can also use SQLite and MySQL with django-atlas, although MySQL is very lacking in terms of GIS. 

Add the following to your INSTALLED_APPS:

1. django.contrib.gis
2. django.contrib.admin
3. atlas
4. photologue
5. category
6. tastypie

GeoDjango has some additional installation requirements. They can be found here: https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/.
Follow those instructions and create a spatial database. Then add it to the DATABASES dictionary in your settings as the default database.
::
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'demo_geo',
            'USER': 'demo',
            'PASSWORD': 'demo',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

Atlas uses MaxMind's IP geolocation library and datasets. The following settings need to be included for this to work:
::
    GEOIP_PATH = '.../django-atlas/atlas/datasets/MaxMind/'
    GEOIP_CITY = 'GeoLiteCity.dat'
    GEOIP_COUNTRY = 'GeoIPv6.dat'

You can also add a Google Maps API key setting (see below). This will enable the LonLatWidget to use Google Maps for selecting coordinates.
::
    DJANGO_ATLAS = {
        'google_maps_api_key': 'XXX...',
    }

Datasets
--------

The geo data required by django-atlas can be downloaded at https://github.com/downloads/praekelt/django-atlas/data_postgresql.tbz2 for PostgreSQL or
https://github.com/downloads/praekelt/django-atlas/data_mysql.tbz2 for MySQL. Extract data.sql and load the data using ``psql -U user -W -d demo_geo < data.sql`` for PostgreSQL, or ``mysql -u user -p -D demo_geo < data.sql``
for MySQL.

MaxMind's IP geolocation datasets are available at http://www.maxmind.com/download/geoip/database/. MaxMind updates these datasets on a regular basis.