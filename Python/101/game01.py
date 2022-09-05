#!/usr/bin/python

# El juego de piedra papel y tijeras

computador    = 'papel'

usuario       = input('Usa "papel", "tijera", o "piedra": \n')

if computador == usuario:
    print('Hay un empate')
elif usuario == "tijera":
    print('\n**************')
    print('El usuario gano')
    print('**************')
else:
    print('\n**************')
    print('El computador gano')
    print('**************')