from django import forms

from jmbo.forms import as_div

from atlas.models import Country, Region, City

class SelectLocationForm(forms.Form):
    country = forms.ChoiceField(
        choices= Country.objects.all().values_list('country_code', 'name'),
        required=True,
    )
    city = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(SelectLocationForm, self).__init__(*args, **kwargs)
        self.fields['country'].choices = [('', '---------'), ] + self.fields['country'].choices
        if 'location' in self.request.session:
            city = self.request.session['location']['city']
            self.fields['country'].initial = city.country.country_code
            self.fields['city'].initial = city.name

    as_div = as_div