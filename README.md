# ALKIS2PostgreSQL
Helpful scripts to work with ALKIS data on a PostgreSQL server

(1) `downloadALKIS.sh` is shell script to download the ALKIS data end populate
a predefine PostgreSQL database with the ALKIS data. The script makes use of
the [ogr2ogr](http://www.gdal.org/ogr2ogr.html) command to transform the `gml`
data and populate the PostgreSQL database.
