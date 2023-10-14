"""Turtle Tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
i: int = 0

leo.pencolor(252,240,39)
leo.penup()
leo.goto(-150,-30)
leo.pendown()
leo.fillcolor("pink")
leo.color("black",(0,150,72))

leo.speed(70)
leo.hideturtle()
leo.begin_fill()
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()

bob.color("black")
bob.penup()
bob.goto(-150,-30)
bob.pendown()
bob.speed(100)

g: int = 0
side_length: int = 300
while side_length > 1:
    g = 0
    while g < 3:
        bob.forward(side_length)
        bob.left(120.3)
        g += 1
    side_length *= 0.97

done()