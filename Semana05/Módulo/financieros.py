# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:15:31 2022

@author: Nanquen
Los Módulos te permiten crear librerías de funcionalidades
que puedas utilizar o reutilizar en cualquier momento en tu proyecto.
"""
igv = 0.18
def obtenerIGVconSubTotal(subtotal):
    return subtotal*igv

def obternerTotalconSubTotal(subtotal):
    # subtotal + igv*subtotal
    # subtotal * (1+0.18)
    return subtotal*(1+igv)
# y porque no poner 1.18?
# Porque si hago cambios solo necesitaria cambiar una línea

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)


