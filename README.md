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
  * Marca / Modelo: Intel(R) HD Graphics 4000
  * Memoria dedicada: 2.00 GB
  * Resolución: 1366 x 768 x 39 hercios
* Disco 1: 
  * Marca: JMCR SD 
  * Tipo: Removable Media
  * Tamaño:14.83 GB (15.924.142.080 bytes) 
  * Particiones: Disco #1, particion #0
  * Sistema de archivos:
* Disco 2: 
  * Marca:Samsung
  * Tipo: Disco duro fijo
  * Tamaño: 119.24 GB
  * Particiones: Disco #0, particiom #1
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

# P0E3 - Desempeño INV
![1double](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2021-P0/main/Graficos%20Entrega3/Rendimiento%20caso1_double.png)
![1half](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2021-P0/main/Graficos%20Entrega3/half_error.PNG)
![1long](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2021-P0/main/Graficos%20Entrega3/Rendimiento%20caso1_longdouble.png)
![1single](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2021-P0/main/Graficos%20Entrega3/Rendimiento%20caso1_single.png)
 
![2double](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso2_double.png)
![2half](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso2_half.png)
![2long](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso2_longdouble.png)
![2single](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso2_single.png)

![3double](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso3_double.png)
![3half](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso3_half.png)
![3long](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso3_longdouble.png)
![3single](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso3_single.png)

Observaciones:
En primer lugar en relacion al caso 1 half, se puede ver en la imagen que este caso no corrio en mi computador.
En segundolugar el caso 2 double erroja un error de falta de memoria para el caso 2 double para matrices de N=10000
EN tercer lugar el caso 3 double y 3 half presentan el mismo problema de falta de memoria para llegando a N=3000 y N=5000 respectivamente

Al comparar los graficos se puede ver que la opcion overwrite_a=True(caso3) mejora el desempeño vs la opcionoverwrite_a=False(caso2). Ya que en los casos mas criticos como lo son matrices de N=10000, podemos ver que el tiempo en el caso 3 es menor.

# P0E4 - Desempeño de SOLVE y EIGH



