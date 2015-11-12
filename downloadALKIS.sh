#!/bin/sh

echo "Download and unzip ALKIS files"

Folder='/home/esteban/workspace/PostgreSQL/DownloadsTemp/'
mkdir -p $Folder

Base='http://daten-hamburg.de/geographie_geologie_geobasisdaten/ALKIS_Liegenschaftskarte/ALKIS_Liegenschaftskarte_ausgewaehlteDaten_'
DataFiles=("HH_2015-10-03.zip") #"HH_2015-08-03.zip" #"HH_2015-04-04.zip" "HH_2015-01-03.zip" "HH_2014-11-19.zip" "HH_2014-06-14.zip" 

for var in "${DataFiles[@]}"; do
    if [ -f  $Folder$var ]; then
        echo "File on disk " $var
    else
        echo "Downloading " $var
        wget -O $Folder$var $Base$var
    fi
done

echo "unzip files"
for var in "${DataFiles[@]}"; do
    if [ -f $Folder${var%.*} ]; then
        echo "Unziped files at " $Folder${var%.*}
    else
        echo "Unziping file"
        unzip -u -d $Folder${var%.*} $Folder$var
    fi
done

echo "populate postgreSQL"
for var in "${DataFiles[@]}"; do
    for file in $Folder${var%.*}/*.xml
    do
        if [ -f $Folder${var%.*} ]; then
            echo "shapefile exists"
        else
            ogr2ogr -skipfailures -f "ESRI Shapefile" ${file%.*} $file
        fi
        for shape in ${file%.*}/*.shp
        do
            ogr2ogr -update -append -skipfailures -progress -f "PostgreSQL" PG:"dbname=alkis2015 user=esteban password=esteban" $shape
        done
        echo $file
    done
done
