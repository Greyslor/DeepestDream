# Declara el personaje base
define psico = Character("Lucy", color="#FF8000")
define Prota = Character("Me", color="#a349a4")
define friend = Character("Milly", color="#ffc0cb")

# Declara una variante del personaje base con una imagen diferente
define psicoSmile = psico.copy()
image psicoSmile = "images/psicoSmile.png"
define psicoNormal = psico.copy()
image psicoNormal = "images/psicoNormal.png"  # Modifica la ruta según la ubicación real
image Restaurant_B ="images/Restaurant_B.png"
define MillySmile = friend.copy()
image MillySmile = "images/MillySmile.png"
define MillyLaugh = friend.copy()
image MillyLaugh= "images/MillyLaugh.png"
define MillySad = friend.copy()
image MillySad= "images/MillySad.png"

image School_Hallway_Day ="images/School_Hallway_Day.png"
image Bedroom_Night_Dark ="images/Bedroom_Night_Dark.png"


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo
    scene School_Hallway_Day

    # Muestra la imagen del personaje psicoSmile en el personaje psico
    show psicoSmile

    # Presenta las líneas del diálogo.
    psico "Hola! Hace un agradable día..."
    psico "Ya has estado aquí durante algunos meses, dime, ¿Cómo te sientes el día de hoy?"

    hide psicoSmile

    menu:
        "Bien, supongo":
                        call respuesta1
        "No tan bien":
                        call respuesta1

    show psicoNormal
    psico "Cuéntame más... Estoy aquí para escucharte."

    hide psicoNormal

    "Después de una charla algo larga, la terapeuta dijo que es bueno que vaya a comer"
    "Como sea, ya es un gran avance que pueda ir  por mí mismo a la cafetería del lugar"

    scene Restaurant_B 
    "Siempre es cálido aquí..."
    
    show MillySmile

    friend "Me alegra mucho verte de nuevo!"
    show MillyLaugh
    friend "Mi doctora dijo que proximamente podré regresar a casa, la verdad que ahora estoy emocionada"
    show MillySmile
    friend "¿Qué te ha dicho Lucy?"

    "No mucho..."

    show MillySad
    friend "Ya veo..."
    friend "Bueno, está bien, iré a mi dormitorio, espero verte luego"

    hide MillySmile
    hide MillyLaugh
    hide MillySad

    "Espero no haberle causado problemas, sólo necesito un tiempo para socializar de nuevo, o eso creo..."
    "Debería comer, es lo que dicen todos"

    scene School_Hallway_Day
    "Ya es algo tarde, debería regresar a mi dormitorio"
    "Aunque no sé si debería continuar de ésta manera... Lucy ha dicho que ve mejoras en mí, pero me siento peor"
    "Tal vez debería dejar de mentir y fingir, pero por una parte no quiero estar controlado todo el tiempo para hacer cualquier actividad"

    scene Bedroom_Night_Dark
    "Los días me pasan bastante rápido, siento que no tengo ni siquiera oportunidad de cambiar algo"
    "Será mejor que vaya a dormir, al menos dentro de mis sueños, puedo hacer lo que sea y no cansarme"






    return

label respuesta1:
    psico "Oh vaya..."
    return

    # Finaliza el juego:
    return
