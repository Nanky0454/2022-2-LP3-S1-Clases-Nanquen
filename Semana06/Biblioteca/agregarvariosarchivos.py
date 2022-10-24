# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:10:52 2022

@author: user
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")

lista_autores= [('Flor Cerdán', '25/10/1975'),
                ('Daniel Lévano', '17/01/1980'),
                ('Omar Peña', '15/10/1978'),
                ('César Zapata', '15/10/1960')]

lista_editoriales= [('EIU','A'),
                    ('Macro','A'),
                    ('Bosh','A'),
                    ('Lima Sur','A'),
                    ('Pirámide','A'),
                    ('Colombus','A'),
                    ('Centros','A')]

lista_paises=[('Perú','A'),
              ('Argentina','A'),
              ('Colombia','A'),
              ('Venezuela','A'),
              ('Uruguay','A'),
              ('Paraguay','A'),
              ('USA','A')]

lista_libros=[('Oracle 11g', 10, 2019, 50, 'A', 2, 1, 1),
              ('Sistemas Operativos', 14, 2016, 59, 'A', 2, 4, 3),
              ('Estructura de Datos', 6, 2018, 20, 'A', 3, 2, 3),
              ('Algoritmos con Python', 8, 2017, 70, 'A', 3, 2, 1),
              ('BI', 6, 1998, 50, 'A', 2, 4, 2),
              ('Ing. de Software', 9, 2000, 56, 'A', 4, 2, 4),
              ('Organización de PC', 9, 2016, 60, 'A', 8, 2, 1),
              ('Ensamblaje', 9, 2018, 50, 'A', 5, 4, 3)]

consulta_pais="""INSERT INTO
                 PAIS(NOMBRE, ESTADO)
                 VALUES(?,?)
"""
consulta_editorial="""INSERT INTO
                      EDITORIAL(NOMBRE, ESTADO)
                      VALUES(?,?)
"""

consulta_autor="""INSERT INTO
                  AUTOR(NOMBRE, F_NACIMIENTO)
                  VALUES(?,?)
"""

consulta_libro="""INSERT INTO
                   LIBRO(TITULO, CANTIDAD, ANIO, PRECIO, ESTADO, IDPAIS, IDEDITORIAL, IDAUTOR)
                   VALUES(?, ?, ?, ?, ?, ?, ?, ?)
"""

cursor = conexion.cursor()
cursor.executemany(consulta_pais,lista_paises)
cursor.executemany(consulta_editorial,lista_editoriales)
cursor.executemany(consulta_autor,lista_autores)
cursor.executemany(consulta_libro,lista_libros)

conexion.commit()

conexion.close()