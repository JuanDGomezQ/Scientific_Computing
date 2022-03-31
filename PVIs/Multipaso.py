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



def MultipasoOrden2(f,x0,y0,h,n):
    """
    F ECUACION DIFERENCIAL
    X0,Y0 valorinicial
    h incremento
    n numero de puntos
    """
    X=[]
    Y=[]
    
    
    for i in range(n):
        if i==0:
            X.append(x0)
            Y.append(y0)
        elif i==1:
            k1=f(X[-1],Y[-1])
            k2=f(X[-1]+h/2,Y[-1]+k1*h/2)
            k3=f(X[-1]+h/2,Y[-1]+k2*h/2)
            k4=f(X[-1]+h,Y[-1]+k3*h)
            X.append(X[-1]+h)
            Y.append(Y[-1]+h*(k1+2*(k2+k3)+k4)/6)
            
        else:        
        
            Y.append(Y[-1]+(3*f(X[-1],Y[-1])-f(X[-2],Y[-2]))*h/2)
            X.append(X[-1]+h)
    return X,Y

def MultipasoOrden4(f,x0,y0,h,n):
    """
    F ECUACION DIFERENCIAL
    X0,Y0 valorinicial
    h incremento
    n numero de puntos
    """
    X=[]
    Y=[]
    for i in range(n):
        if i==0:
            X.append(x0)
            Y.append(y0)
        
        elif 0<i<4:
            
            k1=f(X[-1],Y[-1])
            k2=f(X[-1]+h/2,Y[-1]+k1*h/2)
            k3=f(X[-1]+h/2,Y[-1]+k2*h/2)
            k4=f(X[-1]+h,Y[-1]+k3*h)
            X.append(X[-1]+h)
            Y.append(Y[-1]+h*(k1+2*(k2+k3)+k4)/6)
            
        else:
            p=55*f(X[-1],Y[-1])-59*f(X[-2],Y[-2])+37*f(X[-3],Y[-3])-9*f(X[-4],Y[-4])
            Y.append(Y[-1]+p*h/24)
            X.append(X[-1]+h)
    return X,Y


def main():

    t0= 0
    y0= 1
    h=0.001
    n= 10
    start_time = time()
    
    F=Diferencial2

    Mult= MultipasoOrden4
    T,Y = Mult(F,t0,y0,0.1,n)
    T2,Y2 = Mult(F,t0,y0,0.01,n)
    T3,Y3 = Mult(F,t0,y0,0.001,n)
    T4,Y4 = Mult(F,t0,y0,0.0001,n)

    FA=Analitica2


    
    YAnalitica = np.array([FA(T[i]) for i in range(len(T))])
    YAnalitica2 = np.array([FA(T2[i]) for i in range(len(T2))])
    YAnalitica3 = np.array([FA(T3[i]) for i in range(len(T3))])
    YAnalitica4 = np.array([FA(T4[i]) for i in range(len(T4))])
    
    elapsed_time = time() - start_time
    
    Error1 = np.mean([  0 if FA(T[x]) ==0 else abs((FA(T[x])-Y[x])/FA(T[x]))  for x in range(len(T)-1)])
    Error2 = np.mean([  0 if FA(T2[x]) ==0 else abs((FA(T2[x])-Y4[x])/FA(T2[x]))  for x in range(len(T2)-1)])
    Error3 = np.mean([  0 if FA(T3[x]) ==0 else abs((FA(T3[x])-Y4[x])/FA(T3[x]))  for x in range(len(T3)-1)])
    Error4 = np.mean([  0 if FA(T4[x]) ==0 else abs((FA(T4[x])-Y4[x])/FA(T4[x]))  for x in range(len(T4)-1)])

    ErrorTotal = (Error1 + Error2 + Error3 + Error4)/4
    print("Error Total: ",ErrorTotal)
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