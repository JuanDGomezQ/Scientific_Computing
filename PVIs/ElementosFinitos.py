import numpy as np
from time import time
import matplotlib.pyplot as plt

matriz=np.array
det=np.linalg.det
delta=0.000001
def gauss_jordan(A,b):
    ans=None
    if abs(det(A))>delta:
        for i in range(len(A)):
            transform=np.identity(len(A))
            tr=0
            while A[i][i]==0 and tr<len(A):
                if i!=tr:
                    A[i],A[tr]=matriz(A[tr]),matriz(A[i])
                    b[i],b[tr]=b[tr],b[i]
                
                tr+=1
            for j in range(len(A)):
                if i!=j:
                    transform[j][i]=-(A[j][i]/A[i][i])
           
            A=transform.dot(A)
            b=transform.dot(b)
        ans=[b[i]/A[i][i] for i in range(len(b))]
    else:
        print("no tiene solucion")       
    return ans



def Diferencial2(x):
    """
    x*cos(x)
    """
    return x*np.cos(x)


def Analitica2(x):
    """
    Funcion encargada de dar el resultado analitico de la Segunda Diferencial
    -x*cos(x)+2*sin(x)+c1*x+c2
    """
    return -x*np.cos(x)+2*np.sin(x)


def Diferencias(f,xa,xb,ya,yb,n):
    """
    f ecuacion diferencial
    xa,ya primer valor de frontera
    xb,yb segundo valor de frontera
    n numero de puntos
    """
    L=np.linspace(xa,xb,n)
    h=(xb-xa)/(n-1)
    A=np.array([[0 for _ in range(n-2)] for _ in range(n-2)])
    for i in range(n-2):
        A[i][i]=-2
        if i!=0 and i!=n-3:
            A[i][i-1]=1
            A[i][i+1]=1
        elif i ==0:
            A[i][i+1]=1
        else:
            A[i][i-1]=1
    
    b=np.array([f(L[x])*h*h for x in range(1,n-1)])
    b[0]-=ya
    b[-1]-=yb

    return L,[xa]+gauss_jordan(A,b)+[xb]


def elementosfinitos(f,xa,xb,ya,yb,n):
    ans=[None for _ in range(n)]
    ans[0]=[xa**i for i in range(n)]
    ans[-1]=[xb**i for i in range(n)]
    X=np.linspace(xa,xb,n)
    for i in range(1,n-1):
        ans[i]=[j*(j-1)*X[i]**(j-2) if j>1 else 0 for j in range(n)]
    B=[None for _ in range(n)]
    B[0]=ya
    B[-1]=yb
    
    for i in range(1,n-1):
        B[i]=f(X[i])
    K=gauss_jordan(ans,B)
 
    Y=[sum(K[i]*x**i for i in range(n)) for x in X]
    return X,Y


def main():


    n=10
    start_time = time()
    
    F=Diferencial2

    T,Y = Diferencias(F,2,4,5,2,n)
    T2,Y2 = Diferencias(F,10,2,4,5,n)


    FA=Analitica2


    
    YAnalitica = np.array([FA(T[i]) for i in range(len(T))])
    YAnalitica2 = np.array([FA(T2[i]) for i in range(len(T2))])

    
    elapsed_time = time() - start_time
    
    Error1 = np.mean([  0 if FA(T[x]) ==0 else abs((FA(T[x])-Y[x])/FA(T[x]))  for x in range(len(T)-1)])
    Error2 = np.mean([  0 if FA(T2[x]) ==0 else abs((FA(T2[x])-Y2[x])/FA(T2[x]))  for x in range(len(T2)-1)])


    ErrorTotal = (Error1 + Error2 )/2
    print("Error Total: ",ErrorTotal)
    print("Tiempo: {} ".format(elapsed_time))


    fig, axs = plt.subplots(1, 2, figsize=(9, 3), sharey=True)

    axs[0].plot(T,Y,color="r",label='(2,4)(5,2)')
    axs[0].plot(T,YAnalitica,color="brown",label="Analitica")
    axs[0].legend()

    axs[1].plot(T2,Y2,color="black",label='(10,2)(4,5)')
    axs[1].plot(T2,YAnalitica2,color="brown",label="Analitica")
    axs[1].legend()



    plt.show()
    
main()