# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:28:30 2022

@author: Nanquen
"""
# Dado el total, calcular el IGV y el SUBTOTAL

import financieros

total = 1000.49
print(f"Subtotal: {financieros.obtenerSubtotalconTotal(total):.2f}")
print(f"IGV: {financieros.obtenerIGVconTotal(total):.2f}")
print(f"Total: {total}")
