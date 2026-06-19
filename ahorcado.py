"""
Juego del Ahorcado
Sigue el diagrama de flujo: Inicio -> elegir palabra -> pedir letra ->
verificar si esta en la palabra -> restar intento o revelar letra ->
verificar si gano o perdio -> Fin del juego.
"""

import random


def elegir_palabra():
    """Sistema elige una palabra de una lista y la devuelve en mayusculas."""
    palabras = ["PYTHON", "TECLADO", "PROGRAMA", "VARIABLE", "FUNCION"]
    return random.choice(palabras)


def mostrar_progreso(palabra, letras_adivinadas):
    """Muestra la palabra como guiones, revelando solo las letras correctas."""
    return " ".join(letra if letra in letras_adivinadas else "_" for letra in palabra)


def jugar():
    # Inicio
    palabra = elegir_palabra()
    letras_adivinadas = set()
    intentos = 5

    print("Bienvenido al juego del Ahorcado")
    print(mostrar_progreso(palabra, letras_adivinadas))

    # Bucle principal: se repite hasta que gane o pierda (lineas punteadas del diagrama)
    while True:
        # Usuario ingresa una letra
        letra = input("Ingresa una letra: ").upper()

        # Decision: La letra esta en la palabra?
        if letra in palabra:
            # Revelar letra correcta
            letras_adivinadas.add(letra)
            print(mostrar_progreso(palabra, letras_adivinadas))

            # Decision: Se completo la palabra?
            if set(palabra) == letras_adivinadas:
                print("Ganaste!")
                break  # Fin del juego
        else:
            # Restar un intento
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

            # Decision: Quedan intentos?
            if intentos <= 0:
                print(f"Perdiste! La palabra era: {palabra}")
                break  # Fin del juego

    print("Fin del juego")


if __name__ == "__main__":
    jugar()