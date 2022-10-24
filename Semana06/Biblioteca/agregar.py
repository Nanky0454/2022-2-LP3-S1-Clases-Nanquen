# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:01:00 2022

@author: user
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")

consulta = """ INSERT INTO
               PAIS (NOMBRE, ESTADO)
               VALUES('Brasil','A')
"""

cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()

conexion.close()