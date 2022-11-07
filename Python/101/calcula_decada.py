#!/usr/bin/python

# This is a simple python script that calculate decades

tu_edad  = int(input('Que edad tienes? '))
decada   = tu_edad // 10 # Divide sin coma
anios    = tu_edad % 10  # Modulo
print(f'Tu tienes {decada} decadas, y {anios} anios')