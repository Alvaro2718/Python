# Simulador de una tienda en linea
# La tienda va a vender libros

# Diccionario con los productos disponibles
# Cada producto tiene su precio y el stock
productos = {
    "Aprende Python": {"precio": 15.0, "stock": 5},
    "La Biblia": {"precio": 18.0, "stock": 3},
    "El Quijote": {"precio": 20.0, "stock": 4}
}

# Lista que va a funcionar como el carrito de la compra
carrito = []

# Variable para controlar la opcion del menu
opcion = 0

# El programa se repite hasta que el usuario elija salir
while opcion != 4:
    print("\n--- TIENDA EN LÍNEA ---")
    print("1. Ver catálogo")
    print("2. Agregar producto al carrito")
    print("3. Ver carrito y total a pagar")
    print("4. Finalizar compra y salir")

    # Pedimos la opcion al usuario
    opcion_texto = input("Elige una opción: ")

    # Comprobamos que lo que escribe sea un numero
    if opcion_texto.isdigit():
        opcion = int(opcion_texto)
    else:
        # Si no es un numero, no dejamos que el programa se rompa
        print("Tienes que escribir un número del menú")
        opcion = 0

    # Opcion 1: mostramos todos los productos
    if opcion == 1:
        print("\nCatálogo de productos:")
        for nombre, info in productos.items():
            print(
                f"{nombre} - Precio: €{info['precio']} - Stock: {info['stock']}")

    # Opcion 2: añadir un producto al carrito
    elif opcion == 2:
        # Pedimos el nombre del producto
        # strip() sirve para quitar los espacios de más al principio o al final del texto
        nombre_producto = input("Escribe el nombre del producto: ").strip()

        # Comprobamos que el producto exista
        if nombre_producto in productos:
            # Miramos si queda stock
            if productos[nombre_producto]["stock"] > 0:
                carrito.append(nombre_producto)
                productos[nombre_producto]["stock"] -= 1
                print("Producto agregado al carrito")
            else:
                print("No hay stock disponible de este producto")
        else:
            print("Ese producto no existe")

    # Opcion 3: ver el carrito y calcular el total
    elif opcion == 3:
        if len(carrito) == 0:
            print("El carrito está vacío")
        else:
            total = 0
            print("\nProductos en el carrito:")
            for producto in carrito:
                print(f"- {producto}")
                total += productos[producto]["precio"]

            print(f"Total a pagar: €{total}")

    # Opcion 4: salir del programa
    elif opcion == 4:
        print("Gracias por tu compra. ¡Hasta luego!")

    # Por si el usuario pone una opcion que no existe
    else:
        print("Opción no válida, intenta de nuevo")
