
import turtle
import random

# Настройки окна
screen = turtle.Screen()
screen.bgcolor("midnight blue")

# Настройка черепахи
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Функция для рисования здания
def draw_building(x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Функция для рисования окна
def draw_window(x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(width)
        t.left(90)
    t.end_fill()

# Создаем здания
t.color("dark slate gray")
for i in range(-300, 301, 100):
    building_height = random.randint(100, 300)
    draw_building(i, -250, 80, building_height)

# Добавляем окна
t.color("yellow")
for i in range(-290, 301, 100):
    building_height = random.randint(100, 300)
    for j in range(-250 + 20, -250 + building_height, 40):
        if random.choice([True, False]):  # Случайно решаем, будет ли окно светиться
            draw_window(i + 10, j, 20, 20)

# Рисуем луну
t.penup()
t.goto(200, 200)
t.pendown()
t.color("light goldenrod")
t.begin_fill()
t.circle(30)
t.end_fill()

# Рисуем звезды
t.color("white")
for _ in range(20):
    x = random.randint(-300, 300)
    y = random.randint(0, 250)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(10)
        t.right(144)
    t.end_fill()

# Скрыть черепаху и оставить окно открытым
t.hideturtle()
turtle.done()
