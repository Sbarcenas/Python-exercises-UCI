# -*- coding: utf-8 -*-
"""
@author: Sebastian Bárcenas
"""

# 1.

llantas_a_comprar = int(input('Número de llantas a comprar: '))
# Valores por cantidad
five = 300
five_ten = 250
ten = 200

if llantas_a_comprar < 5:
    # Calculo precio total para cantidades menores a 5 llantas
    total = llantas_a_comprar * five
    print(f'Precio por unidad para {llantas_a_comprar} llantas es: ${five}')
    print(f'El total para {llantas_a_comprar} llantas es: ${total}')
    
elif llantas_a_comprar >= 5 and llantas_a_comprar <= 10:
    total = llantas_a_comprar * five_ten
    # Calculo precio total para cantidades entre 5 y 10
    print(f'Precio por unidad para {llantas_a_comprar} llantas es: ${five_ten}')
    print(f'El total para {llantas_a_comprar} llantas es: ${total}')
    
elif llantas_a_comprar > 10:
    # C alculo precio total para cantidades mayores a 5 llantas
    total = llantas_a_comprar * ten
    print(f'Precio por unidad para {llantas_a_comprar} llantas es: ${ten}')
    print(f'El total para {llantas_a_comprar} llantas es: ${total}')



# 2.

price = int(input('Precio total de los televisores: $'))
cedula = input('Ultimos digitos de su cedula: ')

if cedula == '01':
    final = price * 0.9
    print(f'El total con descuento a la cc terminana en {cedula} es ${final}')

elif cedula == '25':
    final = price * 0.8
    print(f'El total con descuento a la cc terminana en {cedula} es ${final}')
    
elif cedula == '44':
    final = price * 0.65
    print(f'El total con descuento a la cc terminana en {cedula} es ${final}')
    
elif cedula == '57':
    final = price * 0.5
    print(f'El total con descuento a la cc terminana en {cedula} es ${final}')
else:
    print('Sin descuentos aplicables!')

# 3.

price = int(input('Precio total de los colchones: $'))
colchones_comprar = int(input('Numero de colchones a comprar: '))

if colchones_comprar >= 3 and colchones_comprar < 6:
    price = price * 0.8
    
elif colchones_comprar >= 6 and colchones_comprar < 8:
    total = total * 0.75

elif colchones_comprar >= 8:
    total = total * 0.7
    
print(f'Para {colchones_comprar} colchones el precio es: ${price}')  



# 4.

students = int(input('Número de alumnos: '))
sample = None 
if students < 20:
    sample = round(students * 0.5)

elif students >= 20 and students <= 30:
    sample = round(students * 0.6)

elif students > 30:
    sample = round(students * 0.7)
    
print(f'{sample} estudiantes son seleccionados para ser encuestados')









