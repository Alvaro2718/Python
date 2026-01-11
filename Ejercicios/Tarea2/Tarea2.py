
#Mi clase Bucles
class Bucles:

    
    def mostrar_menu(self):
        print("--- Menú de Bucles ---")
        print("1º Ejercicio 1: Recorrer lista con for")
        print("2º Ejercicio 2: Recorrer lista con while")
        print("3º Ejercicio 3: Recorrer cadena de texto")
        print("4º Ejercicio 4: Tablas de multiplicar (1 al 9)")
        print("5º Ejercicio 5: Mostrar árboles hasta 'nogal'")
        print("6º Ejercicio 6: Mostrar solo números impares")
        print("7º Salir")

    #Ejercicio 1
    def recorrer_lista_for(self):
        # Aquí tengo una lista de ejemplo
        lista = [1, 2, 3, 4, 5]
        # Uso un bucle for para recorrer cada elemento de la lista
        for elemento in lista:
            print(elemento)

    #Ejercicio 2
    def recorrer_lista_while(self):
        lista = [1, 2, 3, 4, 5]
        i = 0
        # Con while lo hago manual: mientras i sea menor que la longitud de la lista, sigo
        while i < len(lista):
            print(lista[i])
            i += 1  # voy sumando 1 al índice para no quedarme en un bucle infinito

    #Ejercicio 3
    def recorrer_cadena_for(self):
        texto = "Hola mundo"
        # Aquí recorro cada letra de la cadena como si fuera una lista de caracteres
        for caracter in texto:
            print(caracter)
    
    #Ejercicio 4
    def tablas_multiplicar(self):
        # Dos bucles anidados: uno para el número base y otro para multiplicar del 1 al 10
        for i in range(1, 10):
            for j in range(1, 10):
                print(f"{i} * {j} = {i * j}")
            print("---")  # separador para que no se vea todo pegado

    #Ejercicio 5
    def mostrar_arboles(self):
        arboles = ["manzano", "pino", "madroño", "eucalipto",
                   "nogal", "olivo", "almendro"]
        # Recorro la lista de árboles uno a uno
        for arbol in arboles:
            if arbol == "nogal":
                # Cuando llego a "nogal", corto el bucle con break
                print("He llegado al nogal, paro aquí.")
                break
            print(arbol)
    
    #Ejercicio 6
    def mostrar_impares(self):
        numeros = [4, 6, 7, 8, 23, 21, 999, 10, 13, 65, 72]
        # Recorro todos los números y saco solo los que no son pares
        for numero in numeros:
            if numero % 2 != 0:  # si el resto de dividir entre 2 no es 0 → es impar
                print(numero)


# Aquí empieza el método principal (El método main en java)
bucles = Bucles()

while True:
    bucles.mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        bucles.recorrer_lista_for()
    elif opcion == "2":
        bucles.recorrer_lista_while()
    elif opcion == "3":
        bucles.recorrer_cadena_for()
    elif opcion == "4":
        bucles.tablas_multiplicar()
    elif opcion == "5":
        bucles.mostrar_arboles()
    elif opcion == "6":
        bucles.mostrar_impares()
    elif opcion == "7":
        print("Saliendo del programa...Adios, Alvaro")
        break
    else:
        print("Opción no válida, prueba otra vez.")
