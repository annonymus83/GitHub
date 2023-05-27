# PYTHON

## Instalacion

Entramos al sig. link https://www.python.org/
Seleccionamos *downloads*, y pinchamos en *Download for Windows* -> `Phyton 3.11.3`

En windows 11 viene por defecto instalado una version de phyton, en ese caso nos
aparecera la opcion _upgrape Now_ . lo Pinchamos.
Luego seleccionamos _Disable path length limit_ -> Yes -> Close

Cerramos todo. Vamos a nuestro Inicio y buscamos la palabra **cmd** (es nuestra linea de 
comandos) y lo pinchamos. Escribimos `Python`, -> ENTER y nos aparecerá la version de python 
que instalamos y Listo. 

NOTAS:
Para escrbir codigo utlizaremos un ***editor de texto*** o un ***IDE***. La diferencia de estos 
dos es que el IDE tiene mas herramientas que un Editor de texto (Autocompletado, Debugging, Testing).

### FUNCIONES DE PHYTON
print() : imprime en la terminal los datos que deseemos 

EJECUTAR EN PHYTON
Abrimos una terminal escribimos `python nombreDeArchivo`
-> Enter y listo

### VARIABLES
Integer : señala a los nros enteros ej:
alumnos = 5000 (_esto es una variable_)

Float : señala a los decimales ej:
promedio = 9.9 

Bool : señala a los valores True o False ej:
publicados = True

## Strings
`"string"` : con doble comilla "" puedo señalar un strings (texto/s)

`""" string tipo parrafo o verso"""` : con triple comilla puedo señalar una descripcion larga o corta.

`len(variable)` :me dice la cantidad de caracteres que tiene una variable . ej de uso ; _print(len(ejemplo_de_variable))_

`variable[i]` me da el i-esimo caracter de mi varaible. ej de uso; _print(variable[0])_ . i peretenece NU{0}
 
`variable[i:l]` : me desde i hasta l caracteres de una variable.

`+` : con este simbolo podemos concatenar dos o mas strings

`f"{string/variable} {string2/variable2}"` :formateo de strings, cumple la misma funcion de concatenar 
(solo que mas limpio). Ademas lo que esté entre {} podemos escribir la expresion que deseemos ej. variable[0] , 2+5..

NOTA: `f"... {...} ..." ` la f es muy importante, para que funciones lo que este entre llaves{}

METODOS SOBRE VARIABLES STRINGS
`upper()`  :su funcion es pasar string/s a mayusculas. Ej: 
            _print(variable.upper())_

`lower()`  :su funcion es pasar strings a minusculas

`capitalize()` :toma el primer caracter lo pasa en Mayus, y el resto lo deja en Minus (se usa de la 
                misma forma que upper)

`title()`  :a cad string lo comvierte a un capitalize. (se usa de la misma forma que upper) 


SECUENCIAS DE ESCAPE
var = 'Quiero "entrecomillar" una variable' : puedo definir una var con comillas dentro de las comillas de 
                                        esa manera

**otra forma es**: "quiero \"entrecomillar\"" : \ me dice que lo q esta a mi derecha es un caracter

### NUMEROS 
TIPOS: Integer, Float

ejemplos: n/t = Float.   Pero n//t = Int (me devuelve la parte entera)

FUNCIONES
Para utlizar mas variedad de funciones podemos importar un modulo: `import math`
https://docs.python.org/es/3.10/library/ este link me lleva a todas las func. de math

`round(x)` : redondea a un entero un float
`abs(x)` :nos da el vbalor absoluto de x

Ejemplos con `import.math`

**print(math.ceil(x))**  ->nos lleva al numero sup entero mas cercano de x 

**print(math.floor(x))** ->nos lleva al numero inferior entero mas cercano de x 

**print(math.pox(b, p))**  ->eleva b a la n 

**print(math.sqrt(x))**  -> raiz cuadrada de x

INPUT----------------------------

n1 = input("ingresa primer numero")
n2 = input("ingresa primer numero")

Aqui el input me indica que parametros de entrada voy a querer (ejecutar en la terminal y 
ver lo que sucede)

ejemplos:
``` python
n1 = input("ingresa primer numero")
n2 = input("ingresa primer numero")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2}
el resultado de la suma es {suma}.
el resultado de la resta es {resta}.
el resultado de la multiplicacion es {multi}.
el resultado de la division es {div}.
"""

print(mensaje)
```

