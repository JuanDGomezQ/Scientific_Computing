"""
    Juan David Gomez
    Codigo: 8939024
"""

from sys import stdin
import math
import numpy as np
import matplotlib as plt
from time import time

def f(x):
    """  
        Esta funcion, evalua la funcion matematica f(x) segun un valor x.

        Dentro de esta funcion se encuentran las 3 funciones requeridas para el laboratorio, para usar una solo
        es necesario descomentarla, recuerde que solo puede haber una funcion descomentada.
    """
    #return (8*math.pow(x,3))+ (2*math.pow(x,2)) + (2*x)                 #Funcion 1: 8x**3 + 2x**2 + 2x
    #return (5 * math.sin(x))                                            #Funcion 2: 5 * Sin(x**2)
    return np.log((math.pow(x,5)) + 100)                                 #Funcion 3: log(x**5 + 100)

def simpson(a,b,n):
    """
        Entrada:  un limite de integrcion inferior a, un limite de integracion b y un n que es la cantida de
                  partes en las que se integraran
        
        Salida:   Valor de la integral definida entre a y b calculado mediante el metodo de simpson
    """
    ans = 0
    i = (b - a)/ n
    xi = i
    while xi <= b:
        xiant = xi - i
        ans += (xi -xiant) * ( f(xiant) + (4*f((xiant + xi)/2)) + f(xi) )
        xi += i
    ans = ans * 1/6
    return ans

def pruebas(a,b,n):
    """
        Esta funcion imprime las pruebas dado un x y un arreglo de valores h
    """
    print()
    print(" Metodo simpson:")
    print(" -------------------------------------------------------------------------")
    for i in n:
        start = time()
        ans = simpson(a,b,i)
        elapsed = time() - start
        real = 4.60683232792 #Integral Analitica funcion1: 11/3 | funcion 2: 5*(-math.cos(1) + 1) | Funcion3: 4.60683232792
        error = abs(ans - real)
        print("con x = 5, n = {0}".format(i))
        print("  el resultado con el metodo es: {0} con un erro de {1}".format(ans,error))
        print("  tiempo de ejecucion: {0}".format(elapsed))
        print(" -------------------------------------------------------------------------")    


def main():
    """
        Funcion Principal donde se definen los valores para los limites de integracion a,b y la cantida de
        intervalos en los que se integrara (n), ademas se hace el llamado a la funcion simpson(a,b,n) para
        solucionar la integral por el metodo simpson
    """
    n = 10
    a = 0
    b = 1
    ns = [20,60,120,300]
    pruebas(a,b,ns)
    ans = simpson(a,b,n)
    print(ans)
    
main()