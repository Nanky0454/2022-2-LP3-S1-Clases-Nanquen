# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:53:38 2022

@author: user
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor =  conexion.cursor()

consulta = """ UPDATE EDITORIAL
                SET
                    NOMBRE = 'Editorial Imprenta Unión'
                WHERE
                    IDEDITORIAL = 1

"""

cursor.execute(consulta)
conexion.commit()
conexion.close()
