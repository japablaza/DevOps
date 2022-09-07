#!/usr/bin/python

from urllib.request import urlopen as uo

url = 'https://sixty-north.com/c/t.txt'
url2 = 'http://cuatrodedos.com/web2.0/'

historia = uo(url)

for line in historia:
    print(line.decode('utf-8').split())
# print(historia.read())

historia.close()


