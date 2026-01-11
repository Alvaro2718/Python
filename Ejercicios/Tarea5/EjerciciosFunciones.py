"""Autor : Alvaro Lozano"""

# Ejercicio1
"""Escribir una función que muesre por pantalla el saludo 
¡Hola amiga! cada vez que se la incoque."""


import math
def saludar():
    print("¡Hola amiga!")  # Muestra por pantalla el Hola amiga


saludar()  # Ejemplo de uso

# ------
# Ejercicio 2
"""Escribir una función que se le pase una cadena <nombre> y muesre por pantalla
el saludo ¡hola <nombre>!."""


def saluda_nombre(nombre):
    # Muestra por pantalla el saludo con el nombre
    print("¡Hola " + nombre + "!")


saluda_nombre("Alvaro")  # Ejemplo de uso


# ------

# Ejercicio 3
"""Escribir una función que reciba un número entero positivo y devulva su factorial."""


def factorial(n):

    # Manejamos casos especiales, el caso del 0 y el 1
    if n <= 0 or n == 1:
        return 1

    else:
        # Inicializa el resultado
        fact = 1

        # Calcula el factorial
        for i in range(1, n + 1):
            fact *= i
            return fact
    # Ejemplo de uso
    print(f"El factorial de 5 es {factorial(5)}")


# Ejercicio 5
"""Escribir una función que calcule el área de un círculo
y otra que calcule el volumen de un cilindro usando la primera función."""


def area_circulo(radio):
    # Calcula el área del círculo
    return math.pi * radio ** 2


def volumen_cilindro(radio, altura):
    # Calcula el volumen del cilindro usando el área del círculo
    area = area_circulo(radio)
    return area * altura


print(f"El área de un círculo de radio 5 es {area_circulo(5)}")
print(
    f"El volumen de un cilindro de radio 5 y altura 10 es {volumen_cilindro(5, 10)}")

# Ejercico 9
"""Escribir una función que calcule el máximo común divisor de 2 números
  y otra que calcule el mínimo común múltiplo."""


def mcd(a, b):
    """Calcula el Máximo Común Divisor (MCD) de dos números."""
    return math.gcd(a, b)


def mcm(a, b):
    """Calcula el Mínimo Común Múltiplo (MCM) de dos números."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mcd(a, b)


# Ejemplo de uso:
print(f"MCD de 12 y 18: {mcd(12, 18)}")
print(f"MCM de 12 y 18: {mcm(12, 18)}")


# Ejercicio 10
"""Escribir una función que convierta un número decimal binario y
otra que convierta un número binario en decimal."""


def decimal_a_binario(n):
    """Convierte un número decimal a binario."""
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        # str= función en python que convierte valores de otros tipos de datos a una cadena de caracteres(String)
        binario = str(n % 2) + binario
        n //= 2
    return binario


# -----
# Ejercicio 8
"""Escribir una función que cuente los caracteres de una cadena."""


def contar_caracteres(cadena):

    # Contar y devolver el número de caracteres de una cadena.
    # utilizamos len, que devuelve el número de caracteres de una cadena.
    return len(cadena)


# Ejemplo
print(
    f"Número de caracteres en 'Hola Alvaro': {contar_caracteres('Hola Alvaro')}")


# ------
# Ejercicio 10
"""Función de suma recursiva"""


def suma_recursiva(n):

    # Calcula la suma de los primeros n números enteros positivos de forma de forma recursiva.

    if n == 1:
        return 1
    elif n <= 0:
        return 0
    else:
        # Llamada recursiva: n + suma_recursiva(n-1)
        return n + suma_recursiva(n - 1)  # La función se llama a sí misma
    # Ejemplo
    print(f"Suma recursiva hasta el 5: {suma_recursiva(5)}")
