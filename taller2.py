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

# 2. En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta.
valor_compra = float(input('Digite el valor de la compra: $'))
num = int(input('Digite un número: '))
if (num < 74):
    calcular_descuento = valor_compra * 0.15
    descuento = valor_compra - calcular_descuento
    print(f'Se descuenta ${calcular_descuento} del total de la compra. ')
    print(f'El total a pagar con descuento incluido es de ${descuento}')
else:
    calcular_descuento = valor_compra * 0.2
    descuento = valor_compra - calcular_descuento
    print(f'Se descuenta ${calcular_descuento} del total de la compra. ')
    print(f'El total a pagar con descuento incluido es de ${descuento}')
