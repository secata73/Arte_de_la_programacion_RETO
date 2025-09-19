"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from turtle import *
from random import randrange, choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Lista de colores permitidos (sin rojo)
colors = ["blue", "purple", "orange", "yellow", "pink"]

# Selección aleatoria de colores distintos
snake_color = choice(colors)
food_color = choice(colors)
while food_color == snake_color:
    food_color = choice(colors)


def change(x, y):
    "Cambia la dirección de la serpiente."
    aim.x = x
    aim.y = y


def inside(head):
    "Regresa True si la cabeza está dentro de los límites."
    return -200 < head.x < 190 and -200 < head.y < 190


def move_food():
    "Mueve la comida un paso al azar sin salirse de la ventana."
    step = choice([vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)])
    new_pos = food + step
    if inside(new_pos):
        food.move(step)


def move():
    "Mueve la serpiente un segmento hacia adelante."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # Rojo = Game Over
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Dibujar la serpiente
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Dibujar la comida
    square(food.x, food.y, 9, food_color)

    update()
    move_food()  # Movimiento aleatorio de la comida
    ontimer(move, 100)


# --- Configuración de la ventana ---
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
