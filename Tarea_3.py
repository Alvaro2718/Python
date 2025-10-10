TAREA 3


    print("--- Menú de Ejercicios")
    print("1º Ejercicio 1: Preguntar al usuario Nº ganadores de la lotería.")
    print("2º Ejercicio 2: Mostrar por pantalla números del 1 al 10 separados por comas.")
    print("3º Ejercicio 3: Contar vocales")
    pritn("4º Ejercicio 4: Mostrar Precios")
    pritn("5º Ejercicio 5:")


#Ejercicio 1
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los
#almacene en una lista y los muestre por pantalla ordenados de menor a mayor
def ejercicio1 (self):
    numeros = [] #Creamos una lista vacía
    cantidad = int(input("Dime los números ganadores de la Primitiva: "))
    
    for i in range(cantidad):
        num = int(input(f"Introduce el número {i+1}: "))
        numeros.append(num) #Añadimos el número a la lista

    numeros.sort()

    print("\nLos númros ganadores dela Primitiva ordenados de menor a mayor son: ")
    print(numeros)

#Ejercicio 2
#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas
def ejercicio2 (self):
    numeros = list(range(1,11))#Creamos una lista con los números del 1 al 10
    print(", ".join(map(str, numeros[::-1])))#Mostramos en orden inverso, separados por comas

#Ejercicio 3
#Escribir un programa que pida al usuario un palabra y muestre por pantalla el número de veces que contiene cada vocal
def ejercicio3 (self):
    #Pedimos al usuario que introduzca una palabra
    palabra = input("Introduce una plabra: ").lover()#Con .lover lo transformamos todo a minusculas

    #Inicializamos un diccionario para contar las vocales
    vocales = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}

    #Contar las vocales
    for letra in palabra:
        if letra in vocales:
            vocales[letra] += 1

    #Mostramos resultados
    print("\nNúmero de veces que aparece cada vocal:")
    for vocal, cantidad in vocales.items():
        print(f"{vocal}: {cantidad}")


#Ejercicio 4
#Escribir un programa que almacene en una lista los siguientes precios 
#50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios
def ejercicio4(self):
    precios = [50, 75, 46, 22, 80, 65, 8]#Lista de precios

    #Calcular el menor y el mayor precio
    menor = min(precios)
    mayor = max(precios)

    #Mostrar por pantalla los resultados
    pritn(f"El precio más bajo es: {menor}")
    pritn(f"El precio más alto es: {mayor}")


#Ejercicio 5
#Escribir un programa que guarde en una variable el diccionario:
#'Euro':'€', 'Dollar':'$', Yen : '¥'
#pregunte al usuario por una divisa y muestre su simbolo o un mensaje de aviso si la divisa no está en el diccionario
def ejercicio5(self):
    #Creamos el diccionario
    divisa = {'Euro':'€', 'Dollar':'$', 'Yen ': '¥'}

    #Pedimos al usuario que introduzca la divisa
    nombre = input("Introduce la divisa (Euro, Dolar, Yen): ")

    #Comprobamos si está en el diccionario
    if nombre in divisa:
        print(f"El símbolo de {nombre} es: {divisa[nombre]}")



#Ejercicio 6
#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
#pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese
#número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
#informando de ello.
#Fruta Precio
#Plátano 1.35
#Manzana 0.80
#Pera 0.85
#Naranja 0.70
def ejercicio6(self):
    #Hacemos nuestro diccionario
    precios ={
        'Plátano' : 1.35,
        'Manzana' : 0.80,
        'Pera' : 0.85,
        'Naranja' : 0.70
    }

    # Pedir al usuario una fruta y la cantidad de kilos
    fruta = input("Introduce una fruta (Plátano, Manzana, Pera, Naranja): ")
    kilos = float(input("Introduce la cantidad de kilos: "))


    # Calcular al usuario una fruta y la cantidad de kilos
    if fruta in precios:
        total = precios[fruta] * kilos
        print(f"El precio de {kilos} kilos de {fruta} es : {total:.2f}€")
    else:
        print("Lo siento, la fruta no está en el diccionnario.")


#Ejercicio 7
#Un programa que cree un diccionario simulando una cesta de la compra.
#El programa debe preguntar el articulo y su precio y añadir el par al diccionario, hasta que el usuario
#decida terminar.
#Despues se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato:
#Lista de la Compra:
#Arcitulo 1    Precio
#Arcitulo 2    Precio
#Arcitulo 3    Precio
#Total         Coste

def ejercicio7(self):
    #Creamos nuestro diccionario
    cesta = {}

    #Pedir artículos y precios al usuario
    while True:
        articulo = input("Introduce el nombre del artículo (o 'fin' para terminar): ")
        if articulo.lower() =='fin':
            break
        try:
            precio = float(input(f"Introduce el precio de {articulo}: "))
            cesta[articulo] = precio
        except ValueError:
            print("Por favor, introduce un precio válido.")

    print("\nLista de la compra:")
    for articulo, precio in cesta.items():
        print(f"{articulo:<15} {precio:>6.2f}€")


