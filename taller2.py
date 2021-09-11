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

# 5 Comprar automovil o terreno
costo = float(input('Digite el valor del automóvil/Terreno: $'))
devaluacion = float(input('Digite la devaluación del automóvil al año: $'))
incremento = float(input('Digite el incremento del terreno al año: $'))
devaluacion_auto = costo - (devaluacion * 3)
incremento_terr = costo + (incremento * 3)
mitad_incre = incremento_terr / 2
if (devaluacion_auto < mitad_incre):
    print('Comprar automóvil!')
else:
    print('NO comprar automóvil!')

# 6 Fabrica de Computadoras
n_pc = int(input('Digite el número de computadoras a comprar: '))
total_sin_descuento = n_pc * 11000
if (n_pc < 5):
    descuento = total_sin_descuento - (total_sin_descuento * 0.1)
    print(f'El total a pagar por las {n_pc} computadoras es de: ${descuento}')
elif (n_pc >= 5 and n_pc < 10):
    descuento = total_sin_descuento - (total_sin_descuento * 0.2)
    print(f'El total a pagar por las {n_pc} computadoras es de: ${descuento}')
else:
    descuento = total_sin_descuento - (total_sin_descuento * 0.4)
    print(f'El total a pagar por las {n_pc} computadoras es de: ${descuento}')

# 7 Proveedor de estéreos
costo = float(input('Digite el costo del aparato: $'))
marca = input('Digite el nombre de la marca: ')
if (costo >= 2000 and marca == "NOSY"):
    costo_sin_iva = costo - (costo * 0.1)
    iva = (costo_sin_iva * 0.16) + costo_sin_iva
    desc_marca_nosy = iva - (iva * 0.05)
    print(f'valor total a pagar por el aparato marca NOSY: ${desc_marca_nosy}')
elif (costo >= 2000 and marca != "NOSY"):
    costo_sin_iva = costo - (costo * 0.1)
    iva = (costo_sin_iva * 0.16) + costo_sin_iva
    print(f'valor total a pagar por el aparato de marca {marca}: ${iva}')
elif (costo < 2000 and marca == "NOSY"):
    iva = (costo * 0.16) + costo
    desc_marca_nosy = iva - (iva * 0.05)
    print(f'valor total a pagar por el aparato marca NOSY: ${desc_marca_nosy}')
elif (costo < 2000 and marca != "NOSY"):
    iva = (costo * 0.16) + costo
    print(f'valor total a pagar por el aparato de marca {marca}: ${iva}')

# 8 Compra de piezas a fábrica de refacciones
compra = float(input('Digite el monto total de la compra: $'))
if (compra > 500000):
    inversion = compra * 0.55
    prestamo = compra * 0.30
    credito = compra * 0.15
    intereses = credito * 0.20
    print(f'Cantidad a invertir: ${inversion}')
    print(f'Valor del préstamo: ${prestamo}')
    print(f'Valor del crédito: ${credito}')
    print(f'Intereses: ${intereses}')
else:
    inversion = compra * 0.70
    credito = compra * 0.30
    intereses = credito * 0.20
    print(f'Cantidad a invertir: ${inversion}')
    print(f'Valor del crédito: ${credito}')
    print(f'Intereses: ${intereses}')

# 9 Leer 2 numeros
n1 = int(input('Digite el primer número: '))
n2 = int(input('Digite el segundo número: '))
if (n1 == n2):
    multiplicacion = n1 * n2
    print('El resultado de la multiplicación es: ', multiplicacion)
elif (n1 > n2):
    resta = n1 - n2
    print('El resultado dela resta es: ', resta)
else:
    suma = n1 + n2
    print('El resultado de la suma es: ', suma)

# 10 Imprimir el numero mayor
n1 = int(input('Digite el primer número: '))
n2 = int(input('Digite el segundo número: '))
n3 = int(input('Digite el tercer número: '))
if (n1 > n2 and n1 > n3):
    print('El mayor es: ', n1)
elif (n1 < n2 and n2 > n3):
    print('El mayor es: ', n2)
elif (n1 < n3 and n2 < n3):
    print('El mayor es: ', n3)
