#!/usr/bin/python

from urllib.request import urlopen as uo

url = 'https://sixty-north.com/c/t.txt'
url2 = 'http://cuatrodedos.com/web2.0/'

historia = uo(url)
palabras = []
for line in historia:
    line = line.decode('utf-8').split()
    for word in line:
        palabras.append(word)

# print(historia.read())

historia.close()

print(palabras)