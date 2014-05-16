"""
/***************************************************************************
 SynoptiquesAtlas
                                 A QGIS plugin
 Creation de synoptiques grille ou dynamique pour utiliser dans un atlas
                             -------------------
        begin                : 2012-02-22
        copyright            : (C) 2012 by Experts SIG / Biotope
        email                : dev-qgis@biotope.fr
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


def classFactory(iface):
    # load SynoptiquesAtlas class from file SynoptiquesAtlas
    from synoptiquesatlas import SynoptiquesAtlas
    return SynoptiquesAtlas(iface)

