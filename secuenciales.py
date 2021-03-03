# -*- coding: utf-8 -*-
"""
@author: Sebastian Bárcenas
"""

# 1

def add(lista):
    total = 0
    for i in lista:
        total = total + i
    return total

data = []

count = 0
for i in range(3):
    count += 1
    inversor = int(input(f'Capital invertido por el inversor {count}: $'))
    data.append(inversor)

totalc = sum(data)
contador = 0
for i in data:
    contador += 1
    pactual = (i*100)/totalc
    print(f'El porcentaje que corresponde al inversor {contador} es del {pactual:.2f}%')
    # Se truncan los valores con 2 decimales para obtener numeros legibles
    
    
# 2

base = int(input('Ingrese el sueldo base del empleado: $'))
nHijos = int(input('Ingrese número de hijos del empleado: '))
bonificacion = 80000 * nHijos
total = base + bonificacion
print(f'El monto total a pagar es: ${total}')

# 3

dato_entrada = int(input('Ingrese el saldo inicial a ahorrar: $'))
total_salida = (dato_entrada * 0.015) + dato_entrada
print(f'El saldo final del ahorrado mas sus intereses es de: ${total_salida}')


# 4 

m2 = int(input('Ingrese los metros cuadrados (m2) a comprar: '))
total = m2 * 80000
cuota_inicial = total * 0.35
cuotas = (total - cuota_inicial)/12
print(f'Para {m2} metros cuadrados el valor a pagar por cuota inicial es de: ${cuota_inicial}, y las 12 cuotas son de: ${cuotas}')


# 5

sueldo = int(input('Ingrese el sueldo base: $'))
politica_publica = sueldo * 0.01
seguro_social = sueldo * 0.04
seguro_forzoso = sueldo * 0.005
caja_ahorro = sueldo * 0.05
total_trabajador = sueldo - seguro_forzoso - seguro_social - caja_ahorro - politica_publica

print(f'El descuento por seguro social es de: ${seguro_social}')
print(f'El descuento por ley de politica pública es de: ${politica_publica}')
print(f'El descuento por seguro forzoso es de: ${seguro_forzoso}')
print(f'El descuento por caja de ahorro es de: ${caja_ahorro}')
print(f'El monto total a pagar es: ${total_trabajador}')


# 6

words = int(input('Ingrese el número de palabras que tendrá el aviso: '))
centimetros = int(input('Ingrese el tamaño(cm): '))
color = int(input('Ingrese el número de colores: '))
total = (words * 20000) + (color * 15000) + (centimetros * 25000)
print(f'El monto a pagar por el aviso clasificado es: ${total}')


# 7

antiguedad = int(input('Ingrese la antiguedad del empleado en años: '))
bono = ((antiguedad - 1) * 120000) + 100000
print(f'El total del bono es: ${bono}')


# 8

hours = int(input('Ingrese el número de horas trabajadas: '))
salary = (hours * 20000)
discount = salary * 0.05
salario_con_descuento = salary - discount
print(f'El salario del profesor es ${salario_con_descuento} y su descuento es ${discount}')


# 9

monto_inicial = int(input('Ingrese el monto inicial de la tarjeta: $'))
monto_final = int(input('Ingrese el monto final de la tarjeta: $'))
monto_consumido = (monto_inicial - monto_final)
costo_llamada = (monto_consumido * 0.2) + monto_consumido
print(f'El costo de la llamada es: ${costo_llamada}')

# 10

fotos = int(input('Ingrese el número de fotos a revelar: '))
rev_price = fotos * 1500
total_revelado = (rev_price * 0.16) + rev_price
print(f'Para revelar {fotos} se debe pagar ${total_revelado}')


# 11

presupuesto_anual = int(input('Ingrese el presupuesto de este año: $'))
ginecologia = presupuesto_anual * 0.4
traumatologia = presupuesto_anual * 0.3
pediatria = presupuesto_anual * 0.3

print(f'La cantidad de dinero para ginecologia es de: ${ginecologia}')
print(f'La cantidad de dinero para traumatologia es de: ${traumatologia}')
print(f'La cantidad de dinero para pediatria es de: ${pediatria}')


# 12

peliculas_alquiladas = int(input('Ingrese el número de peliculas alquiladas: '))
dias_alquiler = int(input('Ingrese el número de dias de alquiler: '))
monto_alquiler = (peliculas_alquiladas - 1) * (dias_alquiler * 1500)
print(f'El monto a pagar por las {peliculas_alquiladas} peliculas es de: ${monto_alquiler}')


# 13

personas_viaje = int(input('Ingrese el número de personas que van a viajar: '))
costo_tour = personas_viaje * 25000
total_viaje = (costo_tour * 0.12) + costo_tour
print(f'El monto a pagar por el tour para las {personas_viaje} es de: ${total_viaje}')


# 14

dias_estadia = int(input('Ingrese el número de dias de estadia: '))
total_habitacion = ((dias_estadia - 1) * 200000) + 100000
print(f'El valor total a pagar por la habitacion es de: ${total_habitacion}')



# 15


prestamo = int(input('Ingrese valor del prestamo: $'))
intereses = prestamo * 0.24
total_pagar = prestamo + intereses
mitad_prestamo = total_pagar / 2
cuotas_especiales = mitad_prestamo / 4
cuotas_ordinarias = mitad_prestamo / 20
print(f'El Total a pagar es ${total_pagar}')
print(f'Cada cuota especial es ${cuotas_especiales}')
print(f'Cadaada cuota ordinaria es ${cuotas_ordinarias}')














