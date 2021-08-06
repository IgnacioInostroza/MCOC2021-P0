# MCOC2021-P0

# Mi computador principal

* Marca/modelo: HP EliteBook Revove 810 G1
* Tipo: Notebook
* Año adquisición: 2013
* Procesador:
  * Marca/Modelo: Intel(R) Core(TM) i5-3437U
  * Velocidad Base: 4.00 GHz
  * Velocidad Máxima: 4.40 GHz
  * Numero de núcleos: 4 
  * Humero de hilos: 
  * Arquitectura:x64 
  * Set de instrucciones: 
* Tamaño de las cachés del procesador
  * L1d: 32KB
  * L1i: 32KB
  * L2: 256KB
  * L3: 8192KB
* Memoria 
  * Total: 32 GB
  * Tipo memoria: DDR3
  * Velocidad 1867 MHz
  * Numero de (SO)DIMM: 4
* Tarjeta Gráfica
  * Marca / Modelo: Nvidia GeForce GTX 980M
  * Memoria dedicada: 8192 MB
  * Resolución: 1920 x 1080
* Disco 1: 
  * Marca: Samsung
  * Tipo: SSD
  * Tamaño: 1TB
  * Particiones: 4
  * Sistema de archivos: EXT4, swap
* Disco 2: 
  * Marca: Samsung
  * Tipo: SSD
  * Tamaño: 1TB
  * Particiones: 1
  * Sistema de archivos: EXT4
* Disco 3: 
  * Marca: Samsung
  * Tipo: SSD
  * Tamaño: 1TB
  * Particiones: 1
  * Sistema de archivos: EXT4
  
* Dirección MAC de la tarjeta wifi: 5C:E0:C5:D7:EE:48 
* Dirección IP (Interna, del router): 192.168.0.129
* Dirección IP (Externa, del ISP): 190.45.122.34
* Proveedor internet: Entel Fibra Optica

# Desempeño MATMUL

![Rendimiento](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2021-P0/main/Rendimiento_A%40B.png)

* ¿Como difiere del gráfico del profesor/ayudante?  

Como se puede apreciar en el grafico, una de las diferencias es que para la multiplicacion de matrices de N=10000 el computador del profesor se demora un tiempo cercano a los 10 segundos, mientras que mi computador se demora un tiempo mayor a un minuto. 

Otra diferencia notoria es el rango de tamaños de matrices en los cuales el grafico presenta un comportaminto oscilatorio en el tiempo de operacion. Como podemos ver en el grafico del profesor, este comportamiento se da en matrices de tamaños de N=50 a N=500, mientras que en mi computador este comportamiento oscilatorio se presenta en matrices de  tamaño N= 10 a N=50.

Por otra parte podemos ver que para el grafico de memoria utilizada, la linea de memoria limite en el grafico del profesor es a los 32 GB, mientras que el limite en mi grafico es a los 4 GB, ya que es la memoria RAM de mi computador.

* ¿A qué se pueden deber las diferencias?  
Las diferencias entre las corrridas del profesor con las mias, se puede deber a las especificaciones de cada computador, diferencias en el procesador y cantidad de núcleos e hilos.
Por otra parte, las diferencias entre corridas realizadas en un mismo computador se debe a que este en cada corrida va optimizando recursos, lo cual produce estas variaciones, haciendose mas notorias en tamaños intermedios de matrices.

* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?  
El grafico de uso de memoria es lineal, ya que el uso de memoria correspone al tamaño de la matriz en bytes, independientemente del tiempo que demore en ejecutar o los numeros que esta contenga, los bytes ocupados seran los mismos para un mismo tamaño de matriz N.

* ¿Qué versión de python está usando?  
La versión de python que estoy usando es la 3.8.3

* ¿Qué versión de numpy está usando?  
La versión de numpy que estoy usando es la 1.18.5.

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
 




