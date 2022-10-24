# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:48:01 2022

@author: user
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor =  conexion.cursor()

consulta = """ DELETE FROM EDITORIAL
                WHERE 
                IDEDITORIAL = 5 
"""

cursor.execute(consulta)
conexion.commit()
conexion.close()