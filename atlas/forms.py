from django import forms
from django.utils.safestring import mark_safe

from atlas.models import Country, Region, City

class SelectLocationForm(forms.Form):
    country = forms.ChoiceField(
        choices= Country.objects.all().values_list('country_code', 'name'),
        required=True,
    )
    region = forms.ChoiceField(
        choices=(),
        required=True,
    )
    city = forms.ChoiceField(
        choices=(),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(SelectLocationForm, self).__init__(*args, **kwargs)
        self.fields['country'].choices = [('', '---------'), ] + self.fields['country'].choices
        if 'location' in self.request.session:
            city = self.request.session['location']['city']
            self.fields['country'].initial = city.country.country_code
            if city.region:
                self.fields['region'].choices = Region.objects.filter(country=city.country).values_list('code', 'name')
                self.fields['region'].initial = city.region.code
                self.fields['city'].choices = City.objects.filter(region=city.region).values_list('id', 'name')
            else:
                self.fields['region'].widgets.attr['disabled'] = True
                self.fields['city'].choices = City.objects.filter(country=city.country).values_list('id', 'name')
            self.fields['city'].initial = city.id
        else:
            self.fields['region'].widgets.attr['disabled'] = True
            self.fields['city'].widgest.attr['disabled'] = True
    
    def __unicode__(self):
        html = super(SelectLocationForm, self).__unicode__()
        html += u'''<script type="text/javascript">
                    SelectLocationForm = {
                        onCountrySelected: function(event) {
                            var regions = $('#id_region').attr("disabled", "disabled").empty();
                            $('#id_city').attr("disabled", "disabled").empty();
                            var c_code = $("#id_country").val();
                            $.ajax({
                                url: "/atlas-api/v1/region/?format=json&limit=100&country__country_code=" + c_code,
                                success: function (data) {
                                    if (data.meta.total_count > 0) {
                                        $.each(data.objects, function(key, value) {   
                                            regions.append($("<option></option>")
                                                .attr("value",value.code)
                                                .text(value.name)); 
                                        });
                                        regions.removeAttr("disabled");
                                    }
                                    else {
                                        SelectLocationForm.onRegionSelected(undefined, true);
                                    }
                                },
                                error: SelectLocationForm.onError,
                                retries: 0,
                                max_retries: 5,
                            });
                        },
                        
                        onRegionSelected: function(event, no_regions) {
                            $('#id_city').attr("disabled", "disabled").empty();
                            var c_code = $("#id_country").val();
                            var cities = $("#id_city");
                            var on_cities_received = function (data) {
                                console.log(data);
                                $.each(data.objects, function(key, value) {   
                                    cities.append($("<option></option>")
                                        .attr("value",value.id)
                                        .text(value.name)); 
                                });
                                cities.removeAttr("disabled");
                            };
                            settings = {
                                success: on_cities_received,
                                error: SelectLocationForm.onError,
                                retries: 0,
                                max_retries: 5,
                            };
                            if (no_regions) {
                                settings.url = "/atlas-api/v1/city/?format=json&limit=10000&country__country_code=" + c_code;
                            }
                            else {
                                r_code = $("#id_region").val();
                                settings.url = "/atlas-api/v1/city/?format=json&limit=10000&region__code=" + r_code + "&country__country_code=" + c_code;
                                $.ajax(settings);
                            }
                        },
                        
                        onError: function (jqXHR, textStatus, error) {
                            if (textStatus == 'timeout') {
                                this.retries++;
                                if (this.retries <= this.max_retries) {
                                    $.ajax(this);
                                    return;
                                }
                                return;
                            }
                        },
                    };
                    
                    $(document).ready(function () {
                        $('#id_country').change(SelectLocationForm.onCountrySelected);
                        $('#id_region').change(SelectLocationForm.onRegionSelected);
                    });
                </script>'''
        return mark_safe(html)