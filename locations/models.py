from django.contrib.gis.db import models

from photologue.models import Photo

from category.models import Category


class Country(models.Model):
    objects = models.GeoManager()
    
    name = models.CharField(max_length=50)
    country_code = models.CharField(
        max_length=2,
        unique=True,
        db_index=True,
    )
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
        

class City(models.Model):
    objects = models.GeoManager()
    
    name = models.CharField(max_length=128)
    coordinates = models.PointField(
        srid=4326,
        geography=True,
        null=True,
        blank=True
    )
    country = models.ForeignKey(Country)
    
    class Meta:
        verbose_name_plural = 'Cities'
        ordering = ('name',)
    
    def __unicode__(self):
        return self.name


class Location(models.Model):
    objects = models.GeoManager()
    
    name = models.CharField(max_length=128)
    # geography is True because we need to deal with global coordinates
    coordinates = models.PointField(
        srid=4326,
        geography=True,
        null=True,
        blank=True
    )
    country = models.ForeignKey(
        Country,
        db_index=True
    )
    city = models.ForeignKey(
        City,
        db_index=True
    )
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
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True
    )
    
    def __unicode__(self):
        return self.name


# must override the default manager with GeoManager to allow for queries on related objects
#Category.add_to_class('objects', models.GeoManager())
#ImageModel.add_to_class('objects', models.GeoManager())
