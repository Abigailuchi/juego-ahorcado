"""
Juego del Ahorcado - 

Este programa lleva a codigo real el algoritmo que fue diseniado
previamente en el diagrama de flujo (Autonomo 1).

Flujo del programa (igual al diagrama):
Inicio -> el sistema elige una palabra -> se muestra oculta con guiones ->
el usuario ingresa una letra -> se decide si la letra esta en la palabra ->
si esta: se revela la letra y se revisa si la palabra quedo completa (Ganaste) ->
si no esta: se resta un intento y se revisa si quedan intentos (Perdiste) ->
Fin del juego.
"""

import random


def elegir_palabra():
    """
    Sistema elige una palabra.

    No recibe ningun parametro.
    Devuelve (return) un texto (str) en mayusculas, elegido al azar
    de una lista fija de palabras relacionadas con programacion.
    """
    palabras = ["PYTHON", "TECLADO", "PROGRAMA", "VARIABLE", "FUNCION"]
    return random.choice(palabras)


def mostrar_progreso(palabra, letras_adivinadas):
    """
    Construye el texto que el jugador ve en pantalla.

    Parametros:
        palabra (str): la palabra secreta que el sistema eligio.
        letras_adivinadas (set): conjunto con las letras que el jugador
            ya adivino correctamente hasta el momento.

    Devuelve (return) un texto (str) donde cada letra adivinada se
    muestra normal, y cada letra que falta se muestra como un guion bajo.
    Por ejemplo, si la palabra es "PYTHON" y solo se adivino la "P",
    esta funcion devuelve: "P _ _ _ _ _"
    """
    return " ".join(letra if letra in letras_adivinadas else "_" for letra in palabra)


def jugar():
    """
    Funcion principal que controla todo el juego del Ahorcado.
    No recibe parametros ni devuelve ningun valor, solo imprime
    mensajes en pantalla y pide datos al usuario.
    """

    # --- Inicio del juego ---
    palabra = elegir_palabra()          # El sistema elige la palabra secreta
    letras_adivinadas = set()           # Aqui se guardan las letras correctas
    intentos = 5                        # El jugador empieza con 5 intentos

    print("Bienvenido al juego del Ahorcado")
    print(mostrar_progreso(palabra, letras_adivinadas))

    # --- Bucle principal del juego ---
    # Se repite una y otra vez (estructura repetitiva) hasta que el
    # jugador gane o pierda. Esto corresponde a las flechas punteadas
    # del diagrama de flujo que regresan a "Usuario ingresa una letra".
    while True:

        # El usuario ingresa una letra
        letra = input("Ingresa una letra: ").upper()

        # Decision (estructura condicional): la letra esta en la palabra?
        if letra in palabra:
            # Caso "Si" del diagrama: Revelar la letra correcta
            letras_adivinadas.add(letra)
            print(mostrar_progreso(palabra, letras_adivinadas))

            # Nueva decision: se completo la palabra?
            if set(palabra) == letras_adivinadas:
                print("Ganaste!")
                break  # Termina el bucle: Fin del juego

        else:
            # Caso "No" del diagrama: Restar un intento
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

            # Nueva decision: quedan intentos?
            if intentos <= 0:
                print(f"Perdiste! La palabra era: {palabra}")
                break  # Termina el bucle: Fin del juego

    # --- Fin del juego ---
    print("Fin del juego")


# Este bloque hace que el programa solo se ejecute si abrimos
# directamente este archivo (y no si lo importamos desde otro archivo).
if __name__ == "__main__":
    jugar()