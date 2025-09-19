# Juego de memoria con mejoras
# Basado en Turtle Graphics y Freegames
# Documentado según estándar del Instituto

from random import shuffle
from turtle import *
from freegames import path

# Imagen central
car = path('car.gif')

# Sustituimos números por emojis para ayudar a la memoria
# Se repiten 2 veces para formar pares
emojis = ['🍎', '🍌', '🍒', '🍇', '🍉', '🍍', '🥑', '🥕',
          '🍓', '🍑', '🍋', '🍊', '🥭', '🥝', '🍈', '🌽',
          '🍆', '🥦', '🥔', '🥬', '🧄', '🧅', '🍄', '🌶',
          '🥜', '🌰', '🥐', '🥯', '🥨', '🍞', '🧀', '🥚']
tiles = emojis * 2  # Total 64 fichas

state = {'mark': None, 'taps': 0}  # Estado global
hide = [True] * 64  # Todas ocultas al inicio


def square(x, y):
    """Dibuja un cuadrado blanco con borde negro en (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierte coordenadas (x, y) en índice de tiles."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierte índice de tiles en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Actualiza estado con base en un clic del usuario."""
    spot = index(x, y)
    mark = state['mark']
    state['taps'] += 1  # Contador de taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Dibuja tablero, fichas y estado del juego."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Dibujar fichas ocultas
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    # Mostrar ficha seleccionada temporalmente
    mark = state['mark']
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 10)  # Centrado del texto
        color('black')
        write(tiles[mark], align="center", font=('Arial', 24, 'normal'))

    # Mostrar contador de taps
    up()
    goto(-190, 200)
    color('blue')
    write(f"Taps: {state['taps']}", font=('Arial', 16, 'normal'))

    # Detectar si el juego terminó
    if all(not h for h in hide):
        goto(0, -220)
        color('green')
        write("¡Felicidades! Has destapado todas las fichas 🎉", align="center", font=('Arial', 18, 'bold'))

    update()
    ontimer(draw, 100)


# Inicialización del juego
shuffle(tiles)
setup(420, 470, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

