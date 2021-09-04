# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:47:33 2021

@author: ignacio
"""

#import matplotlib.pyplot as plt
from time import perf_counter
import numpy as np
import scipy.sparse as sparse
from scipy import linalg
import scipy.sparse.linalg as lin


def matriz_laplaciana_dispersa(N, t=np.double):    # funcion obtenida de clases para formar matriz dispersa
    d=sparse.eye(N, N, 1, dtype=t)
    return 2 * sparse.eye(N,dtype=t) - d - d.T


def matriz_laplaciana_llena(N, t=np.double):    # funcion obtenida de clases para formar matriz llena
    e=np.eye(N)-np.eye(N,N,1)
    return t(e+e.T)


Ns = [2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000, 6000]

corridas= 10

names = ["MATMUL_llena.txt", "MATMUL_dispersa.txt", "SOLVE_llena.txt", "SOLVE_dispersa.txt", "INV_llena.txt", "INV_dispersa.txt"]

files = [open(name, "w") for name in names]

for N in Ns:
    
    dts1 = np.zeros((corridas, len(files)))
    dts2 = np.zeros((corridas, len(files)))
    print(f"N = {N}")
    
    
    for i in range(corridas):
        
        #--------------------------------------------------------------      
        #MATMUL LLENA
        
        t1 = perf_counter() 
           
        A = matriz_laplaciana_llena(N)
        B = matriz_laplaciana_llena(N)
                
        t2 = perf_counter()
        
        matmul_LL = A@B
        
        t3 = perf_counter()
        
        dt1 = t2 - t1
        dt2 = t3 - t2
        
        dts1[i][0] = dt1
        dts2[i][0] = dt2
        
        #---------------------------------------------------------------
        #MATMUL DISPERSA

        t1 = perf_counter()
        
        A = matriz_laplaciana_dispersa(N)
        B = matriz_laplaciana_dispersa(N)
        
        t2 = perf_counter()
        
        matmul_D = A@B
        
        t3 = perf_counter()
    
        dt1 = t2 - t1
        dt2 = t3 - t2
        
        dts1[i][1] = dt1
        dts2[i][1] = dt2


        #---------------------------------------------------------------
        #SOLVE LLENA
                
        t1 = perf_counter()
        
        A = matriz_laplaciana_llena(N)
        b = np.ones(N, dtype = np.double)        
        
        t2 = perf_counter()
        
        solve_LL = linalg.solve(A,b)
        
        t3 = perf_counter()
    
        dt1 = t2 - t1
        dt2 = t3 - t2
        
        dts1[i][2] = dt1
        dts2[i][2] = dt2
        
        #---------------------------------------------------------------
        #SOLVE DISPERSA

        t1 = perf_counter()
        
        A = matriz_laplaciana_dispersa(N)
        b = np.ones(N, dtype = np.double)
        Acsc = sparse.csc_matrix(A)
        
        t2 = perf_counter()
        
        solve_D = lin.spsolve(Acsc,b)
        
        t3 = perf_counter()
    
        dt1 = t2 - t1
        dt2 = t3 - t2
        
        dts1[i][3] = dt1
        dts2[i][3] = dt2


        #---------------------------------------------------------------
        #INV LLENA

        t1 = perf_counter()
        
        A = matriz_laplaciana_llena(N)
        
        t2 = perf_counter()
        
        inv_LL = np.linalg.inv(A)
        
        t3 = perf_counter()
    
        dt1 = t2 - t1
        dt2 = t3 - t2
        
        dts1[i][4] = dt1
        dts2[i][4] = dt2
        
        #---------------------------------------------------------------
        #INV DISPERSA

        t1 = perf_counter()
        
        A = matriz_laplaciana_dispersa(N)
        Acsc = sparse.csc_matrix(A)    
        
        t2 = perf_counter()
        
        inv_D = lin.inv(Acsc)
        
        t3 = perf_counter()
    
        dt1 = t2 - t1
        dt2 = t3 - t2
        
        dts1[i][5] = dt1
        dts2[i][5] = dt2
       

    #Calculo del promedio de las corridas
    
    dts_mean1 = [np.mean(dts1[:,j]) for j in range(len(files))]
    dts_mean2 = [np.mean(dts2[:,j]) for j in range(len(files))]    
 
    #Escribo los dts promedio junto con el N 
    
    for j in range(len(files)):
        files[j].write(f"{N} {dts_mean1[j]} {dts_mean2[j]} \n")
        files[j].flush()
        
[file.close() for file in files]

