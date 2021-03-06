# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QuickApi
                                 A QGIS plugin
 This plugin balbla
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-06-12
        copyright            : (C) 2019 by bla
        email                : abl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCursor, QPixmap
from PyQt5.QtWidgets import QApplication

from qgis.gui import QgsMapToolEmitPoint, QgsVertexMarker
from qgis.core import (QgsCoordinateReferenceSystem,
                       QgsCoordinateTransform,
                       QgsProject
                       )

class PointTool(QgsMapToolEmitPoint):
    """Point Map tool to capture mapped coordinates."""

    def __init__(self, canvas):
        """
        :param canvas: current map canvas
        :type: QgsMapCanvas
        """

        QgsMapToolEmitPoint.__init__(self, canvas)
        self.canvas = canvas
        self.cursor = QCursor(QPixmap(':/plugins/quick_api/icons/icon_locate.png').scaledToWidth(48))

    canvasClicked = pyqtSignal('QgsPointXY')
    def canvasReleaseEvent(self, event):
        # Get the click and emit a transformed point

        crs_canvas = self.canvas.mapSettings().destinationCrs()

        point_canvas_crs = event.mapPoint()

        wgs = QgsCoordinateReferenceSystem(4326)
        xformer = QgsCoordinateTransform(crs_canvas, wgs, QgsProject.instance())

        point_wgs = xformer.transform(point_canvas_crs)

        self.canvasClicked.emit(point_wgs)

    def activate(self):
        QApplication.setOverrideCursor(self.cursor)