# The script of the game goes in this file.

# CHARACTERS
# -----------------------------------------------------------------------------------------------------------------------

# OCs
define od = Character("OPSEC Demon", color="FF0000")                                # OPSEC Demon, rojo
define lpv = Character("La puta vieja", color="00FF00")                             # La puta vieja, verde

# Touhou
define c = Character("Cirno", color="FF69B4")                                       # Cirno, azul
define r = Character("Reimu Hakurei", color="FF0000")                               # Reimu, rojo
define p = Character("Patchouli Knowledge", color="9D00FF")                         # Patchouli, moraito

# GNU/Linux/Open Source
define e = Character("eMule", color="00FF00")                                       # eMule, verde
define t = Character("Tux", color="FFFF00")                                         # Tux, amarillo

# Otros
define mm = Character("Monero Mommy", color="FFA500")                               # Monero Mommy, naranja
define s = Character("Satanichia Kurumizawa McDowell", color="FF0000")              # Satania, rojo

# Subnormales
define ccb = Character("CyberCatBoy", color="FF00FF")                               # Germán, magenta
define rc = Character("Ron Cola", color="9D00FF")                                   # Carlos, moraito
define nc = Character("Nigeru-chan", color="804000")                                # Arturo, marrón
define jc = Character("Jean Charles", color="FF69B4")                               # Juan Carlos, rosita mariconcete

# -----------------------------------------------------------------------------------------------------------------------

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show Patchouli Knowledge happy

    # These display lines of dialogue.
    p "You've created a new Ren'Py game."
    p "Once you add a story, pictures, and music, you can release it to the world!"

    with fade

    "Es medianoche. Estás solo en una casa abandonada."

    gr "¿Qué ha sido ese ruido?"

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
    
    p "Sabía que vendrías..."

    "La puerta se cierra detrás de ti."

    "FINAL 1: La habitación secreta."
    return

label salida:

    p "No pienso averiguar qué hay ahí dentro."

    "Escapas de la casa antes del amanecer."

    "FINAL 2: La huida."
    return
