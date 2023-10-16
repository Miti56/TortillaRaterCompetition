import random

def main():
    print("¡Bienvenido al Concurso de Calificación de Tortilla Española!")

    name = input("Primero, ¿cuál es tu nombre, futuro crítico de tortillas? ")
    print(f"¡Hola, {name}! Comencemos la aventura de degustación de tortillas.")

    # Obtener el número de jueces expertos y jueces adicionales
    num_jueces_expertos = int(input("¿Cuántos jueces expertos (imparciales) participarán? "))
    num_jueces_adicionales = int(input("¿Cuántos jueces adicionales (cocinaron) participarán? "))

    # Obtener el nombre de los jueces
    nombres_jueces_expertos = []
    for i in range(num_jueces_expertos):
        nombre_juez_experto = input(f"Nombre del juez experto {i + 1}: ")
        nombres_jueces_expertos.append(nombre_juez_experto)

    nombres_jueces_adicionales = []
    for i in range(num_jueces_adicionales):
        nombre_juez_adicional = input(f"Nombre del juez adicional {i + 1}: ")
        nombres_jueces_adicionales.append(nombre_juez_adicional)

    # Generar preguntas aleatorias para hacerlo más divertido
    preguntas = [
        "Describe la textura de la tortilla. ¿Es esponjosa como una nube o más densa que un muro de ladrillo?",
        "¿El aroma de la tortilla te transporta a una soleada playa española?",
        "Imagina que la tortilla es una obra de arte. ¿Cómo se ve? ¿Picasso o pintura con los dedos?",
        "¿El sabor es una fiesta en tu boca o más parecido a una siesta tranquila?",
        "¿Qué tan bien se mantiene unida la tortilla? ¿Es tan resistente como un torero o más frágil que un bailarín de flamenco?",
        "¿Los ingredientes armonizan como una apasionada actuación de flamenco o chocan como un toro en una tienda de porcelana?"
    ]

    puntuacion_total_expertos = 0
    puntuacion_total_adicionales = 0

    for pregunta in preguntas:
        print("\n" + pregunta)
        for nombre in nombres_jueces_expertos:
            puntuacion = obtener_puntuacion(nombre)
            puntuacion_total_expertos += puntuacion
        for nombre in nombres_jueces_adicionales:
            puntuacion = obtener_puntuacion(nombre)
            puntuacion_total_adicionales += puntuacion

    # Calcular la puntuación final considerando la ponderación de los jueces
    puntuacion_final = calcular_puntuacion_final(
        puntuacion_total_expertos, num_jueces_expertos,
        puntuacion_total_adicionales, num_jueces_adicionales)

    print("\nCalculando tu puntuación final...")
    print(f"¡{name}, tu Tortilla Española ha obtenido una puntuación de {puntuacion_final:.2f}/10!")

def obtener_puntuacion(nombre_juez):
    puntuacion = int(input(f"Calificación de {nombre_juez} del 1 al 10, siendo 1 terrible y 10 excelente: "))
    while puntuacion < 1 or puntuacion > 10:
        print("Por favor, ingresa una calificación válida entre 1 y 10.")
        puntuacion = int(input(f"Calificación de {nombre_juez} del 1 al 10, siendo 1 terrible y 10 excelente: "))
    return puntuacion

def calcular_puntuacion_final(puntuacion_total_expertos, num_jueces_expertos, puntuacion_total_adicionales, num_jueces_adicionales):
    peso_expertos = 2  # Peso de los jueces expertos (imparciales)
    peso_adicionales = 1  # Peso de los jueces adicionales (parciales)

    puntuacion_expertos = puntuacion_total_expertos / num_jueces_expertos
    puntuacion_adicionales = puntuacion_total_adicionales / num_jueces_adicionales

    puntuacion_final = (peso_expertos * puntuacion_expertos + peso_adicionales * puntuacion_adicionales) / (peso_expertos + peso_adicionales)
    return puntuacion_final

if __name__ == "__main__":
    main()
