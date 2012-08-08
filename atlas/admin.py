from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from atlas.models import Location, City, Country, Region


class LocationAdminForm(forms.ModelForm):
    # add some Javascript to make the form more interactive later on
    pass


class LocationAdmin(admin.ModelAdmin):
    form = LocationAdminForm


admin.site.register(Location, LocationAdmin)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Region)