# -*- coding: utf-8 -*-
"""
@author: Sebastian Bárcenas
"""
from random import randint

#1

def add(lista):
    sum = 0
    for i in lista:
        sum = sum + i
    return sum

camisas = int(input("Número de camisas a comprar: "))
count = 0
data = []
for i in range(camisas):
    count += 1
    valor = int(input(f"Ingrese el precio de la camisa {count}: $"))
    data.append(valor)
    
total = add(data)
if camisas >=3:
    total *= 0.7
    print(f"El total de la compra es: ${total}")
else:
    total *= 0.9
    print()
    print(f"El total de la compra es: ${total}")
    
    
"""2. En un supermercado se hace una promoción, mediante la cual el
cliente obtiene un descuento dependiendo de un número que se
escoge al azar. Si el número escogido es menor que 74 el descuento
es del 15% sobre el total de la compra, si es mayor o igual a 74 el
descuento es del 20%. Obtener cuanto dinero se le descuenta."""
    
valor_compra = int(input('Valor de la compra: $'))
aleatorio = randint(0,100)
print(f"Su numero aleatorio es: {aleatorio}")
if aleatorio < 74:
    valor_compra *= 0.85
else:
    valor_compra *= 0.80
    
print(f"Su descuento fue de: ${valor_compra}")


"""3. Una compañía de seguros está abriendo un departamento de
finanzas y estableció un programa para captar clientes, que conssite
en lo siguiente: Si el monto por el que se efectúa la fianza es menor
que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
es mayor que $50.000 la cuota a pagar será el 2% del monto. La
afianzadora desea determinar cual será la cuota que debe pagar al
cliente."""

fianza = int(input('Monto de la fianza: $'))
if fianza < 50000:
    cuota = fianza*0.03
else:
    cuota = fianza*0.02
print(f'La cuota a pagar es de: ${cuota}')


#4


listay = []
for i in range(5):
    puntos = int(input(f'Indique los puntos medidos del dia {i}: '))
    listay.append(puntos)
suma4 = add(listay)
promedio = suma4/5
if promedio > 170:
    print('Debe cerar por una semana a demas de una multa del 50% de las ganancias diarias')
else:
    print('No debe ser sancionado')
    

# 6

computadoras = int(input('Ingrese el número de computadoras que comprará: '))
listaz = []
contador = 0
for i in range(computadoras):
    contador += 1
    valor_computadora = int(input(f'Ingrese el precio de la computadora {contador}: $'))
    listaz.append(valor_computadora)
precio_total_computadoras = add(listaz)
if computadoras < 5:
    precio_total_computadoras *= 0.9
    print(f"El total con el 10% de descuento es: {precio_total_computadoras}")
elif computadoras >= 5 and computadoras < 10:
    precio_total_computadoras *= 0.8
    print(f"El total con el 20% de descuento es: {precio_total_computadoras}")
else:
    precio_total_computadoras *= 0.6
    print(f"El total con el 40% de descuento es: {precio_total_computadoras}")
    

# 7

precio_con_iva = int(input('Ingrese el precio del producto: $'))
marca = input('Ingrese el precio del producto: $')
marca.upper()
precio_sin_iva = precio_con_iva / 1.19
if precio_con_iva >= 2000 and marca == 'NOSY':
    precio_sin_iva = *0.85
    total_con_iva = (precio_sin_iva*0.16)+precio_sin_iva
    print(f'El precio total con descuento es: {total_con_iva}')
elif precio_con_iva >= 2000:
    precio_sin_iva = *0.80
    total_con_iva = (precio_sin_iva*0.16)+precio_sin_iva
    print(f'El precio total con descuento es: {total_con_iva}')
    
# 8

piezas = int(input('Ingrese el numero de piezas a comprar: '))
valor_pieza = int(input('Ingrese el valor de cada pieza a comprar: $'))
total_compra = piezas * valor_pieza
if total_compra > 500000:
    capacidad_de_invertir = total_compra * 0.55
    prestamo_banco = total_compra * 0.3
    valor_credito = total_compra * 0.15
    intereses = valor_credito * 0.2
    print(f'La cantidad a invertir será de: ${capacidad_de_invertir}, con un prestamo al banco de: ${prestamo_banco} y un crédito al fabricante de: ${valor_credito} con intereses de: ${intereses}')
    
else:
    capacidad_de_invertir = total_compra * 0.7
    valor_credito = total_compra * 0.3
    intereses = valor_credito * 0.2
    print(f'La cantidad a invertir será de: ${capacidad_de_invertir} y un crédito al fabricante de: ${valor_credito} con intereses de: ${intereses}')


# 9

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
if num1 == num2:
    respuesta = num1 * num2
elif num1 > num2:
    respuesta = num1 - num2
elif num1 < num2:
    respuesta = num1 + num2
print(respuesta)

"""10. Leer tres números diferentes e imprimir el número mayor de los
tres"""
listaw = []
for i in range(3):
    numero = int(input(f'Ingrese el número deseado: '))
    listaw.append(numero)
mayor = max(listaw)
print('')
print(f'El número mayor de los 3 es: {mayor}')
    