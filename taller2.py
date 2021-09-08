#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 09:53:11 2021

@author: ivandavid
"""

# 1. Hacer un algoritmo que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# del 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.
n_camisas = int(input('Digite el número de camisetas compradas: '))
valor_camisas = float(input('Digite el valor de la camiseta: '))
if (n_camisas >= 3):
    total_sin_descuento = ((n_camisas * valor_camisas) * 0.3)
    descuento = (n_camisas * valor_camisas)-total_sin_descuento
    print(f'El total a pagar por las {n_camisas} es de ${descuento} ')
else:
    total_sin_descuento = (n_camisas * valor_camisas) * 0.1
    descuento = (n_camisas * valor_camisas)-total_sin_descuento
    print(f'El total a pagar por las {n_camisas} es de ${descuento} ')
