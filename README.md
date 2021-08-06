# MCOC2021-P0

# Mi computador principal

* Marca/modelo: HP EliteBook Revove 810 G1
* Tipo: Notebook
* Año adquisición: 2013
* Procesador:
  * Marca/Modelo: Intel(R) Core(TM) i5-3437U
  * Velocidad Base: 2.40 GHz
  * Numero de núcleos: 2 
  * Numero de hilos: 
  * Arquitectura:x64 
  * Set de instrucciones: 
* Tamaño de las cachés del procesador
  * L1: 128 kB
  * L2: 512 kB
  * L3: 3.0 MB
* Memoria 
  * Total:
  * Tipo memoria: 
  * Velocidad:
  * Numero de (SO)DIMM: 
* Tarjeta Gráfica
  * Marca / Modelo:
  * Memoria dedicada:
  * Resolución: 
* Disco 1: 
  * Marca: 
  * Tipo: 
  * Tamaño: 
  * Particiones: 
  * Sistema de archivos:
* Disco 2: 
  * Marca:
  * Tipo: 
  * Tamaño: 
  * Particiones: 
  * Sistema de archivos:
* Disco 3: 
  * Marca:
  * Tipo: 
  * Tamaño: 
  * Particiones: 
  * Sistema de archivos:
* Proveedor internet: Entel Fibra Optica

# Desempeño MATMUL

![Rendimiento](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2021-P0/main/Rendimiento_A%40B.png)

(Mi codigo genera un archivo de texto para cada corrida, por lo cual solo subi tres archivos de texto correspondientes a las corridas 4, 6 y 8. Por otra parte el script de visualizacion de resultados se encuentra dentro del script timing_matmul.py)

* ¿Como difiere del grafico del profesor/ayudante?  

Como se puede apreciar en el grafico, una de las diferencias es que para la multiplicacion de matrices de N=10000 el computador del profesor se demora un tiempo cercano a los 10 segundos, mientras que mi computador se demora un tiempo mayor a un minuto. 

Otra diferencia notoria es el rango de tamaños de matrices en los cuales el grafico presenta un comportaminto oscilatorio en el tiempo de operacion. Como podemos ver en el grafico del profesor, este comportamiento se da en matrices de tamaños de N=50 a N=500, mientras que en mi computador este comportamiento oscilatorio se presenta en matrices de  tamaño N= 10 a N=50.

Por otra parte podemos ver que para el grafico de memoria utilizada, la linea de memoria limite en el grafico del profesor es a los 32 GB, mientras que el limite en mi grafico es a los 4 GB, ya que es la memoria RAM de mi computador.

* ¿A que se pueden deber las diferencias?  

Las diferencias entre las corrridas del profesor con las mias, se puede deber a las especificaciones de cada computador, diferencias en el procesador y cantidad de núcleos e hilos.
Por otra parte, las diferencias entre corridas realizadas en un mismo computador se debe a que este en cada corrida va optimizando recursos, lo cual produce estas variaciones, haciendose mas notorias en tamaños intermedios de matrices.

* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porque puede ser? 
 
El grafico de uso de memoria es lineal, ya que el uso de memoria correspone al tamaño de la matriz en bytes, independientemente del tiempo que demore en ejecutar o los numeros que esta contenga, los bytes ocupados seran los mismos para un mismo tamaño de matriz N.

* ¿Qué version de python esta usando?  

La versión de python que estoy usando es la 3.8.3.

* ¿Qué version de numpy esta usando?  

La version de numpy que estoy usando es la 1.18.5.

![Version](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2021-P0/main/Version.PNG)

* Durante la ejecucion de su código ¿se utiliza mas de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar.

Como podemos ver en la imagen siguiente, se utilizan 4 procesadores logicos.

![Uso](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2021-P0/main/Uso.PNG)


 




