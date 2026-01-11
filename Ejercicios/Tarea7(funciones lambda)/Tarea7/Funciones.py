

# Tarea de Funciones en Python


# 1- Dado un número, calcula su cuadrado.
def calcular_cuadrado(numero):

    def cuadrado(x):
        return x ** 2
    return cuadrado(numero)


print(calcular_cuadrado(5))  # Salida por consola: 25

# -----------

# 2- Dados dos números, encuentra el mayor.


def encontrarNumMayor(num1, num2):

    def mayor(x, y): return x if x > y else y
    return mayor(num1, num2)


print(encontrarNumMayor(10, 20))  # Salida por consola: 20

# -----------

# 3- Dado un número, comprueba si es impar.


def numImpar(numero):

    def impar(x): return x % 2 != 0
    return impar(numero)


print(numImpar(7))  # Salida por consola: True
print(numImpar(8))  # Salida por consola: False

# -----------

# 4- Dada una lista de números enteros positivos, filtra todos los números impares


def filtrarImpares(lista):

    impares = list(filter(lambda x: x % 2 != 0, lista))

    return impares


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtrarImpares(numeros))  # Salida por consola: [1, 3, 5, 7, 9]

# -----------

# 5- Ordena una lista de tuplas de 3 elementos utilizando su tercer elemento.


def ordenarPorTercerElemento(lista_tuplas):

    lista_ordenada = sorted(lista_tuplas, key=lambda x: x[2])
    return lista_ordenada


datos = [(1, 2, 9), (4, 5, 1), (7, 8, 5)]
print(ordenarPorTercerElemento(datos))
# Salida por consola: [(4, 5, 1), (7, 8, 5), (1, 2, 9)]

# -----------

# 6- Extrae el dominio de una dirección de correo electrónico. Por ejemplo, dado
# user@example.com, extrae example.com.


def extraerDominio(correo):

    def dominio(x): return x.split('@')[1]
    return dominio(correo)


print(extraerDominio("user@example.com"))  # Salida por consola: example.com

# -----------
""" EJERCICIOS AVANZADOS"""

"""1. Escriba un programa en Python que genere una función lambda que permita
#multiplicar dos números. """


def multiplicarNumeros(num1, num2):

    def multiplicar(x, y): return x * y
    return multiplicar(num1, num2)


print(multiplicarNumeros(4, 5))  # Salida por consola: 20

# -----------

"""2. Escriba una función de Python para dar la suma de los números de una lista."""


def sumarLista(numeros):

    def suma(lista): return sum(lista)
    return suma(numeros)


print(sumarLista([1, 2, 3, 4, 5]))  # Salida por consola: 15

# -----------
"""3. Dada una lista y un número, cree una función que devuelva dos parámetros:

• Si está dicho número en esa lista. En dicho caso Devolverá TRUE. En caso
contrario, False.
• Si la longitud de la lista coincide con dicho número. En dicho caso devolverá
TRUE. En caso contrario, False."""


def dividirListaPorNumero(lista, numero):

    def existe(list, num): return num in list
    def misma_longitud(list, num): return len(list) == num
    return existe(lista, numero), misma_longitud(lista, numero)


# Ejemplo de uso
numeros = [10, 20, 30, 40, 50]
print(dividirListaPorNumero(numeros, 30))  # Salida por consola: (True, False)
print(dividirListaPorNumero(numeros, 5))    # Salida por consola: (False, True)

# -----------
"""4. Dada una lista, cree dos funciones, una que devuelva el mayor número y otra
que devuelva en menor número."""


def mayor(lista):

    def mayor(lsit): return max(lsit)
    return mayor(lista), min(lista)


def menor(lista):
    def menor(list): return min(list)
    return menor(lista)


# Ejemplo de uso
numeros = [15, 22, 8, 19, 31]
print("Mayor:", mayor(numeros))  # Salida por consola: Mayor: 31
print("Menor:", menor(numeros))  # Salida por consola: Menor: 8

# -----------
"""5. Use la funcion sorted para ordenar una lista de números en orden ascendente y 
también descendente. """


def ordenarLista(lista):

    ascendente = sorted(lista)
    descendente = sorted(lista, reverse=True)
    return ascendente, descendente


# Ejemplo de uso
numeros = [42, 17, 8, 23, 56]
asc, desc = ordenarLista(numeros)
# Salida por consola: Ascendente: [8, 17, 23, 42, 56]
print("Ascendente:", asc)
# Salida por consola: Descendente: [56, 42, 23, 17, 8]
print("Descendente:", desc)

# -----------
"""6. Dada una lista de palabras que defina y una palabra introducida por el usuario, 
analice si dicha palabra está en la lista. """


def palabraEnLista(lista, palabra):

    def existe(list, pal): return pal in list
    return existe(lista, palabra)


# Ejemplo de uso
palabras = ["manzana", "banana", "cereza", "durazno"]
print(palabraEnLista(palabras, "banana"))  # Salida por consola: True
print(palabraEnLista(palabras, "uva"))     # Salida por consola: False

# -----------
"""7. Cree una función para contar la cantidad de números negativos de una lista. """


def contarNegativos(lista):

    def contar(list): return len([x for x in list if x < 0])
    return contar(lista)


# Ejemplo de uso
numeros = [10, -5, 3, -1, 0, -7, 8]
print(contarNegativos(numeros))  # Salida por consola: 3

# -----------
"""8. Cree una función para contar la cantidad de números impares de una lista."""


def contarImpares(lista):

    def contar(list): return len([x for x in list if x % 2 != 0])
    return contar(lista)


# Ejemplo de uso
numeros = [10, 15, 22, 33, 40, 51]
print(contarImpares(numeros))  # Salida por consola: 3

# -----------
"""9. Dada una palabra, cuente el número de vocales que tiene."""


def contarVocales(palabra):

    def contar(pal): return sum(1 for char in pal.lower() if char in 'aeiou')
    return contar(palabra)


# Ejemplo de uso
texto = "Educación"
print(contarVocales(texto))  # Salida por consola: 5

# -----------
"""10. Imprima el abecedario al revés."""


def abecedarioAlReves():

    def al_reves(): return ''.join(reversed('abcdefghijklmnopqrstuvwxyz'))
    return al_reves()


# Ejemplo de uso
print(abecedarioAlReves())  # Salida por consola: zyxwvutsrqponmlkjihgfedcba

# -----------

""" 11. Dado este diccionario concatenado 
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]} 
obtenga el string 'hello"""


def obtenerHello(diccionario):

    def buscar(d): return d['k1'][3]['tricky'][3]['target'][3]
    return buscar(diccionario)


# Ejemplo de uso
d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man',
                                 'inception', {'target': [1, 2, 3, 'hello']}]}]}
print(obtenerHello(d))  # Salida por consola: hello
