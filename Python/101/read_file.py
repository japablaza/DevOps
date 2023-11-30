#!/usr/bin/python

archivos = open('docos.txt', 'r')
comandos = open('list_de_comandos.txt', 'w')
for archivo in archivos:
    linea = archivo.split()
    if len(linea) == 9:
        comandos.write(f'{linea[8]}\n')
archivos.close()
comandos.close()
