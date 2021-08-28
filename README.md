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

#### Caso 1

![1double](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2021-P0/main/Graficos%20Entrega3/Rendimiento%20caso1_double.png)
![1half](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2021-P0/main/Graficos%20Entrega3/half_error.PNG)
![1long](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2021-P0/main/Graficos%20Entrega3/Rendimiento%20caso1_longdouble.png)
![1single](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2021-P0/main/Graficos%20Entrega3/Rendimiento%20caso1_single.png)

#### Caso 2 

![2double](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso2_double.png)
![2half](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso2_half.png)
![2long](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso2_longdouble.png)
![2single](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso2_single.png)

#### Caso 3

![3double](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso3_double.png)
![3half](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso3_half.png)
![3long](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso3_longdouble.png)
![3single](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Graficos%20Entrega3/Rendimiento%20caso3_single.png)

**Observaciones:**
En primer lugar en relacion al caso 1 half, se puede ver en la imagen que este caso no corrio en mi computador. Esto se puede deber a que scipy trabaja transformando por ejemplo un dato de tipo  half en single o un dato de tipo double en longdouble, lo cual podria arrojar ese error  
En segundo lugar el caso 2 double erroja un error de falta de memoria para el caso 2 double para matrices de N=10000
EN tercer lugar el caso 3 double y 3 half presentan el mismo problema de falta de memoria, llegando a N=3000 y N=5000 respectivamente

Al comparar los graficos se puede ver que la opcion overwrite_a=True(caso3) mejora el desempeño vs la opcionoverwrite_a=False(caso2). Ya que en los casos mas criticos, como lo son matrices de N=10000, podemos ver que el tiempo en el caso 3 es menor.


# P0E4 - Desempeño de SOLVE y EIGH

#### Desempeño SOLVE dtype=float
![solvesingle](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Entrega%204/Desempe%C3%B1o_SOLVE_single.png)

#### Desempeño SOLVE dtype=double
![solvedouble](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Entrega%204/Desempe%C3%B1o_SOLVE_double.png)

#### Desempeño EIGH dtype=float
![eighsingle](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Entrega%204/Desempe%C3%B1o_EIGH_single.png)

#### Desempeño EIGH dtype=double
![eighdouble](https://github.com/IgnacioInostroza/MCOC2021-P0/blob/main/Entrega%204/Desempe%C3%B1o_EIGH_double.png)

**Observaciones:**

Es importante mencionar que la parte B de esta entrega, los casos II al V se dividieron en dos subcasos, para asi poder representar la opcion de usar overwrite=False(1) y overwrite=True(2). Esto se puede ver reflejado tanto en la leyenda de los graficos EIGH como en los archivos generados para cada tipo de dato.

Otra observacion importante, son los tamaños de matrices evaludas. Escribi un codigo para las funciones SOLVE y otro para las EIGH, corri ambos codigos para N mayores a 5000 sin embargo luego de dejar corriendo por aproxiadamente 1 hora el codigo, decidi llegar a tamaños menores, ya que por temas tiempo no alcanzaria a realizar 10 corridas para matrices de tamaños superiores, ademas de no quise sobre exigir mi computador. Debido a esto, con la funcion SOLVE solo corri hasta N=5000 y con la funcion EIGH llegue hasta N=2000, lo cual me permitio realizar un analisis de desempeño de igual manera.

¿Como es la variabilidad del tiempo de ejecucion para cada algoritmo? ¿Qué algoritmo gana (en promedio) en cada caso? ¿Depende del tamaño de la matriz? 

Al hacer un analisis de de la variabilidad del tiempo en los algoritmos que resuelven el sistema lineal Ax=b, podemos ver que el algoritmo que invierte la matriz A para luego multiplicarla por el vector b, presenta un mejor desempeño en matrices con un N menor a 20 para los dos tipos de datos (float y double). Sin embargo a medida que aumenta el tamaño N de la matriz, podemos ver que el mejor desempeño lo presenta la funcion **scipy.linalg.solve usando assume_a='pos'**(caso A.III), para los dos tipos de datos (float y double).

Por otro lado, si analizamos el desempeño de los algoritmos que resuelven el problema de valores y vectores propios (EIGH), podemos ver que para matrices con N menor a 20, la funcion que presenta un mejor desempeño es la funcion **scipy.linalg.eigh con driver="evx" y overwrite=True**(caso B.V_2). Sim embargo para matrices con N mayor a 20 esta funcion se combierte en la funcion con mejor desempeño. La funcion con un peor desemepño para matrices pequeñas fue la funcion **Usar scipy.linalg.eigh con parámetros por defecto**(caso B.I). Como podemos ver en los graficos, el tipo de dato no influye en el desempeño de las distintas funciones.

Si realizamos una comparacion mas detallada, tamando por ejemplo el caso B.II_1 (**scipy.linalg.eigh con driver="ev" y overwrite=False**) con el caso B.II_2(**scipy.linalg.eigh con driver="ev" y overwrite=True**) podemos ver que la variabilidad del tiempo es casi nula, ya que si evaluamos el tiempo que demora el caso B.II_1 en operar una matriz de tamaño N=2000 es de 5.1329s mientras que el caso B.II_2 se demora 5.1046s. Por lo tanto podemos decir que hay funciones en las cuales el cambiar un parametro no implica una mejora significativa en el desempeño.

¿A que se puede deber la superioridad de cada opción?

Como se menciono anteriormente, el desempeño del algoritmo que primero invierte la matriz para lugeo multiplicarla, fue mejor que el de otras funciones predeterminadas, a diferencia de lo que se esperaba. Esto se puede deber a el tamaño de matrices, mientras menor sea el tamaño, el computador se comportara de manera mas variable optimizando sus recursos de diferentes maneras, ya que tiene mas opciones o mas memoria disponible. Por otra parte si nos fijamos en tamaños mas grandes de matrices, podemos ver que los desempeños son bastante parecidos entre cada funcion. 

¿Que hay del uso de memoria (como crece)?

El uso de memoria, como se puedo ver en la Entrega3, crece junto con el tamaño N de la matriz que se este operando. El uso de memoria depende netamente del tipo de dato que se esta usando para armar las matrices y es independiente del algoritmo o funcion empleada para la operacion. 

# P0E5 - Matrices dispersas y complejidad computacional

#### Complejidad algorítmica de MATMUL

#### Matriz LLena
![Matmulllena]()

#### Matriz Dispersa
![Matmuldispersa]()

