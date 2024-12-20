import turtle


t1 = turtle.Turtle()

for i in range(4):
    t1.forward(100)
    t1.left(90)

turtle.penup()
turtle.forward(300)
turtle.pendown()

for i in range(3):
    t1.forward(100)
    t1.left(120)

turtle.penup()
turtle.forward(300)
turtle.pendown()

for i in range(5):
    t1.forward(150)
    t1.right(144)

turtle.penup()
turtle.forward(300)
turtle.pendown() 

for i in range(100):
    t1.forward(i)
    t1.right(20)

t1.color("blue")
t1.begin_fill()
t1.circle(50)
t1.end_fill()

turtle.exitonclick()