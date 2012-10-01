from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.geos import LineString

from atlas.models import Location, City, Country, Region
from atlas.utils import get_city


class LocationAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LocationAdminForm, self).__init__(*args, **kwargs)
        self.fields['country'].required = False
        #self.fields['city'].required = False

    def clean(self, *args, **kwargs):
        cd = super(LocationAdminForm, self).clean(*args, **kwargs)
        '''if cd['city'] == 'no_city':
            del cd['city']'''

        # fill in the blanks on the form, if possible
        '''if cd.get('coordinates', None) and not cd.get('city', None):
            cd['city'] = get_city(position=cd['coordinates'])'''
        # if cd.get('city', None):
        if not cd.get('country', None) or cd['country'] != cd['city'].country:
            cd['country'] = cd['city'].country
        '''else:
            self.errors.clear()
            raise forms.ValidationError("A city or coordinates are required.")'''

        # check that fields are consistent
        '''success, msg = self.check_consistency(cd)
        if not success:
            raise forms.ValidationError(msg)'''

        return cd

    '''def clean_city(self):
        if self.cleaned_data.get('city', None):
            return self.cleaned_data['city']
        return 'no_city'''

    # checks that fields are geographically consistent
    def check_consistency(self, cleaned_data):
        if cleaned_data['city'].country != cleaned_data['country']:
            return (False, "The location's city and country do not match.")
        if cleaned_data['coordinates']:
            line = LineString(cleaned_data['coordinates'], cleaned_data['city'].coordinates, srid=4326)
            line.transform(53031)  # transform to two-point equidistant project
            # if coordinate is more than 500km away from city
            if line.length > 500000:
                return (False, "The location's coordinates are more than 500km away from its city.")
        return (True, "")


class SearchByNameAdmin(admin.ModelAdmin):
    search_fields = ['name']


class LocationAdmin(SearchByNameAdmin):
    form = LocationAdminForm


admin.site.register(Location, LocationAdmin)
admin.site.register(City, SearchByNameAdmin)
admin.site.register(Country, SearchByNameAdmin)
admin.site.register(Region, SearchByNameAdmin)