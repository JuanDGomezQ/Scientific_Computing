"""
    Juan David Gomez
    Codigo: 8939024
"""

from sys import stdin
import math
import numpy as np
import pylab as plt
from time import time

def f(x):
    """  
        Esta funcion, evalua la funcion matematica f(x) segun un valor x.

        Dentro de esta funcion se encuentran las 3 funciones requeridas para el laboratorio, para usar una solo
        es necesario descomentarla, recuerde que solo puede haber una funcion descomentada.
    """
    return (8*math.pow(x,3))+ (2*math.pow(x,2)) + (2*x)                 #Funcion 1: 8x**3 + 2x**2 + 2x
    #return (5 * math.sin(x))                                            #Funcion 2: 5 * Sin(x**2)
    #return np.log((math.pow(x,5)) + 100)                                 #Funcion 3: log(x**5 + 100)


def difFinitAtras(x,h):
    """
        Esta funcion aplica la formual para derivacion mediante el metodo hacia atras
    """
    ans =(f(x) - f(x - h)) / h
    return ans

def evaluar(n,h):
    """
        Esta funcion se encarga de evaluar los datos para usarlos como valores de y y poder graficarlos
    """
    ans = []
    for i in range(n):
        tmp = difFinitAtras(i,h)
        ans.append(tmp)
    return ans

def analitica(n):
    """
        Esta funcion calcula la derivada calculada de forma analitica, esta funcion tiene las tres
        funciones requeridas para este laboratorio, para usar una solo es necesario descomentarla
        y comentar todas las demas
    """
    ans = []
    for i in range(n):
        tmp = 24*pow(i,2) + 4*(i) + 2                              #Derivada Funcion 1: 24x**2 + 4x + 2
        #tmp = 5*math.cos(i)                                        #Derivada Funcion 2: 5cos(x**2)
        #tmp =  (5 * math.pow(i,4)) / (math.pow(i,5) + 100)          #Derivada Funcion 3: 5x**(4)  / 2(x**(5) + 100) 
        ans.append(tmp)
    return ans

def pruebas(x,hs):
    """
        Esta funcion imprime las pruebas dado un x y un arreglo de valores h
    """
    print()
    print(" Metodo Hacia Atras:")
    print(" -------------------------------------------------------------------------")
    for i in hs:
        start = time()
        ans = difFinitAtras(x,i)
        elapsed = time() - start
        real = 24*pow(x,2) + 4*(x) + 2  #Derivada Analitica
        error = abs(ans - real)
        print("con x = 5, h = {0}".format(i))
        print("  el resultado con el metodo es: {0} con un erro de {1}".format(ans,error))
        print("  tiempo de ejecucion: {0}".format(elapsed))
        print(" -------------------------------------------------------------------------")    


def main():
    """
        Funcion Principal que llama a los metodos para hacer diferencias hacia atras, despues grafica
    """
    x = 5
    h = 1
    
    hs = [0.2,1,2,3]
    pruebas(x,hs)
    
    n = 10
    ans = difFinitAtras(x,h)
    print(ans)
    finx = np.linspace(0,100,n)
    finy = evaluar(n,h)
    plt.plot(finx,finy,color = "r",label = "h = 1")
    plt.legend(loc = "upper right")
    h = 0.2
    finy = evaluar(n,h)
    plt.plot(finx,finy,color = "b",label = "h = 0.2")
    plt.legend(loc = "upper right")
    h = 2
    finy = evaluar(n,h)
    plt.plot(finx,finy,color = "g",label = "h = 2")
    plt.legend(loc = "upper right")
    h = 3
    finy = evaluar(n,h)
    plt.plot(finx,finy,color = "y",label = "h = 3")
    plt.legend(loc = "upper right")
    finy = analitica(n)
    plt.plot(finx,finy,color = "black",label = "derivada analitica")
    plt.legend(loc = "upper right")
    plt.title("Metodo Hacia Atras | f(x) = log(x**5 + 100) | f'(x) = 5x**(4)  / 2(x**(5) + 100) ")
    plt.grid()
    plt.show()
main()