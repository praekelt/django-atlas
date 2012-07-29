import re

from django import forms
from django.contrib.gis.db import models
from django.contrib.gis.forms import fields
from django.forms.widgets import MultiWidget, TextInput
from django.conf import settings


class LonLatWidget(MultiWidget):

    def __init__(self, **kwargs):
        self.longitude = 0
        self.latitude = 0
        attrs = kwargs['attrs'] if 'attrs' in kwargs else None    
        defaults = {'widgets': (TextInput(attrs=attrs), TextInput(attrs=attrs))}
        defaults.update(kwargs)
        super(LonLatWidget, self).__init__(**defaults)

    def decompress(self, value):
        if value:
            m = re.match(r'POINT \((?P<lon>[-+]?\d+(\.\d*)?) (?P<lat>[-+]?\d+(\.\d*)?)\)', str(value))
            return [m.group('lon'), m.group('lat')]
        return [None, None]
    
    def render(self, name, value, attrs=None):
        vals = self.decompress(value)
        if vals[0] is not None and vals[1] is not None:
            self.longitude = float(vals[0])
            self.latitude = float(vals[1])
        return super(LonLatWidget, self).render(name, value, attrs)
    
    def format_output(self, rendered_widgets):
        pat = r'id="(?P<label>\w+)"'
        id1 = re.search(pat, rendered_widgets[0]).group('label')
        id2 = re.search(pat, rendered_widgets[1]).group('label')
        map_code = u''
        map_key = settings.DJANGO_ATLAS.get('google_maps_api_key', None)
        if map_key:
            map_code = u'''<script type="text/javascript">
                                LonLatWidget = {
                                    initialize: function() {
                                        var lon = %f, lat = %f;
                                        var hasLocation = !(lon == 0 && lat == 0);
                                        var mapOptions = {
                                            zoom: hasLocation ? 12 : 2,
                                            center: new google.maps.LatLng(lat, lon),
                                            disableDefaultUI: true,
                                            mapTypeId: google.maps.MapTypeId.ROADMAP
                                        }
                                        var map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
                                        var marker = new google.maps.Marker({
                                            map: map,
                                            title: 'Selected location'
                                        });
                                        if (hasLocation) {
                                            marker.setPosition(new google.maps.LatLng(lat, lon));
                                        }
                                        google.maps.event.addListener(map, 'click', function(event) {
                                            var pos = event.latLng;
                                            document.getElementById("%s").value = pos.lng();
                                            document.getElementById("%s").value = pos.lat();
                                            marker.setPosition(pos);
                                        });
                                    },

                                    loadScript: function() {
                                        var script = document.createElement("script");
                                        script.type = "text/javascript";
                                        script.src = "http://maps.googleapis.com/maps/api/js?key=%s&sensor=false&callback=LonLatWidget.initialize";
                                        document.body.appendChild(script);
                                    }
                                };
                                
                                if (window.addEventListener) {
                                    window.addEventListener('load', LonLatWidget.loadScript, false);
                                } 
                                else if (window.attachEvent) {
                                    window.attachEvent('onload', LonLatWidget.loadScript);
                                }
                            </script>''' \
                % (self.longitude, self.latitude, id1, id2, map_key)
            map_code += u'''<div id="map_canvas" style="width: 600px; height: 600px"></div>'''
        return u'''<table><tr><td><label for="%s">Longitude:</label></td><td>%s</td></tr>
                <tr><td><label for="%s">Latitude:</label></td><td>%s</td></tr></table>%s''' \
            % (id1, rendered_widgets[0], id2, rendered_widgets[1], map_code)


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


class CoordinateField(models.PointField):
    
    def formfield(self, **kwargs):
        defaults = {'form_class': CoordinateFormField}
        defaults.update(kwargs)
        return super(CoordinateField, self).formfield(**defaults)