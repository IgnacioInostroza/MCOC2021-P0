# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:05:03 2021

@author: ignacio
"""

import matplotlib.pyplot as plt
from scipy import linalg
from scipy.linalg import eigh
from time import perf_counter
import numpy as np


def matriz_laplaciana(N, t=np.single):    # funcion obtenida de clases
    e=np.eye(N)-np.eye(N,N,1)
    return t(e+e.T)


Ns = [2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000]#, 5000]

corridas= 10

names = ["sp.EIGH_I.txt", "sp.EIGH_II_1.txt", "sp.EIGH_II_2.txt", "sp.EIGH_III_1.txt", "sp.EIGH_III_2.txt", "sp.EIGH_IV_1.txt", "sp.EIGH_IV_2.txt", "sp.EIGH_V_1.txt", "sp.EIGH_V_2.txt"]

files = [open(name, "w") for name in names]

for N in Ns:
    
    dts = np.zeros((corridas, len(files)))
    print(f"N = {N}")
    
    #generacion de matriz y vector    
    A = matriz_laplaciana(N)
    
    for i in range(corridas):
        
        #--------------------------------------------------------------      
        #Usando scipy.linalg.eigh con parametros por defecto (I)
        
        t1 = perf_counter() 
        
        linalg.eigh(A)
        
        t2 = perf_counter()
        
        dt1 = t2 - t1        
        dts[i][0] = dt1
    
        #--------------------------------------------------------------
        #Usando scipy.linalg.eigh con driver="ev" y overwrite_a=False (II_1)
        
        t3 = perf_counter()
        
        linalg.eigh(A, driver="ev", overwrite_a=False )
        
        t4 = perf_counter()
        
        dt2 = t4 - t3        
        dts[i][1] = dt2
        
        #--------------------------------------------------------------
        #Usando scipy.linalg.eigh con driver="ev" y overwrite_a=True (II_2)
        
        t5 = perf_counter()
        
        linalg.eigh(A, driver="ev", overwrite_a=True )
        
        t6 = perf_counter()
        
        dt3 = t6 - t5        
        dts[i][2] = dt3

        #--------------------------------------------------------------
        #Usando scipy.linalg.eigh con driver="evd" y overwrite_a=False (III_1)
        
        t7 = perf_counter()
        
        linalg.eigh(A, driver="evd", overwrite_a=False )
        
        t8 = perf_counter()
        
        dt4 = t8 - t7        
        dts[i][3] = dt4
        
        #--------------------------------------------------------------
        #Usando scipy.linalg.eigh con driver="evd" y overwrite_a=True (III_2)
        
        t9 = perf_counter()
        
        linalg.eigh(A, driver="evd", overwrite_a=True )
        
        t10 = perf_counter()
        
        dt5 = t10 - t9        
        dts[i][4] = dt5

        #--------------------------------------------------------------
        #Usando scipy.linalg.eigh con driver="evr" y overwrite_a=False (IV_1)
        
        t11 = perf_counter()
        
        linalg.eigh(A, driver="evr", overwrite_a=False )
        
        t12 = perf_counter()
        
        dt6 = t12 - t11        
        dts[i][5] = dt6
        
        #--------------------------------------------------------------
        #Usando scipy.linalg.eigh con driver="evr" y overwrite_a=True (IV_2)
        
        t13 = perf_counter()
        
        linalg.eigh(A, driver="evr", overwrite_a=True )
        
        t14 = perf_counter()
        
        dt7 = t14 - t13        
        dts[i][6] = dt7
        
        #--------------------------------------------------------------
        #Usando scipy.linalg.eigh con driver="evx" y overwrite_a=False (V_1)
        
        t15 = perf_counter()
        
        linalg.eigh(A, driver="evx", overwrite_a=False )
        
        t16 = perf_counter()
        
        dt8 = t16 - t15        
        dts[i][7] = dt8
        
        #--------------------------------------------------------------
        #Usando scipy.linalg.eigh con driver="evx" y overwrite_a=True (V_2)
        
        t17 = perf_counter()
        
        linalg.eigh(A, driver="evx", overwrite_a=True )
        
        t18 = perf_counter()
        
        dt9 = t18 - t17        
        dts[i][8] = dt9
        
                
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
plt.savefig("Desempeño_EIGH_single.png")
