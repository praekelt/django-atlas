Changelog
=========

0.1
---
#. Django 1.6 compatibility.
#. Prepare test framework. Actual tests are not implemented yet.

0.0.4-beta (09-05-2013)
-----------------------
#. Better error messages if locating the request fails on /set-location/.
#. Use http/https depending on current connection to get Google Maps javascript.

0.0.3-beta (20-02-2013)
-----------------------
#. Ajax POST to `/set-location/` rather than GET. Better semantics and it avoids browser caching issue.

0.0.2-beta (08-11-2012)
-----------------------
#. Remove dependency on JQuery.
#. Make location selection form easily overrideable.
#. Fix location_required decorator so that it is chainable.

0.0.1-beta
----------
#. Initial release.
