import random

# Palabras fijas para cada nivel
palabras_fijas = [
    "a",         # Nivel 1: una letra
    "no",        # Nivel 2: dos letras
    "sol",       # Nivel 3: tres letras
    "casa",      # Nivel 4: cuatro letras
    "perro",     # Nivel 5: cinco letras
]

def juego():
    print("¡Bienvenido al juego de adivinanza de letras y palabras!")
    nivel = 1

    while nivel <= 5:
        palabra = palabras_fijas[nivel - 1]
        
        print(f"\nNivel {nivel}: Adivina la palabra de {len(palabra)} letra(s)")
        print(f"Letras posibles: {', '.join(sorted(set(palabra)))}")

        intentos = 0
        while True:
            intento = input("Introduce tu adivinanza: ").lower()
            intentos += 1

            if intento == palabra:
                print(f"¡Correcto! Has adivinado la palabra '{palabra}' en {intentos} intentos.")
                break
            else:
                print("Incorrecto, intenta de nuevo.")

        nivel += 1

    print("\n¡Felicidades! Has completado todos los niveles.")

# Ejecutar el juego
juego()
