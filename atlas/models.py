from django.contrib.gis.db import models

from south.modelsinspector import add_introspection_rules

from photologue.models import Photo

from category.models import Category

from atlas.fields import CoordinateField


class Country(models.Model):
    objects = models.GeoManager()
    
    name = models.CharField(max_length=50)
    country_code = models.CharField(
        max_length=2,
        unique=True,
        db_index=True,
    )
    # the average longitude/latitude for the country
    coordinates = CoordinateField(
        srid=4326,
        geography=True,
        null=True,
        blank=True
    )
    # geography is True because we need to deal with global coordinates
    border = models.MultiPolygonField(
        srid=4326,
        geography=True,
        null=True,
        blank=True
    )
    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ('name',)

    def __unicode__(self):
        return self.name
        

class Region(models.Model):
    objects = models.GeoManager()
    
    name = models.CharField(max_length=128)
    # uses fips10-4 2-digit region codes and US/CA codes
    code = models.CharField(
        max_length=2,
        db_index=True
    )
    # the average longitude/latitude for the region
    coordinates = CoordinateField(
        srid=4326,
        geography=True,
        null=True,
        blank=True
    )
    border = models.MultiPolygonField(
        srid=4326,
        geography=True,
        null=True,
        blank=True
    )
    country = models.ForeignKey(Country)
    
    class Meta:
        ordering = ('name',)
        unique_together = ('country', 'code',)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.country.country_code)


class City(models.Model):
    objects = models.GeoManager()
    
    name = models.CharField(
        max_length=128,
        db_index=True
    )
    coordinates = CoordinateField(
        srid=4326,
        geography=True,
        null=True,
        blank=True
    )
    region = models.ForeignKey(
        Region,
        null=True,
        blank=True
    )
    country = models.ForeignKey(Country)
    
    class Meta:
        verbose_name_plural = 'Cities'
        ordering = ('name',)
    
    def __unicode__(self):
        if self.region is not None:
            return "%s - %s (%s)" % (self.name, self.region.name, self.country.country_code)
        return "%s (%s)" % (self.name, self.country.country_code)


class Location(models.Model):
    objects = models.GeoManager()
    
    name = models.CharField(
        max_length=128,
        db_index=True
    )
    # necessary to do decent location filtering
    coordinates = CoordinateField(
        srid=4326,
        geography=True,
        null=True,
        blank=True
    )
    country = models.ForeignKey(Country)
    city = models.ForeignKey(City)
    description = models.TextField(
        max_length=1024,
        null=True,
        blank=True
    )
    photo = models.ForeignKey(
        Photo,
        null=True,
        blank=True
    )
    address = models.TextField(
        max_length=512,
        null=True,
        blank=True
    )

    @property
    def get_google_map_url(self):
        return "http://maps.google.com/maps?q=%f,%f&ll=%f,%f&z=13" \
            % (self.coordinates.y, self.coordinates.x, self.coordinates.y, self.coordinates.x)

    def __unicode__(self):
        if self.city is not None:
            return "%s - %s (%s)" % (self.name, self.city.name, self.country.name)
        return "%s (%s)" % (self.name, self.country.name)


add_introspection_rules([], ["^atlas\.fields\.CoordinateField"])
add_introspection_rules([], ["^photologue\.models\.TagField"])
