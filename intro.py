print("Hola Mundo")

# variables
nombre_curso = "Ultimate Python"
nombre1 = "Mundo"
print(nombre_curso, nombre1)
alumnos = 5000
punaje = 9.9
publicado = True 

#strings
nombreCurso = "Ultimate python"
descripcion = """ 
Ultimate python,
este curso contempla todos los detalles 
que necesitas aprender para encontrar
 trabajo como programador
"""

print(len(nombreCurso))
print(nombreCurso[0])
print(nombreCurso[0:8])

nombre = "Nicolas"
apellido = "Schurmann"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

numero = 2
#numero = numero + 2 
numero += 2
print("numero", numero) #esto me devuelve 4

#Calculadora

n1 = input("ingresa primer numero") #al ejecutar esto en la terminal me dira que le de un nro
n2 = input("ingresa primer numero")

# print(n1 + n2) esto no devuelve la suma de n1 y n2 sino su concatenacion

n1 = int(n1)
n2 = int(n2)
print(n1 + n2) #Ahora si

#otro ejemplo
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
