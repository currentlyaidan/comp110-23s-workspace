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
leo.color("black","pink")

leo.begin_fill()
while i < 4:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

done()