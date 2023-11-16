import json

# Cargar la base de datos de animales desde el archivo JSON
try:
    with open("animales.json", "r") as archivo_json:
        animales_json = json.load(archivo_json)
except FileNotFoundError:
    print("No se encontró el archivo 'animales.json'. Asegúrate de que exista y esté bien formateado.")
    exit()

# Función para adivinar el animal con el menor número de preguntas
def adivinar_animal():
    print("Piensa en un animal y responde con 'si' o 'no' a las siguientes preguntas:")

    animales_restantes = list(animales_json.keys())
    bits_restantes = set(range(1, 2049))

    while len(animales_restantes) > 1:
        pregunta_actual = None
        respuesta = None

        # Encontrar la pregunta más informativa
        for pregunta, bits in preguntas.items():
            animales_con_bits = [animal for animal in animales_restantes if animales_json[animal]["bits_posicion"] & bits != 0]
            animales_sin_bits = [animal for animal in animales_restantes if animales_json[animal]["bits_posicion"] & bits == 0]

            if len(animales_con_bits) > 0 and len(animales_sin_bits) > 0:
                información = abs(len(animales_con_bits) - len(animales_sin_bits))
                if pregunta_actual is None or información > mejor_información:
                    mejor_información = información
                    pregunta_actual = pregunta

        # Realizar la pregunta y actualizar la lista de animales restantes
        respuesta = input(f"{pregunta_actual} (si/no): ").lower()
        if respuesta == "si":
            animales_restantes = [animal for animal in animales_restantes if animales_json[animal]["bits_posicion"] & preguntas[pregunta_actual] != 0]
        else:
            animales_restantes = [animal for animal in animales_restantes if animales_json[animal]["bits_posicion"] & preguntas[pregunta_actual] == 0]

    # Mostrar el animal adivinado
    print(f"¡Tu animal es un {animales_restantes[0]}!")

# Preguntas y sus valores en bits
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

# Llamar a la función para adivinar el animal
adivinar_animal()