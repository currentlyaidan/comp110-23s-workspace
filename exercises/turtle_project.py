"""'I want you more than any blue sky!' Update later with lines for attempted points"""

__author__ = "730679404"

from turtle import Turtle, colormode, done, Screen
from random import randint
screen = Screen()
colormode(255)
screen.setup(width=1.0, height=1.0, startx=0, starty=1)

def main() -> None:
    """The entrypoint of my scene."""
    # Declare Turtle variables
    city: Turtle = Turtle()
    city.hideturtle()
    # Call procedures which I define and use my turtles as arguments
    land()
    done()


def draw_to(x = int, y = int, turt = Turtle) -> None:
    """Draws a line to the given coordinates"""
    turt.pendown
    turt.speed(0)
    turt.hideturtle()
    turt.goto(x,y)


# Define the procedures for other components    
def land() -> None:
    """Draws the land."""
    land: Turtle = Turtle()
    land.hideturtle()
    land.color((237,223,192),(117,167,117))
    land.penup()
    land.goto(-733,0)
    land.pendown()
    land.speed(0)
    # Make land base
    land.begin_fill()
    draw_to(732,0,land)
    draw_to(732,-400,land)
    draw_to(-733,-400,land)
    draw_to(-733,0,land)
    land.end_fill()

    land.penup()
    land.goto(733,200)
    land.begin_fill()
    draw_to(100,200,land)
    draw_to(0,300,land)
    draw_to(-733,350,land)
    draw_to(-733,50,land)
    draw_to(-400,100,land)
    draw_to(0,50,land)
    draw_to(400,50,land)
    draw_to(733,100,land)
    draw_to(733,200,land)
    land.end_fill()


if __name__ == "__main__":
    main()