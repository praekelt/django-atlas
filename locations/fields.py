import re

from django import forms
from django.contrib.gis.db import models
from django.contrib.gis.forms import fields
from django.forms.widgets import MultiWidget, TextInput


class LonLatWidget(MultiWidget):

    def __init__(self, **kwargs):
        defaults = {'widgets': (TextInput, TextInput)}
        defaults.update(kwargs)
        super(LonLatWidget, self).__init__(**defaults)

    def decompress(self, value):
        if value:
            m = re.match(r'POINT \((?P<lon>[-+]?\d+(\.\d*)?) (?P<lat>[-+]?\d+(\.\d*)?)\)', str(value))
            return [m.group('lon'), m.group('lat')]
        return [None, None]


class CoordinateFormField(fields.GeometryField, forms.MultiValueField):
    
    def __init__(self, *args, **kwargs):
        defaults = {
            'widget': LonLatWidget,
            'fields': (forms.CharField, forms.CharField)
        }
        defaults.update(kwargs)
        fields.GeometryField.__init__(self, *args, **defaults)
        # remove arguments that MultiValueField won't accept
        defaults.pop('srid')
        defaults.pop('null')
        defaults.pop('geom_type')
        forms.MultiValueField.__init__(self, *args, **defaults)

    def clean(self, value):
        lon = value[0]
        lat = value[1]
        try:
            lon = float(lon)
        except ValueError:
            raise forms.ValidationError("Longitude is not a valid number")
        try:
            lat = float(lat)
        except ValueError:
            raise forms.ValidationError("Latitude is not a valid number")
        if lon < -180 or lon > 180:
            raise forms.ValidationError("Longitude is not within -180 to 180")
        if lat < -90 or lat > 90:
            raise forms.ValidationError("Latitude is not within -90 to 90")
        
        val = "POINT (%s %s)" % (value[0], value[1])
        return super(CoordinateFormField, self).clean(val)
    
    def compress(self, values):
        return "POINT (%s %s)" % (value[0], value[1])
    
    def render(self):
        print("rendering")
        super(CoordinateFormField, self).render()


class CoordinateField(models.PointField):
    
    def formfield(self, **kwargs):
        defaults = {'form_class': CoordinateFormField}
        defaults.update(kwargs)
        return super(CoordinateField, self).formfield(**defaults)
