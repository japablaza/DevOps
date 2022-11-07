#!/usr/bin/python

from urllib.request import urlopen as uo


def a_buscar():
    url = 'https://sixty-north.com/c/t.txt'
    url2 = 'http://cuatrodedos.com/web2.0/'

    historia = uo(url)
    palabras = []
    for line in historia:
        line = line.decode('utf-8').split()
        for word in line:
            palabras.append(word)

    historia.close()
    return palabras


def imprime_items(items):
    for item in items:
        print(item)


def main():
    frace = a_buscar()
    imprime_items(frace)

if __name__ == '__main__':
    main()