#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys


def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 


if len(sys.argv) < 2:
    print("debe informar un numero o rango (ej: 4 o 4-8)")
    sys.exit()

input = sys.argv[1]

# el usuario pasa un rango

if "-" in input: 
    desde, hasta = input.split("-")
    
    desde = int(desde)
    hasta = int(hasta)

    if desde > hasta:
        print("el rango no es correcto")
        sys.exit()

    for n in range(desde, hasta + 1):
        print("factorial", n, "! =", factorial(n))

# el usuario pasa solo un numero
else: 
    num = int(input)
    print("factorial", num, "! =", factorial(num))





# if len(sys.argv) == 0:
#    print("Debe informar un número!")
#    sys.exit()
# num=int(sys.argv[1])
# print("Factorial ",num,"! es ", factorial(num)) 

