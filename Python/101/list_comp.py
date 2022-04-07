#!/usr/bin/env python

colores = ['rojo', 'naranjo','celeste','verde', 'amarillo', 'azul']
colores_titulo = []

for color in colores:
    colores_titulo.append(color.title())
    
print(colores_titulo)

#List comprehension
colores_mayuscula = [x.upper() for x in colores]

print(colores_mayuscula)

colores_claros = ['naranjo', 'celeste', 'amarillo']
otros_colores = []

for color in colores:
    if color in colores_claros:
        otros_colores.append(color)
    
print(otros_colores)

#List comprehension
mas_colores = [color for color in colores if color in colores_claros]
print(mas_colores == otros_colores)