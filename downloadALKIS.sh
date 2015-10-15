#!/bin/sh

echo "Download and unzip ALKIS files"

Folder='/home/esteban/workspace/PostgreSQL/DownloadsTemp/'
mkdir -p $Folder

Base='http://daten-hamburg.de/geographie_geologie_geobasisdaten/ALKIS_Liegenschaftskarte/ALKIS_Liegenschaftskarte_ausgewaehlteDaten_'

for var in "HH_2015-08-03.zip" #"HH_2015-04-04.zip" "HH_2015-01-03.zip" #"HH_2014-11-19.zip" "HH_2014-06-14.zip" 
do
    if [ -f  $Folder$var ]; then
        echo "File on disk " $var
    else
        echo "Downloading " $var
        wget -O $Folder$var $Base$var
    fi
done

echo "unzip files"
for var in "HH_2015-08-03.zip" #"HH_2015-04-04.zip" "HH_2015-01-03.zip" #"HH_2014-11-19.zip" "HH_2014-06-14.zip" 
do
    if [ -f $Folder${var%.*} ]; then
        echo "Unziped files at " $Folder${var%.*}
    else
        echo "Unziping file"
        unzip -u -d $Folder${var%.*} $Folder$var
    fi
done

echo "populate postgreSQL"
# using EPSG:5555
# http://www.epsg-registry.org/export.htm?gml=urn:ogc:def:crs:EPSG::5555

for var in "HH_2015-08-03.zip" #"HH_2015-04-04.zip" "HH_2015-01-03.zip" #"HH_2014-11-19.zip" "HH_2014-06-14.zip" 
do
    for file in $Folder${var%.*}/*.xml
    do
        if [ -f $Folder${var%.*}/*.shp ]; then
            echo "shapefile exists"
        else
            ogr2ogr -f "ESRI Shapefile" ${file%.*}.shp $file
        fi
        #ogr2ogr -update -append -f "PostgreSQL" -a_srs "EPSG:5555" PG:"dbname=alkis2015 user=esteban password=esteban" $file
        ogr2ogr -append -f "PostgreSQL" PG:"dbname=alkis2015 user=esteban password=esteban" ${file%.*}.shp
        echo $file
    done
done
