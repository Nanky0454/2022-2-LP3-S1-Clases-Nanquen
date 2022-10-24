# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:43:53 2022

@author: user
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()

consulta ="""SELECT *
             FROM LIBRO
             WHERE
                 precio>=55
             ORDER BY titulo
"""

cursor.execute(consulta)
libros = cursor.fetchall()

# Acá libros es una lista... entonces utilizamos
for libro in libros:
    print(libro)
    
conexion.close()