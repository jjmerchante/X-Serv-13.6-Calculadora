#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    if (num2 == 0):
        return "NaN"
    else:
        return num1 / num2


# Para poder usar las operaciones desde otro archivo
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print
        sys.exit("Uso: python calculadora.py funcion operando1 operando2")
    try:
        fun_str = sys.argv[1]
        operando1 = float(sys.argv[2])
        operando2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Tienes que introducir un número")

    print "El resultado de la operación es:",
    if fun_str == "suma":
        print suma(operando1, operando2)
    elif fun_str == "resta":
        print resta(operando1, operando2)
    elif fun_str == "mult":
        print mult(operando1, operando2)
    elif fun_str == "div":
        print div(operando1, operando2)
    else:
        print "Operaciones válidas: suma, resta, mult, div"
