# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.contrib.gis.geos import fromstr

class Migration(DataMigration):

    def forwards(self, orm):
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."
        orm['atlas.Country'].objects.filter(country_code='AD').update(coordinates=fromstr('POINT (1.5000 42.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AE').update(coordinates=fromstr('POINT (54.0000 24.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AF').update(coordinates=fromstr('POINT (65.0000 33.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AG').update(coordinates=fromstr('POINT (-61.8000 17.0500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AI').update(coordinates=fromstr('POINT (-63.1667 18.2500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AL').update(coordinates=fromstr('POINT (20.0000 41.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AM').update(coordinates=fromstr('POINT (45.0000 40.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AN').update(coordinates=fromstr('POINT (-68.7500 12.2500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AO').update(coordinates=fromstr('POINT (18.5000 -12.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AP').update(coordinates=fromstr('POINT (105.0000 35.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AQ').update(coordinates=fromstr('POINT (0.0000 -90.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AR').update(coordinates=fromstr('POINT (-64.0000 -34.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AS').update(coordinates=fromstr('POINT (-170.0000 -14.3333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AT').update(coordinates=fromstr('POINT (13.3333 47.3333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AU').update(coordinates=fromstr('POINT (133.0000 -27.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AW').update(coordinates=fromstr('POINT (-69.9667 12.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='AZ').update(coordinates=fromstr('POINT (47.5000 40.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BA').update(coordinates=fromstr('POINT (18.0000 44.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BB').update(coordinates=fromstr('POINT (-59.5333 13.1667)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BD').update(coordinates=fromstr('POINT (90.0000 24.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BE').update(coordinates=fromstr('POINT (4.0000 50.8333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BF').update(coordinates=fromstr('POINT (-2.0000 13.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BG').update(coordinates=fromstr('POINT (25.0000 43.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BH').update(coordinates=fromstr('POINT (50.5500 26.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BI').update(coordinates=fromstr('POINT (30.0000 -3.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BJ').update(coordinates=fromstr('POINT (2.2500 9.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BM').update(coordinates=fromstr('POINT (-64.7500 32.3333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BN').update(coordinates=fromstr('POINT (114.6667 4.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BO').update(coordinates=fromstr('POINT (-65.0000 -17.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BR').update(coordinates=fromstr('POINT (-55.0000 -10.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BS').update(coordinates=fromstr('POINT (-76.0000 24.2500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BT').update(coordinates=fromstr('POINT (90.5000 27.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BV').update(coordinates=fromstr('POINT (3.4000 -54.4333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BW').update(coordinates=fromstr('POINT (24.0000 -22.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BY').update(coordinates=fromstr('POINT (28.0000 53.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='BZ').update(coordinates=fromstr('POINT (-88.7500 17.2500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CA').update(coordinates=fromstr('POINT (-95.0000 60.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CC').update(coordinates=fromstr('POINT (96.8333 -12.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CD').update(coordinates=fromstr('POINT (25.0000 0.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CF').update(coordinates=fromstr('POINT (21.0000 7.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CG').update(coordinates=fromstr('POINT (15.0000 -1.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CH').update(coordinates=fromstr('POINT (8.0000 47.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CI').update(coordinates=fromstr('POINT (-5.0000 8.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CK').update(coordinates=fromstr('POINT (-159.7667 -21.2333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CL').update(coordinates=fromstr('POINT (-71.0000 -30.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CM').update(coordinates=fromstr('POINT (12.0000 6.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CN').update(coordinates=fromstr('POINT (105.0000 35.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CO').update(coordinates=fromstr('POINT (-72.0000 4.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CR').update(coordinates=fromstr('POINT (-84.0000 10.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CU').update(coordinates=fromstr('POINT (-80.0000 21.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CV').update(coordinates=fromstr('POINT (-24.0000 16.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CX').update(coordinates=fromstr('POINT (105.6667 -10.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CY').update(coordinates=fromstr('POINT (33.0000 35.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='CZ').update(coordinates=fromstr('POINT (15.5000 49.7500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='DE').update(coordinates=fromstr('POINT (9.0000 51.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='DJ').update(coordinates=fromstr('POINT (43.0000 11.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='DK').update(coordinates=fromstr('POINT (10.0000 56.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='DM').update(coordinates=fromstr('POINT (-61.3333 15.4167)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='DO').update(coordinates=fromstr('POINT (-70.6667 19.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='DZ').update(coordinates=fromstr('POINT (3.0000 28.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='EC').update(coordinates=fromstr('POINT (-77.5000 -2.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='EE').update(coordinates=fromstr('POINT (26.0000 59.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='EG').update(coordinates=fromstr('POINT (30.0000 27.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='EH').update(coordinates=fromstr('POINT (-13.0000 24.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='ER').update(coordinates=fromstr('POINT (39.0000 15.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='ES').update(coordinates=fromstr('POINT (-4.0000 40.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='ET').update(coordinates=fromstr('POINT (38.0000 8.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='EU').update(coordinates=fromstr('POINT (8.0000 47.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='FI').update(coordinates=fromstr('POINT (26.0000 64.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='FJ').update(coordinates=fromstr('POINT (175.0000 -18.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='FK').update(coordinates=fromstr('POINT (-59.0000 -51.7500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='FM').update(coordinates=fromstr('POINT (158.2500 6.9167)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='FO').update(coordinates=fromstr('POINT (-7.0000 62.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='FR').update(coordinates=fromstr('POINT (2.0000 46.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GA').update(coordinates=fromstr('POINT (11.7500 -1.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GB').update(coordinates=fromstr('POINT (-2.0000 54.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GD').update(coordinates=fromstr('POINT (-61.6667 12.1167)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GE').update(coordinates=fromstr('POINT (43.5000 42.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GF').update(coordinates=fromstr('POINT (-53.0000 4.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GH').update(coordinates=fromstr('POINT (-2.0000 8.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GI').update(coordinates=fromstr('POINT (-5.3667 36.1833)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GL').update(coordinates=fromstr('POINT (-40.0000 72.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GM').update(coordinates=fromstr('POINT (-16.5667 13.4667)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GN').update(coordinates=fromstr('POINT (-10.0000 11.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GP').update(coordinates=fromstr('POINT (-61.5833 16.2500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GQ').update(coordinates=fromstr('POINT (10.0000 2.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GR').update(coordinates=fromstr('POINT (22.0000 39.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GS').update(coordinates=fromstr('POINT (-37.0000 -54.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GT').update(coordinates=fromstr('POINT (-90.2500 15.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GU').update(coordinates=fromstr('POINT (144.7833 13.4667)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GW').update(coordinates=fromstr('POINT (-15.0000 12.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='GY').update(coordinates=fromstr('POINT (-59.0000 5.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='HK').update(coordinates=fromstr('POINT (114.1667 22.2500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='HM').update(coordinates=fromstr('POINT (72.5167 -53.1000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='HN').update(coordinates=fromstr('POINT (-86.5000 15.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='HR').update(coordinates=fromstr('POINT (15.5000 45.1667)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='HT').update(coordinates=fromstr('POINT (-72.4167 19.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='HU').update(coordinates=fromstr('POINT (20.0000 47.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='ID').update(coordinates=fromstr('POINT (120.0000 -5.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='IE').update(coordinates=fromstr('POINT (-8.0000 53.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='IL').update(coordinates=fromstr('POINT (34.7500 31.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='IN').update(coordinates=fromstr('POINT (77.0000 20.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='IO').update(coordinates=fromstr('POINT (71.5000 -6.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='IQ').update(coordinates=fromstr('POINT (44.0000 33.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='IR').update(coordinates=fromstr('POINT (53.0000 32.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='IS').update(coordinates=fromstr('POINT (-18.0000 65.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='IT').update(coordinates=fromstr('POINT (12.8333 42.8333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='JM').update(coordinates=fromstr('POINT (-77.5000 18.2500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='JO').update(coordinates=fromstr('POINT (36.0000 31.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='JP').update(coordinates=fromstr('POINT (138.0000 36.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='KE').update(coordinates=fromstr('POINT (38.0000 1.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='KG').update(coordinates=fromstr('POINT (75.0000 41.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='KH').update(coordinates=fromstr('POINT (105.0000 13.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='KI').update(coordinates=fromstr('POINT (173.0000 1.4167)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='KM').update(coordinates=fromstr('POINT (44.2500 -12.1667)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='KN').update(coordinates=fromstr('POINT (-62.7500 17.3333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='KP').update(coordinates=fromstr('POINT (127.0000 40.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='KR').update(coordinates=fromstr('POINT (127.5000 37.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='KW').update(coordinates=fromstr('POINT (47.6581 29.3375)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='KY').update(coordinates=fromstr('POINT (-80.5000 19.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='KZ').update(coordinates=fromstr('POINT (68.0000 48.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='LA').update(coordinates=fromstr('POINT (105.0000 18.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='LB').update(coordinates=fromstr('POINT (35.8333 33.8333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='LC').update(coordinates=fromstr('POINT (-61.1333 13.8833)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='LI').update(coordinates=fromstr('POINT (9.5333 47.1667)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='LK').update(coordinates=fromstr('POINT (81.0000 7.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='LR').update(coordinates=fromstr('POINT (-9.5000 6.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='LS').update(coordinates=fromstr('POINT (28.5000 -29.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='LT').update(coordinates=fromstr('POINT (24.0000 56.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='LU').update(coordinates=fromstr('POINT (6.1667 49.7500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='LV').update(coordinates=fromstr('POINT (25.0000 57.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='LY').update(coordinates=fromstr('POINT (17.0000 25.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MA').update(coordinates=fromstr('POINT (-5.0000 32.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MC').update(coordinates=fromstr('POINT (7.4000 43.7333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MD').update(coordinates=fromstr('POINT (29.0000 47.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='ME').update(coordinates=fromstr('POINT (19.0000 42.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MG').update(coordinates=fromstr('POINT (47.0000 -20.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MH').update(coordinates=fromstr('POINT (168.0000 9.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MK').update(coordinates=fromstr('POINT (22.0000 41.8333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='ML').update(coordinates=fromstr('POINT (-4.0000 17.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MM').update(coordinates=fromstr('POINT (98.0000 22.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MN').update(coordinates=fromstr('POINT (105.0000 46.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MO').update(coordinates=fromstr('POINT (113.5500 22.1667)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MP').update(coordinates=fromstr('POINT (145.7500 15.2000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MQ').update(coordinates=fromstr('POINT (-61.0000 14.6667)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MR').update(coordinates=fromstr('POINT (-12.0000 20.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MS').update(coordinates=fromstr('POINT (-62.2000 16.7500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MT').update(coordinates=fromstr('POINT (14.5833 35.8333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MU').update(coordinates=fromstr('POINT (57.5500 -20.2833)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MV').update(coordinates=fromstr('POINT (73.0000 3.2500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MW').update(coordinates=fromstr('POINT (34.0000 -13.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MX').update(coordinates=fromstr('POINT (-102.0000 23.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MY').update(coordinates=fromstr('POINT (112.5000 2.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='MZ').update(coordinates=fromstr('POINT (35.0000 -18.2500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='NA').update(coordinates=fromstr('POINT (17.0000 -22.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='NC').update(coordinates=fromstr('POINT (165.5000 -21.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='NE').update(coordinates=fromstr('POINT (8.0000 16.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='NF').update(coordinates=fromstr('POINT (167.9500 -29.0333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='NG').update(coordinates=fromstr('POINT (8.0000 10.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='NI').update(coordinates=fromstr('POINT (-85.0000 13.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='NL').update(coordinates=fromstr('POINT (5.7500 52.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='NO').update(coordinates=fromstr('POINT (10.0000 62.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='NP').update(coordinates=fromstr('POINT (84.0000 28.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='NR').update(coordinates=fromstr('POINT (166.9167 -0.5333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='NU').update(coordinates=fromstr('POINT (-169.8667 -19.0333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='NZ').update(coordinates=fromstr('POINT (174.0000 -41.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='OM').update(coordinates=fromstr('POINT (57.0000 21.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PA').update(coordinates=fromstr('POINT (-80.0000 9.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PE').update(coordinates=fromstr('POINT (-76.0000 -10.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PF').update(coordinates=fromstr('POINT (-140.0000 -15.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PG').update(coordinates=fromstr('POINT (147.0000 -6.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PH').update(coordinates=fromstr('POINT (122.0000 13.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PK').update(coordinates=fromstr('POINT (70.0000 30.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PL').update(coordinates=fromstr('POINT (20.0000 52.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PM').update(coordinates=fromstr('POINT (-56.3333 46.8333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PR').update(coordinates=fromstr('POINT (-66.5000 18.2500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PS').update(coordinates=fromstr('POINT (35.2500 32.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PT').update(coordinates=fromstr('POINT (-8.0000 39.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PW').update(coordinates=fromstr('POINT (134.5000 7.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='PY').update(coordinates=fromstr('POINT (-58.0000 -23.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='QA').update(coordinates=fromstr('POINT (51.2500 25.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='RE').update(coordinates=fromstr('POINT (55.6000 -21.1000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='RO').update(coordinates=fromstr('POINT (25.0000 46.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='RS').update(coordinates=fromstr('POINT (21.0000 44.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='RU').update(coordinates=fromstr('POINT (100.0000 60.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='RW').update(coordinates=fromstr('POINT (30.0000 -2.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SA').update(coordinates=fromstr('POINT (45.0000 25.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SB').update(coordinates=fromstr('POINT (159.0000 -8.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SC').update(coordinates=fromstr('POINT (55.6667 -4.5833)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SD').update(coordinates=fromstr('POINT (30.0000 15.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SE').update(coordinates=fromstr('POINT (15.0000 62.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SG').update(coordinates=fromstr('POINT (103.8000 1.3667)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SH').update(coordinates=fromstr('POINT (-5.7000 -15.9333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SI').update(coordinates=fromstr('POINT (15.0000 46.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SJ').update(coordinates=fromstr('POINT (20.0000 78.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SK').update(coordinates=fromstr('POINT (19.5000 48.6667)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SL').update(coordinates=fromstr('POINT (-11.5000 8.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SM').update(coordinates=fromstr('POINT (12.4167 43.7667)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SN').update(coordinates=fromstr('POINT (-14.0000 14.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SO').update(coordinates=fromstr('POINT (49.0000 10.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SR').update(coordinates=fromstr('POINT (-56.0000 4.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='ST').update(coordinates=fromstr('POINT (7.0000 1.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SV').update(coordinates=fromstr('POINT (-88.9167 13.8333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SY').update(coordinates=fromstr('POINT (38.0000 35.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='SZ').update(coordinates=fromstr('POINT (31.5000 -26.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TC').update(coordinates=fromstr('POINT (-71.5833 21.7500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TD').update(coordinates=fromstr('POINT (19.0000 15.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TF').update(coordinates=fromstr('POINT (67.0000 -43.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TG').update(coordinates=fromstr('POINT (1.1667 8.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TH').update(coordinates=fromstr('POINT (100.0000 15.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TJ').update(coordinates=fromstr('POINT (71.0000 39.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TK').update(coordinates=fromstr('POINT (-172.0000 -9.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TM').update(coordinates=fromstr('POINT (60.0000 40.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TN').update(coordinates=fromstr('POINT (9.0000 34.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TO').update(coordinates=fromstr('POINT (-175.0000 -20.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TR').update(coordinates=fromstr('POINT (35.0000 39.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TT').update(coordinates=fromstr('POINT (-61.0000 11.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TV').update(coordinates=fromstr('POINT (178.0000 -8.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TW').update(coordinates=fromstr('POINT (121.0000 23.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='TZ').update(coordinates=fromstr('POINT (35.0000 -6.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='UA').update(coordinates=fromstr('POINT (32.0000 49.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='UG').update(coordinates=fromstr('POINT (32.0000 1.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='UM').update(coordinates=fromstr('POINT (166.6000 19.2833)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='US').update(coordinates=fromstr('POINT (-97.0000 38.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='UY').update(coordinates=fromstr('POINT (-56.0000 -33.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='UZ').update(coordinates=fromstr('POINT (64.0000 41.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='VA').update(coordinates=fromstr('POINT (12.4500 41.9000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='VC').update(coordinates=fromstr('POINT (-61.2000 13.2500)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='VE').update(coordinates=fromstr('POINT (-66.0000 8.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='VG').update(coordinates=fromstr('POINT (-64.5000 18.5000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='VI').update(coordinates=fromstr('POINT (-64.8333 18.3333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='VN').update(coordinates=fromstr('POINT (106.0000 16.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='VU').update(coordinates=fromstr('POINT (167.0000 -16.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='WF').update(coordinates=fromstr('POINT (-176.2000 -13.3000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='WS').update(coordinates=fromstr('POINT (-172.3333 -13.5833)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='YE').update(coordinates=fromstr('POINT (48.0000 15.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='YT').update(coordinates=fromstr('POINT (45.1667 -12.8333)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='ZA').update(coordinates=fromstr('POINT (24.0000 -29.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='ZM').update(coordinates=fromstr('POINT (30.0000 -15.0000)', srid=4326))
        orm['atlas.Country'].objects.filter(country_code='ZW').update(coordinates=fromstr('POINT (30.0000 -20.0000)', srid=4326))
        
        us_regions = orm['atlas.Region'].objects.filter(country__country_code='US')
        us_regions.filter(code='AK').update(coordinates=fromstr('POINT (-152.2683 61.3850)', srid=4326))
        us_regions.filter(code='AL').update(coordinates=fromstr('POINT (-86.8073 32.7990)', srid=4326))
        us_regions.filter(code='AR').update(coordinates=fromstr('POINT (-92.3809 34.9513)', srid=4326))
        us_regions.filter(code='AS').update(coordinates=fromstr('POINT (-170.7197 14.2417)', srid=4326))
        us_regions.filter(code='AZ').update(coordinates=fromstr('POINT (-111.3877 33.7712)', srid=4326))
        us_regions.filter(code='CA').update(coordinates=fromstr('POINT (-119.7462 36.1700)', srid=4326))
        us_regions.filter(code='CO').update(coordinates=fromstr('POINT (-105.3272 39.0646)', srid=4326))
        us_regions.filter(code='CT').update(coordinates=fromstr('POINT (-72.7622 41.5834)', srid=4326))
        us_regions.filter(code='DC').update(coordinates=fromstr('POINT (-77.0262 38.8964)', srid=4326))
        us_regions.filter(code='DE').update(coordinates=fromstr('POINT (-75.5148 39.3498)', srid=4326))
        us_regions.filter(code='FL').update(coordinates=fromstr('POINT (-81.7170 27.8333)', srid=4326))
        us_regions.filter(code='GA').update(coordinates=fromstr('POINT (-83.6487 32.9866)', srid=4326))
        us_regions.filter(code='HI').update(coordinates=fromstr('POINT (-157.5311 21.1098)', srid=4326))
        us_regions.filter(code='IA').update(coordinates=fromstr('POINT (-93.2140 42.0046)', srid=4326))
        us_regions.filter(code='ID').update(coordinates=fromstr('POINT (-114.5103 44.2394)', srid=4326))
        us_regions.filter(code='IL').update(coordinates=fromstr('POINT (-89.0022 40.3363)', srid=4326))
        us_regions.filter(code='IN').update(coordinates=fromstr('POINT (-86.2604 39.8647)', srid=4326))
        us_regions.filter(code='KS').update(coordinates=fromstr('POINT (-96.8005 38.5111)', srid=4326))
        us_regions.filter(code='KY').update(coordinates=fromstr('POINT (-84.6514 37.6690)', srid=4326))
        us_regions.filter(code='LA').update(coordinates=fromstr('POINT (-91.8749 31.1801)', srid=4326))
        us_regions.filter(code='MA').update(coordinates=fromstr('POINT (-71.5314 42.2373)', srid=4326))
        us_regions.filter(code='MD').update(coordinates=fromstr('POINT (-76.7902 39.0724)', srid=4326))
        us_regions.filter(code='ME').update(coordinates=fromstr('POINT (-69.3977 44.6074)', srid=4326))
        us_regions.filter(code='MI').update(coordinates=fromstr('POINT (-84.5603 43.3504)', srid=4326))
        us_regions.filter(code='MN').update(coordinates=fromstr('POINT (-93.9196 45.7326)', srid=4326))
        us_regions.filter(code='MO').update(coordinates=fromstr('POINT (-92.3020 38.4623)', srid=4326))
        us_regions.filter(code='MP').update(coordinates=fromstr('POINT (145.5505 14.8058)', srid=4326))
        us_regions.filter(code='MS').update(coordinates=fromstr('POINT (-89.6812 32.7673)', srid=4326))
        us_regions.filter(code='MT').update(coordinates=fromstr('POINT (-110.3261 46.9048)', srid=4326))
        us_regions.filter(code='NC').update(coordinates=fromstr('POINT (-79.8431 35.6411)', srid=4326))
        us_regions.filter(code='ND').update(coordinates=fromstr('POINT (-99.7930 47.5362)', srid=4326))
        us_regions.filter(code='NE').update(coordinates=fromstr('POINT (-98.2883 41.1289)', srid=4326))
        us_regions.filter(code='NH').update(coordinates=fromstr('POINT (-71.5653 43.4108)', srid=4326))
        us_regions.filter(code='NJ').update(coordinates=fromstr('POINT (-74.5089 40.3140)', srid=4326))
        us_regions.filter(code='NM').update(coordinates=fromstr('POINT (-106.2371 34.8375)', srid=4326))
        us_regions.filter(code='NV').update(coordinates=fromstr('POINT (-117.1219 38.4199)', srid=4326))
        us_regions.filter(code='NY').update(coordinates=fromstr('POINT (-74.9384 42.1497)', srid=4326))
        us_regions.filter(code='OH').update(coordinates=fromstr('POINT (-82.7755 40.3736)', srid=4326))
        us_regions.filter(code='OK').update(coordinates=fromstr('POINT (-96.9247 35.5376)', srid=4326))
        us_regions.filter(code='OR').update(coordinates=fromstr('POINT (-122.1269 44.5672)', srid=4326))
        us_regions.filter(code='PA').update(coordinates=fromstr('POINT (-77.2640 40.5773)', srid=4326))
        us_regions.filter(code='PR').update(coordinates=fromstr('POINT (-66.3350 18.2766)', srid=4326))
        us_regions.filter(code='RI').update(coordinates=fromstr('POINT (-71.5101 41.6772)', srid=4326))
        us_regions.filter(code='SC').update(coordinates=fromstr('POINT (-80.9066 33.8191)', srid=4326))
        us_regions.filter(code='SD').update(coordinates=fromstr('POINT (-99.4632 44.2853)', srid=4326))
        us_regions.filter(code='TN').update(coordinates=fromstr('POINT (-86.7489 35.7449)', srid=4326))
        us_regions.filter(code='TX').update(coordinates=fromstr('POINT (-97.6475 31.1060)', srid=4326))
        us_regions.filter(code='UT').update(coordinates=fromstr('POINT (-111.8535 40.1135)', srid=4326))
        us_regions.filter(code='VA').update(coordinates=fromstr('POINT (-78.2057 37.7680)', srid=4326))
        us_regions.filter(code='VI').update(coordinates=fromstr('POINT (-64.8199 18.0001)', srid=4326))
        us_regions.filter(code='VT').update(coordinates=fromstr('POINT (-72.7093 44.0407)', srid=4326))
        us_regions.filter(code='WA').update(coordinates=fromstr('POINT (-121.5708 47.3917)', srid=4326))
        us_regions.filter(code='WI').update(coordinates=fromstr('POINT (-89.6385 44.2563)', srid=4326))
        us_regions.filter(code='WV').update(coordinates=fromstr('POINT (-80.9696 38.4680)', srid=4326))
        us_regions.filter(code='WY').update(coordinates=fromstr('POINT (-107.2085 42.7475)', srid=4326))

    def backwards(self, orm):
        orm['atlas.Country'].objects.all().update(coordinates=None)
        orm['atlas.Region'].objects.all().update(coordinates=None)

    models = {
        'atlas.city': {
            'Meta': {'ordering': "('name',)", 'object_name': 'City'},
            'coordinates': ('atlas.fields.CoordinateField', [], {'blank': 'True', 'null': 'True', 'geography': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atlas.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atlas.Region']", 'null': 'True', 'blank': 'True'})
        },
        'atlas.country': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Country'},
            'border': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'blank': 'True', 'null': 'True', 'geography': 'True'}),
            'coordinates': ('atlas.fields.CoordinateField', [], {'blank': 'True', 'null': 'True', 'geography': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'atlas.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atlas.City']"}),
            'coordinates': ('atlas.fields.CoordinateField', [], {'blank': 'True', 'null': 'True', 'geography': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atlas.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photologue.Photo']", 'null': 'True', 'blank': 'True'})
        },
        'atlas.region': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('country', 'code'),)", 'object_name': 'Region'},
            'border': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'blank': 'True', 'null': 'True', 'geography': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'coordinates': ('atlas.fields.CoordinateField', [], {'blank': 'True', 'null': 'True', 'geography': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atlas.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'photologue.photo': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Photo'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_related'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tags': ('photologue.models.TagField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.59999999999999998'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        }
    }

    complete_apps = ['atlas']
    symmetrical = True
