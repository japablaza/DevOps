#/usr/bin/python

# Este es el juego de los datos

from random import randint as ri


computador  = ri(1,6)
usuario     = int(input('Dame un numero entre el 1 y el 6:\n'))

print(f'El computador saco: {computador}')

if computador == usuario:
    print('\n**********')
    print('Hay un empate')
    print('**********')
elif computador > usuario:
    print('\n**********')
    print('El computador gano')
    print('**********')
else:
    print('\n**********')
    print('El usuario gano')
    print('**********')