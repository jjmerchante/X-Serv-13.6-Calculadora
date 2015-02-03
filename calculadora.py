#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def suma (num1, num2):
    return num1 + num2
    
def resta (num1, num2):
    return num1 - num2
    
def mult (num1, num2):
    return num1 * num2
    
def div (num1, num2):
    return num1 / num2

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print 
        sys.exit("Usage: python calculadora.py funcion operando1 operando2")
try:
    fun_str = sys.argv[1]
    operando1 = float(sys.argv[2])
    operando2 = float(sys.argv[3])
except ValueError:
    sys.exit("Tienes que introducir un float")

if fun_str == "suma":
    print suma(operando1, operando2)
elif fun_str == "resta":
    print resta(operando1, operando2)
elif fun_str == "mult":
    print mult(operando1, operando2)
elif fun_str == "div":
    print div(operando1, operando2)
else:
    print "Error: Nombre de funcion no válida"
