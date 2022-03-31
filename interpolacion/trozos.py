import matplotlib.pyplot as plt
import numpy as np
from math import e


def evaluar(M,t,t_eval):
    sol=[]

    for i in range(len(t_eval)):
        index=0
        for j in range(len(t)):
            if(t_eval[i]<t[j]):
                index=j-1

                break
            elif(t_eval[i]==t[j]):
                index= len(M[0])-1

        aux= M[0][index]*t_eval[i] + M[1][index]
        sol.append(aux)

    
    return sol

def interTrozos(t,y):
    """
    Entrada: Arreglo de t y arreglo de y
    Salida: una matriz "ans" de dimensiones 2 x (n - 1) que almacena las pendientes (m) e interceptos (b)
            de las rectas que se pueden generar entre cada pareja de puntos consecutivos (ti,yi).
            para la matriz "ans" cada columna representa la recta entre dos puntos consecutivos, la fila 0
            almacena los m de cada recta y la fila 1 almacena los b de cada recta, teniendo en cuenta que
            la ecuacion de la recta es y = mx + b.
    """
    n = len(t)
    ans = [[0 for i in range(n - 1)] for i in range(2)] #creacion de la matriz 2 x (n-1)
    ti,yi = 0,0
    for _ in range(n - 1): #para cada pareja de puntos consecutivos (d,e) se calcula los valores de  m y b que tendria la recta que intercepta d y e 
        m = (y[yi + 1] - y[yi]) / (t[ti + 1] - t[ti]) #calculo de la oendiente (m)
        ans[0][ti] = m #guarda m en la posicion correspondiente de la matr
        b = y[yi] - m * t[ti] #calculo intercepto eje y (b)
        ans[1][ti] = b
        ti += 1
        yi += 1
    return ans

#t = [0,1,2,3,4]
#y = [0,1,4,3,6]


def main():
    #primera base de datos relacionada a la caida del peso argentino a lo largo de 110 dias
    t = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
    y = np.array([78.612,78.69,78.214,78.295,78.2345,78.306,78.2,78.06,77.99,77.67,77.655,77.5035,77.462,77.4065,77.41,77.3625,77.0005,77.054,77.095,77.085,77.05,76.886,76.177,76.18,76.12,75.9865,75.7835,75.78,75.68,75.577,75.523,75.585,75.1825,75.215,75.1175,75.055,75.01,74.775,74.72,74.638,74.3685,74.645,74.308,74.1785,74.315,74.131,73.935,73.8775,73.803,73.746,73.667,73.502,73.472,73.339,73.3365,73.1,73.0405,73.13,72.9845,72.942,72.892,72.6375,72.6375,72.566,72.45,72.49,72.2495,72.19,72.13,72.0715,72.035,71.985,71.77,71.6505,71.745,71.63,71.4245,71.3575,71.32,71.17,71.205,70.875,70.878,70.885,70.865,70.751,70.3915,70.635,70.575,70.46,70.3495,70.1525,70.092,70.0325,70.095,69.93,69.746,69.6815,69.62,69.62,69.34,69.2525,69.345,69.1035,69.13,69.05,68.9215,68.835,68.7415,68.68])
    
    #Segunda base de datos relacionada a aumento de casos de covid en 110 dias
    #y = np.array([182140,190700,197278,204005,211038,218428,226373,233541,240795,248976,257101,267385,276055,286020,295508,306181,317651,327850,334979,345714,357710,367196,376870,387481,397623,410453,422519,433805,445111,456689,468332,476660,489122,502178,513719,522138,533103,541147,551696,562128,572270,582022,590520,599914,607938,615168,624069,633339,641574,650062,658456,666521,671848,679513,686851,694664,702088,708914,716319,721892,728590,736377,743945,750471,758398,765076,770435,777537,784268,790823,798317,806038,813056,818206,824042,829679,835339,841531,848147,855052,862158,869808,877683,886179,894300,902747,911316,919083,924096,930159,936982,945354,952371,959572,965883,974139,981700,990270,998942,1007711,1015885,1025052,1033218,1041935,1053122,1063151,1074184,1083321,1093256,1099392])
    
    #Tercero ejemplo de la clase sobre interpolacion polinomial
    #t=np.array([-2,0,1])
    
    #y= np.array([-27,-1,0])


    d= int(input("Ingrese el tamaño del salto: "))

    t_entrena = t[::d]
    y_entrena = y[::d]

    t_val = t[1::2]
    y_val = y[1::2]

  
    finx=np.arange(t[0],t[len(t)-1],(abs(t[0])+abs(t[len(t)-1]))/100)
    sol = interTrozos(t_entrena,y_entrena)
    finy= evaluar(sol,t_entrena,finx)

    yevu= evaluar(sol,t_entrena,t_val)

    Error= np.mean(abs(yevu-y_val))
    
    print("El error es: " ,Error )

    plt.plot(finx,finy,label="Grafica Polinomio")
    plt.plot(t_entrena,y_entrena,'.',color="r",label='Datos de Entrenamiento')
    plt.plot(t_val,y_val,'.',color="g",label="Datos de Validacion")
    plt.legend(loc="upper right")
    plt.grid()
    plt.show()
    

main()