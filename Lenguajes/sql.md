# Introducción

**¿Qué es SQL?**
Es un lenguaje de computación utilizado para el manejo de información en bases de datos relacionales.

## SOFTWARE DE GESTION DE BASE DE DATOS

RDBMS : "sistema de administración de bases de datos relacionales" es un programa que se usa para crear,
actualizar y administrar bases de datos relacionales. Algunos de ellos son
* MySQL
* Postgres
* MariaDB
* Oracle
* Infornix

### Operaciones comunes:
**C**reate : crea base de datos, tablas ... ej:
`create database nombre_base_de_datos;`

**R**ead

**U**pdate

**D**elete

Si quiero ver todas las bases de datos:
`show databases;`

### Tipos

|      SQL      |    No-SQL     |
| ------------- | ------------- |
| suelen almacenar información en tablas | almacenan de diversas formas por ej en formato json, bson, blob, key-value |


### Características

- Una tabla debe tener una columna ID (nro identificativo único). Tipos:
    - PRIMARY KEY: identifica de forma única cada registro en una tabla (lo que esta en la columna ID)
    - FOREIGN KEY: un Id dentro de una tabla (es decir son id que se guarda en alguna columna distinta de ID), se pueden repetir.

## TABLAS

### COLUMNAS

---

**SELECT**

Podemos consultar todos los datos de una tabla:

``` MySQL
SELECT * FROM nombre_tabla;
```

> [!NOTE]
> utilizamos * para seleccionar todas las columnas de la tabla
> SQL es un lenguaje insensible a las mayúsculas SELECT = select


Tambien podemos seleccionar una única columna de la tabla.

``` MySQL
SELECT nombre_de_columna FROM nombre_tabla;
```

O seleccionar múltiples columnas de una tabla:

``` MySQL
SELECT nombre_col1, nombre_col2 FROM nombre_tabla;
```

**AS**

Pdemos asignar un alias o nombre alternativo a una columna en el resultado de la consulta, utilizando la cláusula AS.

``` MySQL
SELECT col1 AS col_nombre1 FROM nombre_tabla;
```


Podemos utilizar la cláusula AS junto con *comillas dobles* para cambiar el nombre de una columna  a uno más descriptivo o que contenga espacios o tildes en los resultados de una consulta

``` MySQL
SELECT col1 AS "Nombre de columna1" FROM nombre_tabla;
```


Se puede cambiar el nombre a múltiples columnas en la misma consulta

``` MySQL
SELECT col1 AS col_nombre1, col2 AS col_nombre2 FROM nombre_tabla;
```


### FILAS

------

**WHERE**

Esta cláusula se utiliza para filtrar los registros de una tabla según una condición específica.
Ej;

``` MySQL
SELECT * FROM productos WHERE precio > 100;
```

>[!NOTE]
> Un detalle importante es que las claúsulas tienen un orden.
>1. select,
>2. from
>3. where

Operandos: **> , >= , < , <= , =**


Tambien podemos seleccionar algunas columnas;

``` MySQL
SELECT col1, col2 FROM nombre_tabla WHERE col1 > x;
```
 
 
**String** : Para comparar textos debemos utilizar comillas simples ('') o comillas dobles (""):

``` MySQL
SELECT * FROM nombre_tabla WHERE col1 = 'Strings';
```


**Booleanos** : columnas con bools (true o false, o reciprocamente 1 o 0):

``` MySQL
SELECT * FROM nombre_tabla WHERE col1 = bool;
```


**AND** : La claúsula WHERE se puede combinar con el operador AND para juntar múltiples condiciones en una consulta SQL. Ej:

``` MySQL
SELECT * FROM nombre_tabla WHERE condicion1 AND condicion2;
```


**OR** : al menos una de las condiciones debe ser verdadera para que el registro se incluya en el resultado.

``` MySQL
SELECT * FROM nombre_tabla WHERE condicion1 OR condicion2;
```


**DATE** : es un tipo de dato para fechas con formato YYYY-MM-DD , ej:

``` MySQL
SELECT * FROM nombre_tabla WHERE col_fecha >= '2022-01-01';
```


**BETWEEN** : este operador se utiliza para seleccionar registros cuyos valores se encuentren dentro de un rango específico

``` MySQL
SELECT * FROM nombre_tabla WHERE col1 BETWEEN x AND y ;
```


**LIKE** : Sup. que queremos buscar todos los usuarios cuyo nombre empiece con la letra 'J' en la tabla de usuarios. Podemos hacer lo siguiente:

``` MySQL
SELECT * FROM usuarios WHERE nombre LIKE 'J%';
```

>[!NOTE]
> El símbolo '%' es un comodín que representa cualquier cantidad de caracteres adicionales

**Nulos** : Algunos registros pueden tener valores nulos para algunos de sus campos, por ello tendremos dos funciones:
* **IS NOT NULL** : para seleccionar valores no nulos
    ``` MySQL
    SELECT * FROM nombre_tabla WHERE columna IS NOT NULL;
    ```

* **IS NULL** : para seleccionar valores nulos
    ``` MySQL
    SELECT * FROM nombre_tabla WHERE columna IS NULL;
    ```


### ORDEN

------

**ORDER BY**

Esta cláusula se utiliza para ordenar los resultados de una consulta según una o más columnas. Por defecto, se ordena de forma ascendente.
Aunque tambien podemos especificar el orden con las plabras claves ASC o DESC

```MySQL
SELECT * FROM tabla ORDER BY columna;
```
lo que es lo mismo que :
```MySQL
SELECT * FROM tabla ORDER BY columna ASC;
```

Luego tenemos el orden descendente:
```MySQL
SELECT * FROM tabla ORDER BY columna DESC;
```


Podemos seleccionar más de una columna a ordenar:
```MySQL
SELECT * FROM tabla ORDER BY col1, col2;
```

>[!NOTE]
>Es importante tener en cuenta que las claúsulas tienen que especificarse justo en este orden:
>1. SELECT
>2. FROM
>3. ORDER BY
>
>El orden de los resultados dependerá del tipo de dato: los números se ordenan de menor a mayor, los textos alfabéticamente y las fechas cronológicamente.

**Nulos** : Si deseamos que los valores nulos queden al principio o al final de la lista independiente de en cual direccion ordenemos. Tenemos dos funciones:

* **NULLS FIRST** : se muestran los nulos primeros

    ```MySQL
    SELECT * FROM tabla ORDER BY columna NULLS FIRST;
    ```

* **NULLS LAST** : se muestran los nulos al final

    ```MySQL
    SELECT * FROM tabla ORDER BY columna NULLS LAST;
    ```


**LIMIT**

Esta cláusula se utiliza para limitar la cantidad de resultados devueltos por una consulta. 

Por ej; si queremos obtener sólo los primeros x registros de una tabla:

```MySQL
SELECT * FROM tabla LIMIT x;
```

>[!NOTE]
> La cláusula LIMIT se agrega al final de la consulta.

### OPERACIONES CON STRINGS

---

**UPPER()** : Para transformar un string a mayúsculas en SQLITE;

```MySQL
SELECT UPPER(columna) FROM nombre_tabla;
```

>[!NOTE]
>La función UPPER() no modifica los datos en la tabla, sólo los transforma para los resultados de la consulta.

También le podemos asignar un alias para evitar confusion:

```MySQL
SELECT UPPER(col) as col_en_mayus FROM nombre_tabla;
```


**LOWER()** : en SQLite convierte todos los caracteres de un texto a minúsculas.

```MySQL
SELECT LOWER(col) as col_en_minus FROM nombre_tabla;
```


**TRIM()**: *elimina* los espacios en blanco iniciales y finales de un string

```MySQL
SELECT TRIM(col) FROM nombre_tabla;
```

podemos seleccionar mas de una columna:
```MySQL
SELECT TRIM(col1), TRIM(col2) FROM nombre_tabla;
```

***Combinar funciones***

Podemos combinar funciones como por ej: 

```
SELECT LOWER(TRIM(columna)) AS col_limpia FROM tabla;
```
que convierte en minúscula los registros de la columna y elimina sus espacios.


> [!IMPORTANT]: EL ORDEN EN QUE ESCRIBIMOS AFECTA EL RESULTADO


**LENGTH()** : Obtenemos una columna con la longitud de sus registros:

```MySQL
SELECT LENGTH(columna) FROM tabla;
```

 #### **Concatenar**

 **||** : operador para concatenar strings. Por ej:

```MySQL
SELECT nombre || " " || apellido AS nombre_completo FROM empleados;
```


**SUBSTR( string, inicio, largo )** : para seleccionar una determinada cantidad de caracteres de un string (en sreing va el nombre de la columna) por ej:

```MySQL
SELECT SUBSTR(nombre, 1, 1) AS primera_letra FROM productos;
```

> **NOTA** : algunas funciones tienen distintos nombres dependiendo del motor de base de datos. Por ej en PostgreSQL se usa LEFT()


### OPERACIONES CON FECHA

---

**DATE()** : con esta función podemos obtener la fecha de hoy. Por ej:

```MySQL
SELECT * FROM nombre_tabla WHERE col_con_fecha = DATE();
```

>[!NOTE]
> Esta función puede recibir distintos nombre segun el motor de datos, por ej en MySQL se usa CURDATE(). Cabe aclarar que aqui estamos ocupando SQLite.

**DATE('now', 'x day/week/month')** : se suman fechas para obtener fechas futuras. En SQLite se logra pasando un segundo argumento a la función DATE. Po ej:

```MySQL
SELECT * FROM nombre_tabla WHERE col_con_fecha > DATE('now', '2 week');
```

**DATE('now', '-x day/week/month')** : se restan fechas para obtener fechas pasadas.

```MySQL
/*consulta la tabla con la fecha de ayer */
SELECT * FROM tabla WHERE col_con_fecha = DATE('now', '-1 day');
```


**strftime('%Y')** : función para extraer año

```MySQL
SELECT *,strftime('%Y', col_con_fecha) as col_año FROM tabla;
```

recíprocamente para mes (**%m**), y dia (**%**)

**strftime('%Y-%m')** : me devuelve una columna con año-mes (ej; 2024-1)




### FUNCIONES DE AGREGACIÓN

---

**MAX()** : nos devuelve el valor más alto del campo que especifiquemos.

```MySQL
SELECT MAX(nom_col) FROM tabla;
```
  
  
**MIN()** : devuelve el valor más pequeño del campo que especifiquemos.

```MySQL
SELECT MIN(nom_col) FROM tabla;
```
  
  
**SUM()** : suma todos los elementos de una columna. 

```MySQL
SELECT SUM(nom_col) FROM tabla;
```
 
 
**AVG()** : promedio (average) de una columna.

```MySQL
SELECT AVG(nom_col) FROM tabla;
```
 
 
**COUNT()** : cuenta la cantidad de registros (#filas) que tiene una tabla

```MySQL
SELECT COUNT(*) FROM tabla;
```
 
 
***EJERCICIO***

Podemos tambien combinar con where ej:
``` MySQL
select sum(sueldo) from empleados where edad > 27;
```
 
 
### DISTINCT
---

Es una herramienta útil para eliminar los valores duplicados en una consulta.

``` MySQL
SELECT DISTINCT nom_col as col_unica FROM tabla;
```

Tambien podemos combinar con otras funciones como por ej;
```MySQL
SELECT DISTINC strftime('%m', col_fecha) AS mes_unico FROM tabla;
```

**COUNT(DUSTINCT col)** : Si queremos contar los valores distintos en una columna de una tabla, podemos combinar las funciones COUNT y DISTINCT.

```MySQL
SELECT count(DISTINC col) AS cant_col_unica FROM tabla;
```
 
 
***Distinct con múltiples columnas*** : Podemos usar DISTINCT con más de una columna para obtener combinaciones únicas de esas columnas. 

```MySQL
SELECT DISTINC col1, col2 FROM tabla;
```
 
 
### INTRODUCCIÓN A GRUPOS
---
 
**GROUP BY** : se utiliza para agrupar filas con valores idénticos en una o varias columnas específicas, permitiendo realizar operaciones de agregación en cada grupo.

Aquí cumple la misma funcion que *distinct*

```MySQL
SELECT col as col_unica FROM tabla GROUP BY col;
```


GROUP BY es comúnmente utilizada junto con funciones de agregación como COUNT, MAX, MIN, SUM y AVG para obtener información resumida de un conjunto de datos.


***COUNT*** : Un ejemplo queremos saber cuantas veces se repite un color/es

```MySQL
SELECT color, COUNT(color) as repeticiones FROM tabla GROUP BY color;
```

Reciprocamente funciona para *SUM*, *AVG*, *MAX*, *MIN* 

#### ***Agrupando sin indicar el nombre de las columnas***

Podemos ahorrarnos espacio simplificando nuestra consulta, por ej

```MySQL
SELECT strftime("%Y", fecha_venta) AS año, SUM(monto) FROM ventas GROUP BY strftime("%Y", fecha_venta)
```

simplifica como:

```MySQL
SELECT strftime("%Y", fecha_venta) AS año, SUM(monto) FROM ventas GROUP BY 1
```

quiere decir "agrupa por el primer criterio".


SINTAXIS GRAL PARA MAS COLUMNAS:

```MySQL
SELECT col1, col2 , func_agrupacion(col3) FROM tabla GROUP BY 1,2;
```


### HAVING
---

Se emplea para filtrar los resultados de una consulta que involucra funciones agregadas. Es decir, HAVING permite aplicar condiciones de filtrado a los resultados de funciones como COUNT, MAX, MIN, SUM y AVG después de que se han agrupado los datos con la cláusula GROUP BY.

ejemplo:
```MySQL
SELECT strftime("%m", Fecha_Inscripcion) AS mes, COUNT(Fecha_Inscripcion) cantidad_usuarios 
FROM inscripciones GROUP BY 1 HAVING cantidad_usuarios >= 2;
```

>[!NOTE]
>Notar que no utilizamos AS para crear la columna cantidad_usuarios, es lo mismo que agregar AS.


***Having y order*** : habitualmente necesitaremos ordenar grupos según algun criterio especificO, para ello utilizaremos *ORDER BY* con sus respectivas funciones de agregación.
El orden de las clausulas en una consulta debe ser el siguiente:

| ORDEN | CLAUSULA | DESCRIPCIÓN |
|----- | ---- |-----|
| 1 | SELECT | Especifica las columnas que se deben retornar en el resultado. |
| 2 | FROM | Especifica las tablas de las cuales se extraerán los datos. |
| 3 | WHERE | Filtra registros antes de cualquier agregación o agrupación. |
| 4 | GROUP BY | Agrupa registros por una o más columnas. |
| 5 | HAVING | Filtra registros después de la agregación. |
| 6 | ORDER BY | Ordena los registros retornados por una o más columnas. |
| 7 | LIMIT | Limita el número de registros retornados. |

### INTRODUCCIÓN A SUBCONSULTAS

---

"subqueries" : nos permiten utilizar los resultados de una consulta dentro de otra consulta.
   
    
Por ej, seleccionar un sueldo mayor al promedio:
```MySQL
SELECT * FROM empleados WHERE sueldo > (SELECT AVG(sueldo) FROM empleados)
```

**Subconsultas con IN**

**IN** : operador que permite evaluar si una expresión está dentro de una lista de valores.
```MySQL
SELECT * FROM tabla WHERE colum IN (SELECT * FROM otra_tabla)
```

>[!NOTE]
> Entre parentesis ira el conjunto de registros que deseemos, es decir tambien puede escribir como (2,3,4) o ("Maria", "Juan", "Marta").
 
  
**Subconsultas en el FROM**

Es como seleccionar algo dentro de una tabla creada. Por ej, se tiene la tabla ventas que tiene el código de vendedor y el monto de cada venta realizada. Nos piden saber cuanto es el promedio total vendido.

```MySQL
SELECT AVG(total_venta) as promedio_ventas
FROM (
    SELECT empleado_id, SUM(monto) as total_venta
    FROM ventas
    GROUP BY empleado_id
);
```

### COMBINACIÓN DE CONSULTAS

---

**UNION** : este operdaor se utiliza para combinar el resultado de dos o más SELECT en un conjunto de resultados

```MySQL
SELECT columna1, columna2
FROM tabla1 
UNION SELECT columna1, columna2
FROM tabla2;
```
 
  
>[!NOTE]
>Las columnas que se seleccionan en los SELECT deben tener los mismos nombres de columna, secuencia y tipos de datos.
   
 
DATO CURIOSO: Al hacer un union se eliminan automaticamente los duplicado en caso de que existan.
 

**UNION ALL** : Al contrario de union este nos muestra las filas duplicadas

```MySQL
SELECT * FROM tabla1 UNION ALL SELECT * FROM tabla2;
```
 

**INTERSECT** : intersección entre dos SELECT

```MySQL
SELECT col1 FROM clientes1 INTERSECT SELECT col1 FROM clientes2;
```

 
**EXCEPT** : devuelve solo las filas, que estan en la primera consulta pero no en segunda consulta.
 
```MySQL
SELECT col1 FROM Tabla1 EXCEPT SELECT col1 FROM Tabla2;
```
 
 
### INSERCCIÓN DE REGISTROS
 
---
 
#### INSERT
Instrucción que agrega datos nuevos a una tabal existente. Esta instrucción ira acompañada por las palabras claves **INTO** (indica en que tabla queremos insertar) y **VALUES** (especifica los valores a insertar).

```MySQL
INSERT INTO tabla VALUES (val_col1, val_col2, ..., val_coln);
```

***Valores Nulos*** : en el caso de que haya un valor que no queremos especificar colocamos el valor en esa columna como *null*

**AÑADIR UN REGISTRO SEGUN LA COLUMNA**

Podria pasar que no recordemos el orden de la tabla, y por ello existe una forma de colocar los valores a la columna sin importar el orden en la tabla, de la sig forma:

```MySQL
INSERT INTO tabla (col1, col3, col2) VALUES (val_col1, val_col3, val_col2);
```

> **Incluso podriamos no especificar los valores y estos se complementaran con nulos por defecto al mencionar las columnas** 
 
ej;
```MySQL
INSERT INTO tabla (col1, col3) VALUES (val_col1, val_col3);
```

**CURRENT_DATE** : Es el valor de la fecha de hoy

```MySQL
INSERT INTO tabla (col1, col_fecha) VALUES (val_col1, CURRENT_DATE);
```

En el caso de querer colocar otra fecha el formato de la misma es la siguiente : 'YYYY-MM-DD' 
 
 
**Añadir multiples valores**
```MySQL
INSERT INTO tabla VALUES (val1, val2), (val3, val4);
```

#### **REGISTRO CON CAMPO AUTOINCREMENTAL** :
Podriamos facilitar la insercción de datos en una tabla mediante la declaración de campos incrementales, por ej el "ID". Para ello utilizaremos la cláusula **INCREMENT**. 

Ej:

```MySQL
CREATE TABLE empleados (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT,apellido TEXT);
```

De esta forma a la hora de insertar no sera necesario aclarar el id. 
[Primary Key](SQL#caracter%C3%ADsticas)

#### **REGISTRO CON VALOR POR DEFECTO**
Palabra clave a utlizar es **DEAFULT** que insertara por defecto el valor que indiquemos si es que no declaramos el valor de su respectiva columna a la hora de insertar.

```MySQL
CREATE TABLE tabla (ID INTEGER PRIMARY KEY AUTOINCREMENT, col1 TEXT, col2 INTEGER DEFAULT 10);
```


### BORRAR REGISTROS

#### **DELETE**
Elimina de forma definitiva los registros de una tabla, para eliminar todos los registros de una tabla, escribimos:

```MySQL
DELETE FROM nombre_tabla;
```
 
  
**Borrar un registro con WHERE**
Con ayuda del where podremos eliminar filas especificas, es decir aquellas que cumplan cierta condicón:

```MySQL
DELETE FROM tabla WHERE condicion;
```
 
#### **UPDATE**
Esta sentencia sirve para realizar modificaciones en datos ya existentes de una tabla.

```MySQL
UPDATE nombre_tabla SET nombre_columna = nuevo_valor;
```
 
**Editar registro con WHERE** : 

Podemos modificar algunas filas de nuestra tabla con ayuda del WHERE, de esta forma solo se editan auellas filas que cumplan cierta condición.
```MySQL
UPDATE nombre_tabla SET nombre_columna = nuevo_valor WHERE condicion;
```

 
**Editar multiples columnas**

```MySQL
UPDATE tabla
  SET
    col1 = nuevo_valor,
    col2 = nuevo_valor
  WHERE
    condicion;
```

## FUNCIONES BASICAS DE TABLAS

### **CREATE**
Sintaxis para crear una tabla
```MySQL
CREATE TABLE nombre_tabla (name_col1 tipo_de_dato);
```

 
Para multiples columnas
```MySQL
CREATE TABLE nombre_tabla (name_col1 tipo_dato, name_col2 tipo_dato );
```


### **DROP**
Sintaxis para eliminar una tabla
```MySQL
DROP TABLE nombre_tabla; 
```

### **ALTER**
Sentencia utilizada para actualizar una tabla, es decir nos permitira redefinir una tabla, como agregar una columna.

```MySQL
ALTER TABLE nombre_tabla ADD COLUMN col_nueva tipo_dato; 
```

## RESTRICCIONES

("constraints") : a la hora de crear tablas es posible añadir restricciones sobre las columnas para evitar el ingreso de datos que no cumplen cierta condición.

**NOT NULL** : impide valores nulos en una columna.
```SQLite
CREATE TABLE nombre_tabla (
    nombre_col tipo_dato NOT NULL
)
```

**AGREGAR RESTRICCION A UNA TABLA EXISTENTE**:

Tener en cuenta que en SQLite no es posible realizar esta acción de forma directa, en cambio PostgreSQL y en MySQL si lo es.
Entoncs lo que podriamos hacer es lo siguiente :

1. Crear una tabla con resticción
```MySQL
CREATE TABLE tabla_nueva (
    col1 tipo_dato NOT NULL
    col2 tipo_dato
);
```

2. Copiar los datos de la tabla original a la nueva tabla
```SQLite
INSERT INTO tabla_nueva (col1, col2)
    SELECT col1, col2 FROM tabla_vieja;
```

3. Borrar la tabla original
```SQLite
DROP TABLE tabla_vieja;
```
4. Renombrar la nueva tabla con el nombre de la tabla original
```SQLite
ALTER TABLE tabla_nueva RENAME TO tabla_vieja;
```
 
      
*Y Para borrar una ***restriccion***  se cumple los mismos pasos*
 
 
**UNIQUE** : unicidad, evita que hayan duplicados en una columna especifica. Por ej en una columna de mails.
 
```MySQL
CREATE TABLE nombre_tabla (col1 tipo_dato, col2 tipo_dato UNIQUE); 
```

 
**CHECK** : Establece una condición para los valores de una columna

```MySQL
CREATE TABLE nombre_tabla (
    col1 tipo_dato, 
    col2 tipo_dato CHECK (condicion) 
); 
```
.
.
### **PRIMARY KEY** : Identifica de forma unica cada registro en una tabla, impidiendo el ingreso de duplicados o nulos en esa columna.

```MySQL
CREATE TABLE nombre_tabla (
    col1 tipo_dato PRIMARY KEY, 
    col2 tipo_dato 
); 
```

***AUTOINCREMENTAL*** : Con el campo autoincremental en los registros nos ahorramos en escribir sobre la columna id primary key. En SQLite no es necesario especificar que es autoincremental pues por defecto al escribir INTEGER (o INT) + PRIMARY KEY  se convierte automáticamente en un campo autoincremental
.
.
***PRIMARY KEY y TEXTO*** : En SQLite no se permite números nulos, en cambio cuando hablamos de textos este caso si es permitido. Por ello utilizaremos la siguiente sintaxis, para asi evitar textos nulos.

```MySQL
CREATE TABLE nombre_tabla (col1 text PRIMARY KEY NOT NULL); 
```
 
### FOREIGN KEY
Clave foránea, es una restricción que se puede agregar a la columna de una tabla para indicar que los valores de esa columna existen en otra tabla.
 
Restricción:
```
FOREIGN KEY (col_tabla) REFERENCES otra_tabla(col_de_otra_tabla)
```
  
 
**Agregar foreign key** : Para agregar la clave foránea a una tabla existente
 
```MySQL
ALTER TABLE nombre_tabla ADD COLUMN nombre_columna tipo_dato REFERENCES nombre_tabla_referencia(nombre_columna_referencia);
```
 
 
## JOIN

Esta cláusula sirve para unir tablas que tengan alguna relación en común. Es decir debe existir un punto de unión
 
  
```MySQL
SELECT * FROM name_table JOIN other_table ON col_table = col_other_table;
```
 
***Atributos con el mismo nombre*** : puede suceder que al querer unir dos tablas nos encontremos con el caso de que el nombre de sus columnas son iguales, es decir que en el punto de unión los nombres de estas columas son iguales. Para este caso ahremos lo siguiente:

```MySQL
/*Notar que agregamos un punto, ej usuarios.email = empleados.email*/
SELECT * FROM name_table JOIN other_table ON name_table.col = other_table.col;
```
.
.  
***Seleccionando ALGUNOS atributos*** : en ocasiones precisaremos solo de ciertos datos de una de las dos tablas, y para evitar confusiones con los atributos de las tablas podemos seleccionarlos de la sig. forma

```MySQL
SELECT tabla.*, otra_tabla.column FROM tabla JOIN otra_tabla ON tabla.column = otra_tabla.column;  
```
 

### Orden de las cláusulas 
| COMANDO | SE LEE COMO |
|---|---|
| SELECT | Selecciona estos esto |
| FROM | De esta tabla |
| JOIN | Unelos con esta tabla |
| WHERE | filtra los valores que cumple tal condición |
| GROUP BY | Agrupa los resultados por este criterio |
| HAVING | Filtra por estos criterios agrupados |
| ORDER BY | Ordena los resultados por este otro criterio |
| LIMIT | Limita los resultados a esta cantidad |


***Agrupar multiples columnas*** 

Supongamos que tenemos dos tablas: una tabla Clientes que almacena información sobre los clientes y otra tabla Pedidos que almacena información sobre los pedidos realizados por esos clientes. Queremos realizar una consulta que nos muestre la cantidad total de pedidos realizados por cada cliente. Para esto, ejecutaremos una consulta que utilice la cláusula GROUP BY para agrupar los pedidos por cliente y contaremos la cantidad total de pedidos para cada cliente.

```MySQL
SELECT c.Nombre AS NombreCliente, COUNT(p.PedidoID) AS TotalPedidos
FROM Clientes c
JOIN Pedidos p ON c.ClienteID = p.ClienteID
GROUP BY c.ClienteID;
```
 

### TIPOS DE JOIN
Existen varias formas de unir tablas. A continuación veremos algunas de ellas.

#### **INNER JOIN**
Este es un join normal, es decir

```
SELECT * FROM tabla JOIN otra_tabla ON tabla.col = otra_tabla.col;
```

es lo mismo que 

```
SELECT * FROM tabla JOIN otra_tabla ON tabla.col = otra_tabla.col;
```

En una operación de Inner Join se combinan los registros de ambas tablas siempre y cuando la clave en común esté en ambas tablas 
 
  
#### **LEFT JOIN**

En un LEFT JOIN, todas las filas de la tabla izquierda aparecerán en el resultado, en el caso de no existir coincidencia con la tabla derecha, los campos correspondientes a dicha tabla se llenarán con valores NULL.

```MySQL
SELECT * FROM tabla1 LEFT JOIN tabla2 ON tabla1.atributo = tabla2.atributo; 
```

#### **RIGHT JOIN**

Al igual que left join, rigth join cumple la misma funcón solo que ahora se centra en los datos de la tabla derecha.

```MySQL
SELECT * FROM tabla1 RIGHT JOIN tabla2 ON tabla1.atributo = tabla2.atributo; 
```






