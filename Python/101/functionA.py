#/usr/bin/env python

dict1 = {"name": "Pepe",
         "lasname": "Tribino"}

def functionA(name, lastname):
    return (f'My name is {name} and my lastname is {lastname}')

print(functionA(dict1.items()))