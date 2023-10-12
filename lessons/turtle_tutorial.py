"""Turtle Tutorial."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
i: int = 0
while i < 4:
    leo.forward(300)
    leo.left(90)
    i += 1

done()