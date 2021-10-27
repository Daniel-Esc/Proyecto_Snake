# 26/10/2021
# 03:35 pm

# Juego Snake, simula una serpiente comiendo fruta, la cual aparece aleatoriamente en la pantalla
# La comida y la vibora pueden ser de 5 colores diferentes cada vez que incia el juego

# Modificado por:

# Gabriel Sebastián Garibay Dávila
# Daniel Evaristo Escalera Bonilla
# Francisco Cruz Vázquez
# Juan Carlos Martínez Zacarías
# Carmina López Palacios

from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
color = ['magenta', 'purple', 'darkblue', 'grey', 'orange']
color2 = ['yellow', 'skyblue', 'lightgreen', 'gold', 'pink']
colal = random.choice(color)
colal2 = random.choice(color2)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # Ahora la comida se actualiza independientemente de si es alcanzada
    # o no por la serpiente
    
    food.x = randrange(-19, 18) * 10  # Las coordenadas x, y, de la comida, adquieren
    food.y = randrange(-19, 18) * 10  # valores aleatorios menores a los límites de la ventana
    
    if head == food:
        print('Snake:', len(snake))
        
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colal)

    square(food.x, food.y, 9, colal2)
    update()
    ontimer(move, 100) # La actualización se realiza cada segundo (paso de 1 segundo)

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