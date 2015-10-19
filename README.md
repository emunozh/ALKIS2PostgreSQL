# ALKIS2PostgreSQL
Helpful scripts to work with ALKIS data on a PostgreSQL server

[(1)](https://github.com/emunozh/ALKIS2PostgreSQL/blob/master/downloadALKIS.sh)
`downloadALKIS.sh` is shell script to download the ALKIS data end populate a
predefine PostgreSQL database with the ALKIS data. The script makes use of the
[ogr2ogr](http://www.gdal.org/ogr2ogr.html) command to transform the `gml` data
and populate the PostgreSQL database.

![Screenshot](https://github.com/emunozh/ALKIS2PostgreSQL/blob/master/Screenshot.png)

[(2)](https://github.com/emunozh/ALKIS2PostgreSQL/blob/master/migrateALKIS.py)
`migrateALKIS.py` is a python script to migrate the ALKIS `gml` data to other
formats using the [osgeo](http://gdal.org/python/) library. 

[(3)](https://github.com/emunozh/ALKIS2PostgreSQL/blob/master/qgis.py)
`qgis.py` a small script to load specific layers on qgis.
