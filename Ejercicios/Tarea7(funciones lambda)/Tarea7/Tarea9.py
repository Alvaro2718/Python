
"""Ejercicio 1: 
Leer un archivo CSV 
Lee un archivo datos.csv con columnas nombre, edad y muestra cada fila en formato: 
Nombre: Juan, Edad: 25. """

import csv

with open("datos.csv", encoding="utf-8") as f:
    for nombre, edad in csv.reader(f):
        if nombre.lower() == "nombre":
            continue
        print(f"Nombre: {nombre}, Edad: {edad}")


#----------------

"""Ejercicio 2: 
Escribir datos en un CSV 
Crea un archivo productos.csv y escribe 3 filas con columnas: producto, precio."""

import csv

rows = [("producto","precio"),
        ("Laptop","1200"),
        ("Mouse","25"),
        ("Teclado","80")]

with open("productos.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

#----------------

"""Ejercicio 3: Leer un archivo JSON 
Crea un archivo config.json con datos como: 
JSON 
{"usuario": "admin", "activo": true, "roles": ["editor", "admin"]} 
Mostrar más líneas 
Lee el archivo y muestra el valor de usuario. 
"""

import json

with open("config.json", "w", encoding="utf-8") as f:
    json.dump({"usuario":"admin","activo":True,"roles":["editor","admin"]}, f)

with open("config.json", encoding="utf-8") as f:
    print(json.load(f)["usuario"])

 #----------------

"""Ejercicio 4: Guardar datos en JSON 
Convierte un diccionario de Python en JSON y guárdalo en salida.json. 
"""
import json

data = {"a": 1, "b": 2, "c": 3}

with open("salida.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

#----------------

""" Ejercicio 5: Listar archivos en un directorio 
Muestra todos los archivos .txt que hay en la carpeta actual."""

import os

for file in os.listdir():
    if file.endswith(".txt"):
        print(file)

#----------------

"""Ejercicio 6: Contar palabras en un archivo grande 
Lee un archivo libro.txt y cuenta cuántas veces aparece la palabra "Python". """

import re

with open("libro.txt", encoding="utf-8") as f:
    text = f.read()
print(len(re.findall(r"\bPython\b", text, re.IGNORECASE)))
#----------------

"""Ejercicio 7: Copiar un archivo binario 
Copia una imagen foto.jpg a copia_foto.jpg usando modo binario. """

with open("foto.jpg", "rb") as origen, open("copia_foto.jpg", "wb") as destino:
    destino.write(origen.read())

#----------------

"""Ejercicio 8: Comprimir archivos en ZIP 
Crea un archivo ZIP que contenga saludo.txt y lineas.txt. """

import zipfile

with zipfile.ZipFile("archivos.zip", "w") as zipf:
    zipf.write("saludo.txt")
    zipf.write("lineas.txt")
#----------------

"""Ejercicio 9: Leer un archivo línea por línea y crear otro filtrado 
Lee datos.txt y guarda en filtrado.txt solo las líneas que contengan la palabra "ERROR" """
with open("datos.txt", encoding="utf-8") as f, open("filtrado.txt", "w", encoding="utf-8") as out:
    for line in f:
        if "ERROR" in line:
            out.write(line)
#----------------

"""Ejercicio 10: Procesar un archivo grande sin cargarlo completo 
Lee grande.txt línea por línea y cuenta cuántas líneas tiene sin usar read() ni readlines() (usa 
iteración)."""

contador = 0
with open("grande.txt", encoding="utf-8") as f:
    for _ in f:
        contador += 1

print(f"Número de líneas: {contador}")
