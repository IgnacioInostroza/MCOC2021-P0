# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:11:44 2021

@author: ignacio
"""

from numpy.linalg import inv as invertir
from time import perf_counter
import numpy as np

#########################################################
#                                                       #
# ESTE CODIGO NO FUNCIONA (MOSTRAR SCREENSHOT DEL ERROR)#
#                                                       #
#########################################################

def matriz_laplaciana(N, t=np.half):    # funcion obtenida de clase
    e=np.eye(N)-np.eye(N,N,1)
    return t(e+e.T)


Ns = [2, 5, 10,12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500] # 600, 800, 1000, 2000, 5000, 10000]

corridas = 10

for corrida in range(corridas):
    
    tiempo = []
    memoria = []
    
    name = (f"half{corrida}.txt")

    fid = open(name,"w")
    
    for i in Ns:

        print(f"i = {i}")    
    
        A = matriz_laplaciana(i)
        
        t1 = perf_counter()

        invertir(A)
        
        t2 = perf_counter()

        dt = t2 - t1
        
        size = 3 * (i**2) * 16

        tiempo.append(dt) 
        memoria.append(size)
    
        fid.write(f"{i} {dt} {size}\n")
    
        print(f"Tiempo transcurrido = {dt} s")
        print(f"Mmoria usada = {size} bytes")

        fid.flush()
    
    
fid.close()


