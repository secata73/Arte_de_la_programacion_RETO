"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle with center at start and radius up to end."""
    # Calcula radio como distancia entre start y end
    r = ((end.x - start.x)**2 + (end.y - start.y)**2) ** 0.5
    if r <= 0:
        return

    # Posiciónate en el borde derecho del círculo
    up()
    goto(start.x, start.y)
    setheading(0)
    forward(r)
    left(90)

    # Traza un círculo aproximado con segmentos
    down()
    begin_fill()
    steps = 60
    circumference = 2 * 3.141592653589793 * r
    step_length = circumference / steps
    turn = 360 / steps
    for _ in range(steps):
        forward(step_length)
        left(turn)
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start (one corner) to end (opposite corner)."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    width = end.x - start.x
    height = end.y - start.y

    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()


def triangle(start, end):
    """Draw equilateral triangle using horizontal side from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    side = end.x - start.x  # longitud de la base
    for _ in range(3):
        forward(side)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
