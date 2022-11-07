#!/usr/bin/python

import os
from pathlib import Path

subdirectorio = {
    'fotos': ['.jpeg', '.jpg', '.gif'],
    'videos': ['.mpge', '.avi', '.ogg'],
    'text': ['.doc', '.txt', '.pdf'],
    'audio': ['.mp3', '.sund', '.mix']
}


def find_carpeta(valor):
    for carpeta, tipo in subdirectorio.items():
        if valor in tipo:
            return carpeta


def dir_list():
    for i in os.scandir():
        file_name = (Path(i))
        file_suffix = file_name.suffix
        directorio = find_carpeta(file_suffix)
        if directorio is None:
            continue
        # print(f'Nombre del archivo: {file_name}')
        # print(f'Suffix del archivo: {file_suffix}')
        # print(f'Nombre del directorio: {directorio}')
        # print(f'Patch del directorio: {Path(directorio)}')


dir_list()