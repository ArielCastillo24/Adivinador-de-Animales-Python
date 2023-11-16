import json

# Definir las preguntas y sus valores en bits
preguntas = {
    "es cuadrupedo": 1,
    "vive en el agua": 2,
    "tiene alas": 4,
    "está en peligro de extincion": 8,
    "tiene plumas": 16,
    "puede hablar": 32,
    "no tiene cola": 64,
    "puede salir del agua": 128,
    "tiene el cuello largo": 256,
    "puede ladrar": 512,
    "tiene escamas": 1024
}

# Función para hacer preguntas y calcular la cantidad de bits
def calcular_bits():
    animal = input("Ingrese el nombre del animal: ").lower()
    bits_totales = 0
    bits_posicion = 0

    # Hacer las 10 preguntas y calcular los bits totales y la posición
    for pregunta, bits in preguntas.items():
        respuesta = input(f"{pregunta} (si/no): ").lower()
        if respuesta == "si":
            bits_totales += bits
            bits_posicion |= bits  # Usar operador OR para establecer el bit en 1

    return animal, bits_totales, bits_posicion

# Verificar si el animal ya existe en el archivo JSON
def animal_existe(animal, json_data):
    return animal in json_data

# Verificar si los bits totales y de posición ya están asignados por otro animal
def bits_iguales(animal, bits_totales, bits_posicion, json_data):
    for existente in json_data.values():
        if bits_totales == existente["bits_totales"]:
            if bits_posicion == existente["bits_posicion"]:
                return True
    return False

# Leer el archivo JSON de animales
try:
    with open("animales.json", "r") as archivo_json:
        animales_json = json.load(archivo_json)
except FileNotFoundError:
    animales_json = {}

while True:
    animal, bits_totales, bits_posicion = calcular_bits()

    if animal_existe(animal, animales_json):
        print("Este animal ya existe en la base de datos. Intente con otro.")
    elif bits_iguales(animal, bits_totales, bits_posicion, animales_json):
        print("Los bits asignados ya están en uso por otro animal. Intente con otra combinación de respuestas.")
    else:
        animales_json[animal] = {"bits_totales": bits_totales, "bits_posicion": bits_posicion}
        with open("animales.json", "w") as archivo_json:
            json.dump(animales_json, archivo_json, indent=4)
        print(f"El animal {animal} ha sido agregado con {bits_totales} bits y la posición de bits: {bits_posicion:011b}.")

    otra_vez = input("¿Desea ingresar otro animal? (si/no): ").lower()
    if otra_vez != "si":
        break