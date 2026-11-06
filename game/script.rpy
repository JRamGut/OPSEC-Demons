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
define e = Character("Eirin Yagokoro", color="E6E6FA")                              # Eirin, lila

# GNU/Linux/Open Source
define e = Character("eMule", color="00FF00")                                       # eMule, verde
define t = Character("Tux", color="FFFF00")                                         # Tux, amarillo
define c = Character("Clippy", color="9B9B9B")                                      # Clippy, gris
define bb = Character("Bonzi Buddy", color="9D00FF")                                # Bonzi Buddy, moraito

# Otros
define m = Character("Monero", color="FFA500")                                      # Monero
define mm = Character("Monero Mommy", color="FFA500")                               # Monero Mommy, naranja
define s = Character("Satanichia Kurumizawa McDowell", color="FF0000")              # Satania, rojo

# Subnormales
define ccb = Character("CyberCatBoy", color="FF00FF")                               # Germán, magenta
define rc = Character("Ron Cola", color="9D00FF")                                   # Carlos, moraito
define nc = Character("Nigeru-chan", color="804000")                                # Arturo, marrón
define jc = Character("Jean Charles", color="FF69B4")                               # Juan Carlos, rosita mariconcete

define ab = Character("Angry Bird", color="FF0000")                                 # Angry Bird, rojo

# -----------------------------------------------------------------------------------------------------------------------

# IMAGES
# -----------------------------------------------------------------------------------------------------------------------

image tux = "images/tux.png"
image tux drinking = "images/tux_drinking.gif"

# -----------------------------------------------------------------------------------------------------------------------

# POSITIONS
# -----------------------------------------------------------------------------------------------------------------------

transform center_left:
    xalign 0.2
    yalign 0.5

transform center:
    xalign 0.5
    yalign 0.5

transform center_right:
    xalign 0.8
    yalign 0.5

transform lower_left:
    xalign 0.2
    yalign 1.0

transform lower_center:
    xalign 0.5
    yalign 1.0

transform lower_right:
    xalign 0.8
    yalign 1.0

# -----------------------------------------------------------------------------------------------------------------------

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black

    with fade

    "You hear a noise coming from the basement."

    show tux drinking at center

    t "¿What was that?"

    show tux at center

    menu:
        "Open the door":
            jump puerta

        "Leave the house":
            jump salida

    # This ends the game.
    return

label puerta:

    scene black
    with dissolve
    
    t "I knew you would come..."

    "The door closes behind you."

    "FINAL 1: The secret room."
    return

label salida:

    t "I don't plan to find out what's in there."

    "You escape the house before dawn."

    "FINAL 2: The escape."
    return
