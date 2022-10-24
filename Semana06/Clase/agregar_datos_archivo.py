# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:30:08 2022

@author: user
"""

archivo = open("noticia.txt", "at")
contenido = "\nFuente :RPP"

archivo.write(contenido)
archivo.close()