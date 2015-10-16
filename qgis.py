#!/usr/bin/env python
# encoding: utf-8
"""
#Created by Esteban
based on email communication with Ivan Dochev

Fr 16 Okt 2015 10:16:49 CEST

Just paste this in the QGIS python window and change the last line
according to the folder (path to the folder) where the XMLs are located,
then the layer that you want (AX_Gebaeude, AX_Geoferen..., usw) and the
type - point,polyline,polygon, table
"""

from glob import glob
from os import path


def load_XMLs(XML_path, Layername, Layertype):
    # A list with the paths to the XMLs
    xmls = glob(path.join(XML_path, "*.xml"))

    for xml in xmls:
        # the |layername gets the sublist
        layer = iface.addVectorLayer(xml +
                                     "|layername=" + Layername +
                                     "|geometrytype=" + Layertype,
                                     "XML_layer: " + str(xmls.index(xml)),
                                     "ogr")
        if not layer:
            print("Layer failed to load!")

# Change these for specifics
load_XMLs("D:\HiwiGEWISS\ALKIS\ALKIS_TEST",
          "AX_LagebezeichnungMitHausnummer",
          "Table")
