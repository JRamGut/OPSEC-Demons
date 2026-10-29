# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define od = Character("OPSEC Demon")
define gr = Character("Germán Ramos")
define rc = Character("Ron Cola")
define n  = Character("Nigeru-chan")
define e = Character("JZ")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show eileen happy

    # These display lines of dialogue.
    e "You've created a new Ren'Py game."
    e "Once you add a story, pictures, and music, you can release it to the world!"

    with fade

    "Es medianoche. Estás solo en una casa abandonada."

    p "¿Qué ha sido ese ruido?"

    menu:
        "Abrir la puerta":
            jump puerta

        "Salir de la casa":
            jump salida

    # This ends the game.
    return

label puerta:

    scene black
    with dissolve

    m "Sabía que vendrías..."

    "La puerta se cierra detrás de ti."

    "FINAL 1: La habitación secreta."
    return

label salida:

    p "No pienso averiguar qué hay ahí dentro."

    "Escapas de la casa antes del amanecer."

    "FINAL 2: La huida."
    return
