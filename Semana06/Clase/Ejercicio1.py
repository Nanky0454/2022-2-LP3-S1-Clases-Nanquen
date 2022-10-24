# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Es un ejercicio clásico, tenemos una cadena llamada nombre
# y se desea que se muestre en formato título

# Importamos la librería
import camelcase

nombre = "piero alonso nanquen castillo"

print(nombre.upper())
print(nombre.title())

# Cremos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con Camelcase...")

# Imprimimos el nombre en formato tíyulo utilizamos cam.hump()
print(cam.hump(nombre))

# Que pasaría si ahora el problema pidiera que el 
# nombre de piero y castillo no se muestre en el formato título

cam2 = camelcase.CamelCase('piero','castillo')
print(cam2.hump(nombre))