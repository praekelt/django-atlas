django-location
===============

Requirements
------------
The following were used for development/testing:
1. Django 1.3
2. PostgreSQL 9.1
3. PostGIS 1.5.2

You might need to apply a PostGIS patch to Django that can be found here: https://code.djangoproject.com/ticket/16778. If you get a database encoding error when loading
initial data, your version of Django has not been patched.

Add the following to your INSTALLED_APPS:
1. django.contrib.gis
2. django.contrib.admin
3. locations

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

You can also add a GOOGLE_MAPS_API_KEY = 'XXX...' setting. This will enable the LonLatWidget to use Google Maps for selecting coordinates.