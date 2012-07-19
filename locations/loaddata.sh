#!/bin/bash
for i in {19..31}
do
   ./bin/foundrydemo loaddata ./src/django-locations/locations/fixtures/cities_$i.json
done