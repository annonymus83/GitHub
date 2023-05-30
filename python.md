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
n2 = input("ingresa segundo numero")

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

### CONVERSION DE TIPOS
int()
float()
str()
bool() : se divide en 
    Falsy : - "" (string vacio es false), - None (es false), - 0 (cero es false)

    Truthy : todo es True si no es un Falsy

## LOGICA PROPOSICIONAL 
### COMPARADORES LOGICOS
- < menor
- > mayor
- <= menor o igual
- >= mayor o igual
- == igualdad
- !=  (not igual) o desigualdad

**sentencias condicionales**

- if (expresion):
     bloque de instruc.Por SI CUMPLE con la expresion

- elif (expresion1):
     bloque de instruc.Por SI CUMPLE con la expresion1

- else :
       bloque de instruc.Por si NO CUMPLE con la expresion 

NOTA: Elif son un monton de if's & puedes usar tantos como quieras, else 
es solo al final & significa si nada entra entonces usa esto

_ejemplo_
``` python
edad = 60
if edad > 17:
    print("puede ver la pelicula")
elif edad > 54:
    print("puede ver la peli con descuento")
else:
    print("no puedes entrar")

print("Listo")

```

#### OPERADOR TERNARIO
Forma mas corta de escribir una condicion
``` python
edad = 15
mensaje = "Es mayor" if edad > 17 else "es menor"
print(mensaje)
```
### OPERADORES LOGICOS

* AND : p and q => True (si se cumple las dos prep)

* OR : p or q => True (si se cumple una prep)

* NOT : negacion

EJEMPLO:
``` python
gas = True
encendido = True
edad1 = 18

if gas and encendido:
    print("Puedes avanzar")

#otro ejplo
if not gas and (encendido or edad > 17):
    print("Puedes avanzar")

```

### CADENA DE COMPARADORES 
Podemos escribir de una forma mas corta un if con comp.logicos
__ejemplo:__
``` python
if edad >= 15 and edad <= 65:
    print("puede entrar a la piscina")
```
otro caso: 
``` python
if 15 <= edad <= 65:
    print("puede entrar a la piscina")
```

## ITERACION

> **FOR**: se utiliza para iterar sobre una objeto iterable y ejecutar un bloque de código 
para cada elemento en la secuencia de dicho objeto

**For else**: por si no sucede el ciclo for

¿que son iterables? que lo podemos recorrer usando un ciclo. Como
* Listas
* tuplas
* numeros ( utilizando range(n) que de 0 a n-1)
* Strings

ejemplo basico
``` python
buscar = 3

for numeros in range(5):
    print(numeros)
    if numeros == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontre nro buscado :(")

for char in "Ultimate python":
    print(char)
```


> **WHILE** : hace que se ejecute un bloque de código repetidamente 
mientras una condición sea verdadera

EJEMPLO:
```python
numero = 1

while numero < 100:
    print(numero)
    numero *= 2
```
consola me devuelve: >> 1  , 2  , 4 , 8, 16 , 32 , 64

**Loops anidados**: un for dentro de un for:
ejemplo: 
```python
for j in range(3):  #---> outer for/loop luego se cumple este ciclo
    for k in range(2):  #---> inner for/loop: primero se cumple este ciclo
        print(f"{j}, {k}")
```




## FUNCIONES
> Funcion:es un bloque de líneas de código o un conjunto de instrucciones cuya 
finalidad es realizar una tarea específica.

`**def**` : se utiliza para definir mi funcion, seguido del nombre de la funcion y 
su bloque de instrucciones.

Nota: para llamar a mi funcion solo escribo (en el editor) `nombreDelafuncion`

Ejemplo:
``` python
def hola():
    print("Hola Mundo")
    print("Ultimate python")

hola()
```

### PARAMETROS Y ARGUMENTOS

>**Parametro** : son los valores que la función puede recibir. Estos parámetros se definen
dentro de los paréntesis que van justo después de declarar el nombre de la función.

>**Argumento** : se considera a los valores del parametro.

ejemplo: 
```python
def holas(nombreDeUs):
    print("Hola Mundo")
    print(f"Bienvenido {nombreDeUs}")

holas("Chanchito Feliz")
```

NOTA: si quiero mas paramtros simplemente lo agrego separandolo con comas
: nombrefuncion( parametro1, parametro2)

> Podemos Agregar valores por Defecto a mi parametro:

``` python
def hola(nombre, apellido="Feliz"):
    print(f"Hola Mundo Bienvenido {nombre} {apellido}" )

hola("Nico", "Schurmann")
hola("Chanchito")
```
Consola: >> Hola Mundo Bienvenido Nico Schurmann
            Hola Mundo Bienvenido Chanchito Feliz



>**Arguemntos Nombrados** : En caso de que me olvide el orden los paramteros 
de mi funcion puedo especificar el parametro de cada argumento sin importar 
el orden de mi funcion.

EJEMPLO:
```python
hola(apellido="Schurmann", nombre="Nico")
```

### X-ARGS
Ayuda a que se pueda agregar la cantidad de argumento que queramos auna función,
sin tener que agregar multiples parametros.
Para Ello: mi parametro se convierte en un _iterable_ si le agrego un **"*"** adelante.


EJEMPLO:
```python
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2,5,7)
suma(2,5)
suma(2,8,7,45,32)
```
consola:>>  14   ,  7  , 94

### RETURN
> **Return**: termina la ejecución de una función y devuelve el control a la función de llamada.
Puede devolver un valor a la función de llamada 

EJEMPLO: quiero utilizar el res de una funcion para asignarlo a una variable.
Nota: los return no imprimen nada en la terminal.

```python
def suma(a, b):
    res = a + b
    return res

c = suma(1, 2)
d = suma(c, 2)

print(d)
```

### ALCANCE
>**Local**: variables locales son aquellas definidas dentro de una función.
Solamente son accesibles desde la propia función y dejan de existir cuando esta 
termina su ejecución

>**Global**: son aquellas vars. definidas en el cuerpo principal del programa 
fuera de cualquier función. Son accesibles desde cualquier punto del programa, 
incluso desde dentro de funciones. 

### DEPURANDO FUNCIONES
 

