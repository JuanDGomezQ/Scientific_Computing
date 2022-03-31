import matplotlib.pyplot as plt
import numpy as np
from math import e



def Productorias(t, T, j , n):

	#FUNCION ENCARGADA DE REALIZAR LAS PRODUCTORIAS DE LA FORMULA DE LAGRANGE Y RETORNAR LA DIVISION ENTRE ELLAS
	Prod1=1
	Prod2=1
	for k in range(n):
		if(j!=k):
			Prod1*= (t- T[k])
			Prod2*= (T[j] - T[k])

	return Prod1/Prod2

def Lagrange(t,y,t_eval,n): 

	"""
	funcion encargada de aplicar lagrange a todos los t_eval que son los t entregados para evaluar
	y retorna su solucion
	"""

	sol=[]
	for i in range(n):
		Polinomio=0
		for j in range(len(t)):
			aux = Productorias(t_eval[i],t, j , len(t))
			#print(y[j]*aux, aux, y)
			Polinomio+= y[j]*aux

		sol.append(Polinomio)

	return sol




def main():
	#primera base de datos relacionada a la caida del peso argentino a lo largo de 50 dias
    t = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
    y = np.array([80.883, 80.693, 80.514, 80.348, 80.192, 80.046, 79.911, 79.786, 79.671, 79.565, 79.467, 79.378, 79.297, 79.224, 79.158, 79.099, 79.047, 79.001, 78.96, 78.926, 78.896, 78.871, 78.851, 78.834, 78.822, 78.812, 78.805, 78.8, 78.8, 78.8, 78.801, 78.804, 78.807, 78.81, 78.814, 78.817, 78.819, 78.821, 78.82, 78.818, 78.814, 78.807, 78.797, 78.783, 78.766, 78.745, 78.72, 78.689, 78.654, 78.613])
    #Segunda base de datos relacionada a aumento de casos de covid en 50 dias
    #y = np.array([666521,671848,679513,686851,694664,702088,708914,716319,721892,728590,736377,743945,750471,758398,765076,770435,777537,784268,790823,798317,806038,813056,818206,824042,829679,835339,841531,848147,855052,862158,869808,877683,886179,894300,902747,911316,919083,924096,930159,936982,945354,952371,959572,965883,974139,981700,990270,998942,1007711,1015885])
    
    #Tercero ejemplo de la clase sobre interpolacion polinomial
    #=np.array([-2,0,1])
    #= np.array([-27,-1,0])
    #t_entrena=np.array([-2,0,1])
    #y_entrena= np.array([-27,-1,0])


    d= int(input("Ingrese el tamaño del salto: "))

    t_entrena = t[::d]
    y_entrena = y[::d]

    t_val = t[1::2]
    y_val = y[1::2]

    #print(t_entrena)
    #print(y_entrena)

    

    finx=np.arange(t[0],t[len(t)-1],(abs(t[0])+abs(t[len(t)-1]))/100)
    
    finy= Lagrange(t_entrena,y_entrena,finx,len(finx))


    yevu= Lagrange(t_entrena,y_entrena,t_val,len(t_val))

    Error= np.mean(abs(yevu-y_val))
    
    print("El error es: " ,Error )

    plt.plot(finx,finy,label="Grafica Polinomio")
    plt.plot(t_entrena,y_entrena,'.',color="r",label='Datos de Entrenamiento')
    plt.plot(t_val,y_val,'.',color="g",label="Datos de Validacion")
    plt.legend(loc="upper right")
    plt.grid()
    plt.show()




main()