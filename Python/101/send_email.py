#!/usr/bin/python

import email


list_estudiantes = {
    "estudiantes": "4",
    "clase": "matematica",
    "contacto":
    [
        {"nombre": "Tulio", "email": "tulio@socio.cl"},
        {"nombre": "Bodoque", "email": "bodoque@socio.cl"},
        {"nombre": "bonbola", "email": "bonbola@socio.cl"},
        {"nombre": "mico", "email": "mico@socio.cl"}
    ]
}

for estudiante in list_estudiantes["contacto"]:
    print(estudiante['email'])