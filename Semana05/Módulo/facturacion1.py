# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:21:12 2022

@author: Nanquen
"""

# Dado el subtotal, calcular el IGV y el TOTAL

import financieros
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV:  {financieros.obtenerIGVconSubTotal(subtotal):.2f}")
print(f"Total: {financieros.obternerTotalconSubTotal(subtotal):.2f}")
