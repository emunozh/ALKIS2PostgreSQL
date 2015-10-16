#!/usr/bin/env python2
# encoding: utf-8
"""
#Created by Esteban.

Do 15 Okt 2015 17:29:45 CEST

"""

from osgeo import ogr
import ogr2ogr
from os import path
import os
ROOT = "./DownloadsTemp/HH_2015-08-03/"


def transform(outFile, inFile, engine="ESRI Shapefile"):
    """Transfor a file using ogr2ogr."""
    # from: https://gis.stackexchange.com/questions/39080/
    #       gishow-do-i-use-ogr2ogr-to-convert-a-gml-to-shapefile-in-python/
    #       41637#41637
    # note: main is expecting sys.argv, where the first argument is the script
    # name so, the argument indices in the array need to be offset by 1
    ogr2ogr.main(["", "-f", engine, outFile, inFile])


def getLayer(inFile, layer, engine="GML"):
    """get a layer from a gml file."""
    inDriver = ogr.GetDriverByName(engine)
    inDataSource = inDriver.Open(inFile, 0)
    inLayer = inDataSource.GetLayer(layer)
    return inLayer


def getLayerSHP(inFile, layer):
    """get the right shp file out of a folder."""
    fileList = os.listdir(inFile)
    for file in fileList:
        if file.endswith(".shp") and layer in file:
            return file


def getFiles(fileStartsWith="ALKIS", fileEndsWith=".xml"):
    """find all xml files."""
    fileList = os.listdir(ROOT)

    for file in sorted(fileList):
        if file.startswith(fileStartsWith) and file.endswith(fileEndsWith):
            yield(path.join(ROOT, file))


def newFile(outFile, engine="GeoJSON", geometryType=ogr.wkbMultiPolygon):
    """Created a new file."""

    outputMergefn = os.path.join(ROOT, outFile)
    geometryType = ogr.wkbMultiPolygon

    out_driver = ogr.GetDriverByName(engine)
    if os.path.exists(outputMergefn):
        out_driver.DeleteDataSource(outputMergefn)
    out_ds = out_driver.CreateDataSource(outputMergefn)
    out_layer = out_ds.CreateLayer(outputMergefn, geom_type=geometryType)

    return out_layer


def populateFile(out_layer, layer):
    """populate a new file with an ogr layer."""
    for feat in layer:
        print(feat)
        out_feat = ogr.Feature(out_layer.GetLayerDefn())
        out_feat.SetGeometry(feat.GetGeometryRef().Clone())
        out_layer.CreateFeature(out_feat)
        out_layer.SyncToDisk()
    return out_layer


def main4():
    inFile = path.join(ROOT, "ALKIS_HH_0014.xml")
    outFile = ".{}.tmp".format(inFile.split(".")[1])
    if not os.path.exists(outFile):
        transform(outFile, inFile)
    searchLayer = "AX_Gebaeude"
    mergeFile = getLayerSHP(outFile, searchLayer)
    mergeFile = path.join(outFile, mergeFile)
    print(mergeFile)
    shpNewFile = newFile(
        "{}.shp".format(searchLayer),
        engine="ESRI Shapefile", geometryType=ogr.wkbMultiPolygon)
    ds = ogr.Open(mergeFile)
    lyr = ds.GetLayer()
    print(lyr)
    shpNewFile = populateFile(shpNewFile, lyr)


def main3():
    searchLayer = "AX_Gebaeude"
    xmlFiles = getFiles()
    geoJSON = newFile("{}.json".format(searchLayer))
    for xmlFile in xmlFiles:
        try:
            layer = getLayer(xmlFile, searchLayer)
            if layer:
                print("OK\t{}".format(xmlFile))
                geoJSON = populateFile(geoJSON, layer)
            else:
                print("NO\t{}".format(xmlFile))
        except:
            print("ERROR\t{}".format(xmlFile))


def main2():
    inFile = path.join(ROOT, "ALKIS_HH_0014.xml")
    #layer = "AX_Gebaeude"
    layer = "AX_Baublock"
    newLayer = getLayer(inFile, layer)
    n = newLayer.GetFeatureCount()
    print(n)
    print(newLayer)


def main():
    engine = "GeoJSON"
    outFile = "ALKIS_HH_0014.json"
    inFile = path.join(ROOT, "ALKIS_HH_0014.xml")
    transform(outFile, inFile, engine=engine)


if __name__ == "__main__":
    main4()
