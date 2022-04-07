#!/usr/bin/env python

#    Print "FuBar" if the number is divisible by 3 and 5.
#    Print "Fu" if the number is divisible by 3.
#    Print "Bar" if the number is divisible by 5.
#    Otherwise print the number.

for n in range(1, 101):
    tres  = n % 3 == 0
    cinco = n % 5 == 0
    if tres and cinco:
        print('Fubar')
    elif tres:
        print('Fu')
    elif cinco:
        print('Bar')
    else:
        print(n)
