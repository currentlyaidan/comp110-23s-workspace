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
    # Call procedures which I define and use my turtles as arguments
    land()
    water()
    hinapants()
    hinashirt()
    hinajacket()
    repeat: int = 0
    while repeat < 150:
        city(randint(-733,720),randint(-400,0),randint(10,100),randint(5,50))
        repeat += 1
    done()


def prepare_pen(x: int, y: int,turt: Turtle) -> None:
    """Gets the pen in the right spot, saves lines of code, and prepares to draw."""
    turt.hideturtle()
    turt.speed(0)
    turt.penup()
    turt.goto(x,y)
    turt.pendown()


def draw_to(x = int, y = int, turt = Turtle) -> None:
    """Draws a line to the given coordinates."""
    turt.pendown
    turt.speed(0)
    turt.hideturtle()
    turt.goto(x,y)


def hinapants() -> None:
    """Draws Hina's pants."""
    pants: Turtle = Turtle()
    prepare_pen(-300,410,pants)
    pants.color((0,0,0),(176,136,254))
    pants.begin_fill()
    pants.goto(-300,375)
    pants.goto(-298,360)
    pants.goto(-260,356)
    pants.goto(-210,358)
    pants.goto(-170,364)
    pants.goto(-140,370)
    pants.goto(-137,410)
    pants.goto(-300,410)
    pants.end_fill()
    pants.penup()
    pants.goto(-170,370)
    pants.pendown()
    pants.goto(-205,380)
    pants.goto(-215,377)

def hinashirt() -> None:
    """Draws Hina's shirt."""
    shirt: Turtle = Turtle()
    prepare_pen(-300,375,shirt)
    shirt.color((0,0,0),(227,152,250))
    shirt.begin_fill()
    shirt.goto(-310,375)
    shirt.goto(-310,345)
    shirt.goto(-305,320)
    shirt.goto(-240,324)
    shirt.goto(-200,327)
    shirt.goto(-180,330)
    shirt.goto(-160,333)
    shirt.goto(-140,337)
    shirt.goto(-134,340)
    shirt.goto(-132,344)
    shirt.goto(-133,385)
    shirt.goto(-138,384)
    shirt.goto(-140,370)
    shirt.goto(-170,364)
    shirt.goto(-210,358)
    shirt.goto(-260,356)
    shirt.goto(-298,360)
    shirt.goto(-300,375)
    shirt.end_fill()

def hinajacket() -> None:
    """Draws Hina's jacket."""
    jacket: Turtle = Turtle()
    prepare_pen(-310,345,jacket)
    jacket.color((0,0,0),(249,237,252))
    jacket.begin_fill()
    jacket.goto(-314,345)
    jacket.goto(-315,343)
    jacket.goto(-311,303)
    jacket.goto(-300,303)
    jacket.goto(-311,302)
    jacket.goto(-312,297)
    jacket.goto(-330,260)
    jacket.goto(-331,259)
    jacket.goto(-332,254)
    jacket.goto(-331,248)
    jacket.goto(-331,245)
    jacket.goto(-290,140)
    jacket.goto(-297,160)
    jacket.goto(-310,140)
    jacket.goto(-311,138)
    jacket.goto(-309,135)
    jacket.goto(-297,120)
    jacket.goto(-297,117)
    jacket.goto(-297,113)
    jacket.goto(-304,-20)
    jacket.goto(-305,-30)
    jacket.goto(-303,-33)
    jacket.goto(-280,-70)
    jacket.goto(-303,-33)
    jacket.goto(-340,-46)
    jacket.goto(-360,-47)
    jacket.goto(-375,-45)
    jacket.goto(-380,-45)
    jacket.goto(-390,-60)
    jacket.goto(-391,-61)
    jacket.goto(-389,-65)
    jacket.goto(-380,-85)
    jacket.goto(-377,-110)
    jacket.goto(-375,-114)
    jacket.goto(-373,-116)
    jacket.goto(-330,-150)
    jacket.goto(-115,-20)
    jacket.goto(-110,10)
    jacket.goto(-107,40)
    jacket.goto(-114,100)
    jacket.goto(-123,120)
    jacket.goto(-135,140)
    jacket.goto(-150,120)
    jacket.goto(-135,140)
    jacket.goto(-120,185)


# Define the procedures for other components    
def water() -> None:
    """Draws the water."""
    water: Turtle = Turtle()
    water.color((101,152,193),(101,152,193))
    prepare_pen(-733,0,water)
    water.begin_fill()
    draw_to(732,0,water)
    draw_to(732,100,water)
    draw_to(400,50,water)
    draw_to(0,50,water)
    draw_to(-400,100,water)
    draw_to(-733,50,water)
    draw_to(-733,0,water)
    draw_to(732,0,water)
    water.end_fill()
    # Fill in top of screen
    water.penup()
    water.goto(733,410)
    water.pendown()
    water.begin_fill()
    draw_to(-733,350,water)
    draw_to(0,300,water)
    draw_to(100,200,water)
    draw_to(733,200,water)
    draw_to(732,410,water)
    draw_to(-733,410,water)
    draw_to(-733,350,water)
    water.end_fill()

def land() -> None:
    """Draws the land."""
    land: Turtle = Turtle()
    land.color((237,223,192),(117,167,117))
    prepare_pen(-733,0,land)
    # Make land base
    land.begin_fill()
    draw_to(732,0,land)
    draw_to(732,-400,land)
    draw_to(-733,-400,land)
    draw_to(-733,0,land)
    land.end_fill()
    # Second part of land base
    land.penup()
    land.goto(732,200)
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

def city(x: int, y: int,height: int, width: int) -> None:
    """Draw an urban formation at a set point"""
    city: Turtle = Turtle()
    city.hideturtle()
    color: int = randint(75,155)
    city.color((color,color,color),(color,color,color))
    prepare_pen(x,y,city)
    city.begin_fill()
    city.seth(330)
    city.forward(width)
    city.seth(30)
    city.forward(width)
    city.seth(90)
    city.forward(height)
    city.seth(210)
    city.forward(width)
    city.seth(150)
    city.forward(width)
    city.seth(270)
    city.forward(height)
    city.end_fill()
    # make top of building lighter
    city.penup()
    city.goto(x,(y+height))
    city.pendown()
    top_color: int = randint(200,230)
    city.color((top_color,top_color,top_color),(top_color,top_color,top_color))
    city.begin_fill()
    city.seth(330)
    city.forward(width)
    city.seth(30)
    city.forward(width)
    city.seth(150)
    city.forward(width)
    city.seth(210)
    city.forward(width)
    city.end_fill()



if __name__ == "__main__":
    main()