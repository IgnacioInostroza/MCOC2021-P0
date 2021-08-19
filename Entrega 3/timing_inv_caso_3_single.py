# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:11:44 2021

@author: ignacio
"""

import matplotlib.pyplot as plt
from scipy import linalg
from time import perf_counter
import numpy as np

def matriz_laplaciana(N, t=np.single):    # funcion obtenida de clase
    e=np.eye(N)-np.eye(N,N,1)
    return t(e+e.T)


Ns = [2, 5, 10,12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000, 10000]

corridas = 10

for corrida in range(corridas):
    
    tiempo = []
    memoria = []
    
    name = (f"single3{corrida}.txt")

    fid = open(name,"w")
    
    for i in Ns:

        print(f"i = {i}")    
    
        A = matriz_laplaciana(i)
        
        t1 = perf_counter()

        A1 = linalg.inv(A, overwrite_a=True)
        
        t2 = perf_counter()

        dt = t2 - t1
        
        size = 3 * (i**2) * 32

        tiempo.append(dt) 
        memoria.append(size)
    
        fid.write(f"{i} {dt} {size}\n")
    
        print(f"Tiempo transcurrido = {dt} s")
        print(f"Mmoria usada = {size} bytes")

        fid.flush()
    
    
fid.close()



dim = []
tim = []
mem = []

for n in range(10):
    dimension = []
    time = []
    memory = []
    with open(f"single3{n}.txt", "r") as f:
        lineas = [linea.split() for linea in f]
        
    for i in lineas:
        dimension.append(int(i[0]))
        time.append(float(i[1]))
        memory.append(int(i[2]))
    
    dim.append(dimension)
    tim.append(time)
    mem.append(memory)

#Grafico superior

plt.subplot(2, 1, 1)
plt.plot(dim[0],tim[0],"-o")
plt.plot(dim[0],tim[1],"-o")
plt.plot(dim[0],tim[2],"-o")
plt.plot(dim[0],tim[3],"-o")
plt.plot(dim[0],tim[4],"-o")
plt.plot(dim[0],tim[5],"-o")
plt.plot(dim[0],tim[6],"-o")
plt.plot(dim[0],tim[7],"-o")
plt.plot(dim[0],tim[8],"-o")
plt.plot(dim[0],tim[9],"-o")
    
plt.yscale('log')
plt.xscale('log')

xticks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
xtext = ["", "", "", "", "", "", "", "", "", "", ""]

yticks = [0.1/1000, 1/1000, 10/1000, 0.1, 1, 10, 60, 600]
ytext = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

plt.yticks(yticks, ytext)
plt.xticks(xticks, xtext)

plt.title("Rendimiento caso3_single")
plt.ylabel("Tiempo transcurrido (s)")
plt.grid(True)

#Grafico inferior 

plt.subplot(2, 1, 2)

plt.plot(Ns,memoria,'-ob')

plt.yscale('log')
plt.xscale('log')

xticks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
xtext = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

yticks = [1000,10000, 100000, 1000000, 10000000, 100000000, 1000000000, 100000000000]
ytext = ["1 KB ", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]

plt.axhline(y=4000000000, linestyle="--",color="black") # RAM 4 GB

plt.yticks(yticks, ytext)
plt.xticks(xticks, xtext, rotation=45)

plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria (bytes)")
plt.grid(True)
plt.savefig("Rendimiento caso3_single.png")