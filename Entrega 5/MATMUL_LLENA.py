# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 15:45:01 2021

@author: ignacio
"""

from time import perf_counter
import numpy as np
import matplotlib.pyplot as plt


def matriz_laplaciana_llena(N, t=np.double):    # funcion obtenida de clases para formar matriz llena
    e=np.eye(N)-np.eye(N,N,1)
    return t(e+e.T)

N = [2, 5, 10, 15, 20, 30, 45, 50, 60, 75, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000, 8000, 10000]


names = ["MATMUL_llena.txt"]

files = [open(name, "w") for name in names]

for i in N:
    dts1 = np.zeros(len(files))
    dts2 = np.zeros(len(files))
    print(f"N = {i}")
    
        
    # Matriz llena MATMUL

    t1 = perf_counter()
    A = matriz_laplaciana_llena(i)
    B = matriz_laplaciana_llena(i)
    t2 = perf_counter()
    matmul_llena = A@B
    t3 = perf_counter()
    
    dt1 = t2 - t1
    dt2 = t3 - t2
    dts1[0] = dt1
    dts2[0] = dt2
      
    
    for j in range(len(files)):
        files[j].write(f"{i} {dts1[j]} {dts2[j]}\n")
        files[j].flush()
        
[file.close() for file in files]

#-------------------------------------------------------------------------------------------------
#PLOTEO MATMUL LLENA

xticks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
yticks = [0.01/1000, 0.1/1000, 1/1000, 10/1000, 0.1, 1, 10, 60, 600]
yticks_text = ["0.01 ms", "0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
xticks_text = ["", "", "", "", "", "", "", "", "", "", ""]
plt.figure()

dt1max = []
dt2max = []

data = np.loadtxt("MATMUL_llena.txt")
Ns = data[:,0]
dts1 =  data[:,1]
dts2 = data[:, 2]
Nsmax = max(Ns)
dts1max = max(dts1)
dts2max = max(dts2)
    
for i in Ns:
    dt1max.append(max(dts1))
    dt2max.append(max(dts2))
        
#SUBPLOT tiempo de ensamblado
    
plt.subplot(2,1,1) 
plt.ylabel("Tiempo de ensamblado")
plt.loglog(Ns,dts1, 'k-o', alpha = 0.5, markersize = 3) 
plt.grid()
plt.yticks(yticks, yticks_text)
plt.xticks(xticks, xticks_text, rotation=45)
 
plt.plot(Ns, dt1max, "--", color = "royalblue")  
plt.loglog(Ns, Ns*(dts1max/Nsmax), "--", color = "orange") 
plt.loglog(Ns, (Ns**2)*(dts1max/(Nsmax**2)), "--", color = "green") 
plt.loglog(Ns, (Ns**3)*(dts1max/(Nsmax**3)), "--", color = "firebrick") 
plt.loglog(Ns, (Ns**4)*(dts1max/(Nsmax**4)), "--", color = "mediumpurple") 
plt.yticks(yticks, yticks_text)
plt.xticks(xticks, xticks_text, rotation=45)
plt.ylim(0.01/1000, 600) 

#SUBPLOT tiempo de solucion

    
plt.subplot(2,1,2) 
plt.loglog(Ns,dts2, 'k-o', alpha = 0.5, markersize = 3)
plt.ylabel("Tiempo de solucion")
plt.xlabel("Tamaño de la matriz")
plt.grid()
plt.yticks(yticks, yticks_text)
plt.xticks(xticks, xticks, rotation=45)

plt.plot(Ns, dt2max, "--", color = "royalblue", label="Constante")  
plt.loglog(Ns, Ns*(dts2max/Nsmax), "--", color = "orange", label="O(N)") 
plt.loglog(Ns, (Ns**2)*(dts2max/(Nsmax**2)), "--", color = "green", label=r"$O(N^2)$") 
plt.loglog(Ns, (Ns**3)*(dts2max/(Nsmax**3)), "--", color = "firebrick", label=r"$O(N^3)$") 
plt.loglog(Ns, (Ns**4)*(dts2max/(Nsmax**4)), "--", color = "mediumpurple", label=r"$O(N^4)$") 
plt.yticks(yticks, yticks_text)
plt.xticks(xticks, xticks, rotation=45)
plt.ylim(0.01/1000, 600) 

plt.tight_layout()
plt.legend()
plt.savefig("Matmul_llena2.png")



