# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:36:12 2022

@author: user
"""

archivo = open("archivo_de_prueba.txt", "wt")
contenido = "Línea1 hola amigos como están?\nLínea2 Bienvenido a la UNTELS."
archivo.write(contenido)
archivo.close()