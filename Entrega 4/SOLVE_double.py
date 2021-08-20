# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:21:39 2021

@author: ignacio
"""

import matplotlib.pyplot as plt
from scipy import linalg
from numpy.linalg import inv as invertir
from time import perf_counter
import numpy as np


def matriz_laplaciana(N, t=np.double):    # funcion obtenida de clases
    e=np.eye(N)-np.eye(N,N,1)
    return t(e+e.T)


Ns = [2, 5, 10,12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000]

corridas= 10

names = ["A_invB.txt", "sp.Solve.txt", "sp.Solve_pos.txt", "sp.Solve_sym.txt", "sp.Solve_overwrite_a=True.txt", "sp.Solve_overwrite_b=True.txt", "sp.Solve_overwrite_a,b=True.txt"]

files = [open(name, "w") for name in names]

for N in Ns:
    
    dts = np.zeros((corridas, len(files)))
    print(f"N = {N}")
    
    #generacion de matriz y vector    
    A = matriz_laplaciana(N)
    B = np.ones(N)
    
    for i in range(corridas):
        
        #--------------------------------------------------------------
        #Invertir matriz y luego multiplicar 
               
        t1 = perf_counter()
        
        A_inv = invertir(A)      
        A_invB = A_inv@B
        
        t2 = perf_counter()
        
        dt1 = t2 - t1
        dts[i][0] = dt1        
        
        #--------------------------------------------------------------      
        #Usando scipy.linalg.solve con parametros por defecto
        
        t3 = perf_counter() 
        
        linalg.solve(A,B)
        
        t4 = perf_counter()
        
        dt2 = t4 - t3        
        dts[i][1] = dt2
    
        #--------------------------------------------------------------
        #Usando scipy.linalg.solve con assume_a='pos'
        
        t5 = perf_counter()
        
        linalg.solve(A,B, assume_a = "pos" )
        
        t6 = perf_counter()
        
        dt3 = t6 - t5        
        dts[i][2] = dt3
        
        #--------------------------------------------------------------      
        #Usando scipy.linalg.solve con assume_a='sym'
        
        t7 = perf_counter() 
        
        linalg.solve(A,B, assume_a = "sym" )
        
        t8 = perf_counter()
        
        dt4 = t8 - t7        
        dts[i][3] = dt4
       
        #--------------------------------------------------------------      
        #Usando scipy.linalg.solve con overwrite_a=True        
        
        t9 = perf_counter() 
        
        linalg.solve(A,B, overwrite_a=True )
        
        t10 = perf_counter()
        
        dt5 = t10 - t9        
        dts[i][4] = dt5

        #--------------------------------------------------------------      
        #Usando scipy.linalg.solve con overwrite_b=True        
        
        t11 = perf_counter() 
        
        linalg.solve(A,B, overwrite_b=True )
        
        t12 = perf_counter()
        
        dt6 = t12 - t11        
        dts[i][5] = dt6

        #--------------------------------------------------------------      
        #Usando solve scipy con overwrite_a=True y overwrite_b=True        
        
        t13 = perf_counter() 
        
        linalg.solve(A,B, overwrite_a=True, overwrite_b=True )
        
        t14 = perf_counter()
        
        dt7 = t14 - t13        
        dts[i][6] = dt7
        
        
    print ("dts: ", dts)
    
    #Calculo del promedio de las corridas
    
    dts_mean = [np.mean(dts[:,j]) for j in range(len(files))]
    
    print("dts_mean : ", dts_mean)
    
    #Escribo los dts promedio junto con el N 
    
    for j in range(len(files)):
        files[j].write(f"{N} {dts_mean[j]}\n")
        files[j].flush()
        
[file.close() for file in files]

#Ploteo diferentes funciones

xticks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
yticks = [0.1/1000, 1/1000, 10/1000, 0.1, 1, 10, 60, 600]
ytext = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

plt.figure()

for name in names:
    data = np.loadtxt(name)
    Ns = data[:,0]
    dts =  data[:,1]
    
    print("Ns: ", Ns)
    print("dts: ", dts)
    plt.grid(b = True)
    plt.loglog(Ns, dts.T, "-o", label = name)
    plt.ylabel("Tiempo transcurrido (s)")
    plt.xlabel("Tamaño matriz N")
    
    plt.yticks(yticks, ytext)
    plt.xticks(xticks, xticks, rotation=45)
    
plt.tight_layout()
plt.legend()
plt.savefig("Desempeño_SOLVE_double.png")








