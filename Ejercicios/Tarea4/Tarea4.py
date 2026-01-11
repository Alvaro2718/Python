
"""Tarea4"""


# Ejercicio 1
"""Encontrar la suma de todos los números impares entre 1 y 50
    Objetivo:Objetivo: Usar bucles y condicionales para filtrar y sumar valores"""


suma = 0  # Variable que vamos a usar ir acumulando los números impares
for num in range(1, 50):  # Números del 1 al 50

    if num % 2 != 0:
        suma += num

print("La suma de todos los números impares entre 1 y 50 es: ", suma)

# Ejercicio2
"""Encontrar la longitud de la palabra más larga en una lista
Objetivo: Enseñar la iteración sobre listas y el cálculo de la longitud de cadenas.
  """
palabras = ["Alvaro", "JuanFran", "Pedro", "Gilberto", "Alba"]


palabra_mas_larga = ""
longitud_maxima = 0


for palabra in palabras:
    if len(palabra) > longitud_maxima:
        longitud_maxima = len(palabra)
        palabra_mas_larga = palabra
print("La palabra más larga es", palabra_mas_larga,
      "con ", longitud_maxima, "caracteres.")


# Ejercicio3
"""Usar un bucle para imprimir la secuencia de Fibonacci hasta el décimo término
Objetivo:Practicar la iteración con bucles y la generación de secuencias"""


# El método Fibonacci es la suma de los dos número ateriores:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...


n = 10  # limites de números que vamos a mostrar
a = 0
b = 1


fibonacci = []


for _ in range(n):
    fibonacci.append(a)
    temporal = a
    a = b
    b = temporal + b


print("Los primeros 10 terminos de la secuencia de Fibonacci son: ")
print(fibonacci)


# Ejercicio4
""" Crear un diccionario para contar la cantidad de veces que aparece cada carácter en
una cada cadena
Objetivo: Enseñar el uso de diccionarios y la iteración sobre cadenas """


# creamos una variable que almacenará el texto introducido
texto = ("El primero que salga de la clase lo suspendo. ")


# Creamos un diccionario
conteo = {}


# Recorremos cada carácter en la cadena
for caracter in texto:
    if caracter in conteo:
        conteo[caracter] += 1  # Si ya existe, sumamos 1
    else:
        conteo[caracter] = 1  # Si no existe, lo inicializamos en 1

# Mostramos los resultados
print("\nFrecuencia de cada carácter: ")
for caracter, cantidad in conteo.items():
    print(f" {caracter} : {cantidad}")


# Ejercicio5
"""Crear un bucle anidado para imprimir una tabla de multiplicar para los números del
1 al 55
Objetivo: Enseñar el uso de bucles anidados y operaciones aritméticas básicas."""


for i in range(1, 56):  # números del 1 al 5
    print(f"\nTabla de multiplicar del  {i}:")
    for j in range(1, 11):  # multiplicadores del 1 al 10
        resultado = i * j
        print(f"{i} X {j} = {resultado}")

 # Ejercicio6
"""Escribir un programa que encuentre el segundo número más grande en una lista
Objetivo:Objetivo: Introducir la ordenación de listas y el uso de índices"""

# Lista de números
numeros = [10, 25, 4, 67, 89, 23, 45, 67, 89, 90, 12]

# Ordenaos la lista de menor a mayor
numeros.sort()

# El segundo número más grande estará en la penúltima posición
segundo_mas_grande = numeros[-2]

# Mostramos el segundo número más grande mas consola
print("\nEl segundo número más grande en la lista es:", segundo_mas_grande)
