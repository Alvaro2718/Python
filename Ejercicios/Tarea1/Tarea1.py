
#Esta es mi clase Ejercicios
class Ejercicios:

   
    #Lo que voy hacer es hacer un menú con todos los ejercicios de esta Tarea
    #donde dependiendo de la opción que elijas accederas a ejecutar ese ejercicio 
    # o saldras del programa

     #Este es mi métod mostrar menú
    def mostrar_menu(self):
        print("--- Menú ---")
        print("1º Ejercicio 1: Mayor de edad")
        print("2º Ejercicio 2: Comprobar contraseña")
        print("3º Ejercicio 3: División de dos números")
        print("4º Ejercicio 4: Número par o impar")
        print("5º Ejercicio 5: Evaluación de empleados")
        print("6º Salir del programa")

    
    # Ejercicio 1:Este es mi método para comprobar si ere mayor de edad
    def mayor_edad(self, edad):
        if edad >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")

    #Ejercicio 2
    def comprobar_contraseña(self):
        contraseña_guardada = "contraseña"
        entrada = input("Introduce la contraseña: ")
        if entrada.lower() == contraseña_guardada.lower():
            print("La contraseña es correcta")
        else:
            print("La contraseña es incorrecta")

    #Ejercicio 3
    def division(self, num1, num2):
        if num2 == 0:
            print("Error: No se puede dividir entre cero")
        else:
            print(f"La división de {num1} entre {num2} es: {num1 / num2}")
    
    #Ejercicio 4
    def par_o_impar(self, numero):
        if numero % 2 == 0:
            print(f"El número {numero} es par")
        else:
            print(f"El número {numero} es impar")


    #Ejercicio 5
    def evaluacion_empleado(self, puntos):
        if puntos == 0.0:
            nivel = "Inaceptable"
        elif puntos == 0.4:
            nivel = "Aceptable"
        elif puntos == 0.6:
            nivel = "Meritorio"
        else:
            print("Puntuación no válida")
            return

        dinero = 2400 * puntos
        print(f"Nivel: {nivel}")
        print(f"Dinero recibido: {dinero:.2f} €")


#Aquí empieza el método principal (el método main en java)
ejercicios = Ejercicios()


#Aquí trabajamos llamando a los métodos dependiendo de la opción 
#que el usuario elija.
#Lo hacemos con if else anidados(en java lo haría con un switch case)
while True:
    ejercicios.mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        edad = int(input("Introduce tu edad: "))
        ejercicios.mayor_edad(edad)

    elif opcion == "2":
        ejercicios.comprobar_contraseña()

    elif opcion == "3":
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        ejercicios.division(num1, num2)

    elif opcion == "4":
        numero = int(input("Introduce un número entero: "))
        ejercicios.par_o_impar(numero)

    elif opcion == "5":
        puntos = float(input("Introduce la puntuación (0.0, 0.4, 0.6): "))
        ejercicios.evaluacion_empleado(puntos)

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, prueba otra vez.")
