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

# 3. Una compañía de seguros está abriendo un departamento de
# finanzas y estableció un programa para captar clientes, que conssite
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La
# afianzadora desea determinar cual será la cuota que debe pagar al
# cliente.
monto = float(input('Digite el monto de la fianza: $'))
if (monto < 50000):
    cuota = monto * 0.03
    total = cuota + monto
    print(f'La cuota será de: ${cuota}')
    print(f'El valor a pagar al cliente es de: ${total}')
else:
    cuota = monto * 0.02
    total = cuota + monto
    print(f'La cuota será de: ${cuota}')
    print(f'El valor a pagar al cliente es de: ${total}')

''' 4. Una fábrica ha sido sometida a un programa de control de
contaminación para lo cual se efectúa una revisión de los puntos de
contaminación generados por la fábrica. El programa de control de
contaminación consiste en medir los puntos que emite la fábrica en
cinco días de una semana y si el promedio es superior a los 170
puntos entonces tendrá la sanción de parar su producción por una
semana y una multa del 50% de las ganancias diarias cuando no se
detiene la producción. Si el promedio obtenido de puntos es de 170 o
menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
desea saber cuanto dinero perderá después de ser sometido a la
revisión.'''
p_lunes = int(input('Digite los puntos emitidos del día lunes:'))
p_martes = int(input('Digite los puntos emitidos del día martes:'))
p_miercoles = int(input('Digite los puntos emitidos del día miércoles:'))
p_jueves = int(input('Digite los puntos emitidos del día jueves:'))
p_viernes = int(input('Digite los puntos emitidos del día viernes:'))
gan_lunes = float(input('Digite las ganancias del día lunes: $'))
gan_martes = float(input('Digite las ganancias del día martes: $'))
gan_miercoles = float(input('Digite las ganancias del día miércoles: $'))
gan_jueves = float(input('Digite las ganancias del día jueves: $'))
gan_viernes = float(input('Digite las ganancias del día viernes: $'))
promedio = (p_lunes + p_martes + p_miercoles + p_jueves + p_viernes)/5
ganancias = gan_lunes + gan_martes + gan_miercoles + gan_jueves + gan_viernes
if (promedio > 170):
    print('El promedio de puntos de la semana es de: ', promedio)
    print('El promedio de los puntos es mayor a 170, debe parar la producción')
    multa = ganancias * 0.5
    print(f'La ganancia total de la semana es de: ${ganancias}')
    print('La multa por no parar producción es de: $', ganancias-multa)
else:
    print('¡No recibe multa!')
    print(f'La ganancia total de la semana es de: ${ganancias}')
