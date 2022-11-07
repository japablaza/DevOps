#!/usr/bin/python

from random import choice as ch

piedra     = 'piedra'
papel      = 'papel'
tijera     = 'tijera'

opciones   = [piedra, papel, tijera]
compu      = ch(opciones)
usuario    = input('Usa una opcion: piedra, papel, o tijera: \n') 
print('\n')
print('*'*20)
print(f'El usuario saco {usuario}')
print(f'El computador saco {compu}')
print('*'*20)

if usuario == compu:
    print('\n Empate')
elif usuario == piedra and compu == papel:
    print('\n Gana el compu')
elif usuario == tijera and compu == papel:
    print('\n Gana Usuario')
elif usuario == piedra and compu == tijera:
    print('Gana el Usuario')
elif usuario == papel and compu == tijera:
    print('Gano el Compu')    
else:
# elif compu == piedra and usuario == tijera:
    print('\n No idea como llegamos aqui')
    