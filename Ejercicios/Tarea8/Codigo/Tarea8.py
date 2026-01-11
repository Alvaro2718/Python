
# Ejercicio1
"""Dada una lista y un número, cree una función que devuelva dos parámetros: 
1. Si está dicho número en esa lista. En dicho caso Devolverá TRUE. En caso contrario, 
False. 
2. Si la longitud de la lista coincide con dicho número. En dicho caso devolverá TRUE. En 
caso contrario, False. """


def analizarLista(lista, numero):

    def exite(list, num): return num in list
    def misma_longitud(list, num): return len(list) == num
    return exite(lista, numero), misma_longitud(lista, numero)


# Ejemplo de uso
numeros = [10, 20, 30, 40, 50]
print(analizarLista(numeros, 30))  # Salida por consola: (True, False)
print(analizarLista(numeros, 5))    # Salida por consola: (False, True)

"""Explicación breve:

lambda l, n: n in l → devuelve True si el número está en la lista.

lambda l, n: len(l) == n → devuelve True si la longitud de la lista es igual al número.

La función devuelve ambos resultados como una tupla:
(existe_en_lista, longitud_igual)."""

# ------

# Ejercicio2
"""Dada una lista, cree dos funciones, una que devuelva el mayor número y otra que devuelva en 
menor número."""


def numeroMayor(lista):

    def mayor(list): return max(list)
    return mayor(lista)


def numeroMenor(lista):

    def menor(list): return min(list)
    return menor(lista)


# Ejemplo de uso
numeros = [15, 22, 8, 19, 31]
print("Mayor:", numeroMayor(numeros))  # Salida por consola: Mayor: 31
print("Menor:", numeroMenor(numeros))  # Salida por consola: Menor: 8


# ------

# Ejercicio3
"""Imprima el abecedario al revés. 
Puedes ayudarse de reversed."""


def abecesarioAlReves():

    def alReves(): return ''.join(reversed('abcdefghijklmnopqrstuvwxyz'))
    return alReves()


print(abecesarioAlReves())  # Salida por consola: zyxwvutsrqponmlkjihgfedcba'))
