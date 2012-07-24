#!/bin/bash
#./bin/foundrydemo loaddata ./src/django-locations/locations/fixtures/countries.json
for i in {1..32}
do
   ./bin/foundrydemo loaddata ./src/django-locations/locations/fixtures/cities_$i.json
   echo $i
done