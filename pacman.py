"""Pacman modificado para Actividad 3.

Cambios realizados (marcados en el código):
1) Cambio de tablero (tiles_alt) y switch USE_ALT_BOARD.
2) Cambio de número de fantasmas (GHOST_STARTS).
3) Cambio del inicio de Pacman (PACMAN_START).
4) Fantasmas más rápidos/lentos por constantes (GHOST_SPEED, TIMER_MS).
5) Fantasmas más listos (greedy con aleatoriedad).

Controles: Flechas ← → ↑ ↓
Requisitos: Python 3.x, turtle, freegames

Basado en el código de Grant Jenks (freegames).
"""

from random import choice, random
from turtle import *
from freegames import floor, vector

# =====================
# Configuración general
# =====================

# Modo dificultad (ajusta velocidad e intervalo de actualización)
HARD_MODE = True  # pon False para normal

GHOST_SPEED = 7 if HARD_MODE else 5   # paso de los fantasmas
TIMER_MS   = 80 if HARD_MODE else 100 # ms entre frames

# Cambia el número de fantasmas editando esta lista
GHOST_STARTS = [
    vector(-180, 160),
    vector(-180, -160),
    vector(100, 160),
    vector(100, -160),
    # Agrega/quita líneas para variar la cantidad
]

# Posición inicial de Pacman (debe caer en celda válida)
PACMAN_START = vector(-160, 160)  # cambiado respecto al original (-40, -80)

# Elegir tablero alternativo
USE_ALT_BOARD = True  # pon False para usar el tablero original

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = PACMAN_START.copy()
ghosts = [[pos.copy(), vector(GHOST_SPEED, 0)] for pos in GHOST_STARTS]

# =====================
# Tableros
# =====================
# fmt: off
tiles_original = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# Tablero alternativo (ejemplo: abre pasillos en la parte central y añade bloqueos laterales)
tiles_alt = tiles_original.copy()
# Modificaciones visibles: abrir un corredor vertical central y cerrar dos laterales
for r in range(4, 12):
    c = 10  # columna central
    tiles_alt[r*20 + c] = 1  # abre camino central

# cierra laterales superiores
tiles_alt[1*20 + 1] = 0
tiles_alt[1*20 + 2] = 0
tiles_alt[2*20 + 1] = 0

tiles = tiles_alt if USE_ALT_BOARD else tiles_original
# fmt: on

# =====================
# Utilidades
# =====================
def square(x, y):
    """Dibuja un cuadrado usando path en (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()
    for _ in range(4):
        path.forward(20)
        path.left(90)
    path.end_fill()


def offset(point):
    """Regresa el índice de tiles correspondiente a point."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """True si point cae en una celda libre (no pared) y está alineado a la grilla."""
    index = offset(point)
    if tiles[index] == 0:
        return False
    index = offset(point + 19)
    if tiles[index] == 0:
        return False
    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """Dibuja el mundo a partir de tiles."""
    bgcolor('black')
    path.color('blue')
    for index in range(len(tiles)):
        tile = tiles[index]
        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


def move():
    """Mueve a pacman y a los fantasmas."""
    writer.undo()
    writer.write(state['score'])

    clear()

    # mover pacman si la dirección es válida
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)
    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    # dibujar pacman
    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    # mover y dibujar fantasmas (IA más “lista”)
    for point, course in ghosts:
        # movimientos ortogonales posibles con la velocidad actual
        options = [
            vector(GHOST_SPEED, 0),
            vector(-GHOST_SPEED, 0),
            vector(0, GHOST_SPEED),
            vector(0, -GHOST_SPEED),
        ]
        valids = [v for v in options if valid(point + v)]

        choose_greedy = (len(valids) > 0) and (random() < 0.8)
        if choose_greedy:
            best = min(valids, key=lambda v: abs((point + v) - pacman))
            course.x, course.y = best.x, best.y
            point.move(best)
        else:
            pool = valids if valids else options
            plan = choice(pool)
            course.x, course.y = plan.x, plan.y
            if valid(point + plan):
                point.move(plan)

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    # condición de derrota
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, TIMER_MS)


def change(x, y):
    """Cambia la dirección de pacman si la celda siguiente es válida."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


# =====================
# Setup de Turtle
# =====================
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
