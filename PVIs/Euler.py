import numpy as np
from time import time
import matplotlib.pyplot as plt

def Diferencial1(x,y):
    """
    y' =e^x - 2Y
    """
    return np.exp(x) - 2*y

def Diferencial2(x,y):
    """
    y' = (3X + 2Y) / 3
    """
    return ((3*x) + (2*y))/3

def Analitica1(t):
    """
    Funcion encargada de dar el resultado analitico de la primera Diferencial
    y(t)=(e^t/3)+(c1/e^2*t)
    """
    return (np.exp(t)/3)+ (1/np.exp(2*t))

def Analitica2(t):
    """
    Funcion encargada de dar el resultado analitico de la Segunda Diferencial
    y(t) = ((-3*t)/2) - (9/4) + (c1*e^((2*t)/3))
    """
    return ((-3*t)/2) - (9/4) + (1*np.exp((2*t)/3))  

def euler(f,t0,y0,h,n):
    """
    Funcion encargada de hallar la aproximacion por el metodo de euler retornando dos arreglos uno con las t a evaluadas con el crecimiento de h
    y otro con las soluciones de estos t

    Entrada:
        f: es la ecuacion diferencial
        t0,y0: Valores iniciales de t y y
        h: incremento 
        n: numero de puntos
    """
    T=[]
    Y=[]
    
    for i in range(n):
        if i==0:
            T.append(t0)
            Y.append(y0)
        else:
            T.append(T[-1]+h)
            Y.append(Y[-1]+f(T[i-1],Y[i-1])*h)
    return T,Y



def main():

    t0= 0
    y0= 1
    h=0.001
    n= 10
    start_time = time()

    F=Diferencial2
    T,Y = euler(F,t0,y0,0.1,n)
    T2,Y2 = euler(F,t0,y0,0.01,n)
    T3,Y3 = euler(F,t0,y0,0.001,n)
    T4,Y4 = euler(F,t0,y0,0.0001,n)

    FA=Analitica2
    
    YAnalitica = np.array([FA(T[i]) for i in range(len(T))])
    YAnalitica2 = np.array([FA(T2[i]) for i in range(len(T2))])
    YAnalitica3 = np.array([FA(T3[i]) for i in range(len(T3))])
    YAnalitica4 = np.array([FA(T4[i]) for i in range(len(T4))])
    
    elapsed_time = time() - start_time
    
    Error2 = np.mean([  0 if FA(T[x]) ==0 else abs((FA(T[x])-Y[x])/FA(T[x]))  for x in range(len(T)-1)])

    
    print("Error 2: ",Error2)
    print("Tiempo: {} ".format(elapsed_time))


    fig, axs = plt.subplots(1, 4, figsize=(9, 3), sharey=True)

    axs[0].plot(T,Y,color="r",label='h = 0.1')
    axs[0].plot(T,YAnalitica,color="brown",label="Analitica")
    axs[0].legend()

    axs[1].plot(T2,Y2,color="black",label='h = 0.01')
    axs[1].plot(T2,YAnalitica2,color="brown",label="Analitica")
    axs[1].legend()

    axs[2].plot(T3,Y3,color="b",label='h = 0.001')
    axs[2].plot(T3,YAnalitica3,color="brown",label="Analitica")
    axs[2].legend()

    axs[3].plot(T4,Y4,color="g",label='h = 0.0001')
    axs[3].plot(T4,YAnalitica4,color="brown",label="Analitica")
    axs[3].legend()

    plt.show()

main()