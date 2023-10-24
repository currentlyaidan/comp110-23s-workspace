"""'I want you more than any blue sky!' Randomness used in line 24 to generate the background, Loops used to create the city."""

__author__ = "730679404"

from turtle import Turtle, colormode, done, Screen
from random import randint
screen = Screen()
colormode(255)
screen.setup(width=1.0, height=1.0, startx=0, starty=1)


def main() -> None:
    """The entrypoint of my scene."""
    land()
    water()
    repeat: int = 0
    while repeat < 1:
        city(randint(-733, 720), randint(-400, 0), randint(10, 100), randint(5, 50))
        repeat += 1
    hinapants()
    hinashirt()
    hinajacket()
    hina()
    hinaface()
    hinahair()
    done()


def prepare_pen(x: int, y: int, turt: Turtle) -> None:
    """Gets the pen in the right spot, saves lines of code, and prepares to draw."""
    turt.hideturtle()
    turt.speed(0)
    turt.penup()
    turt.goto(x, y)
    turt.pendown()


def draw_to(x: int, y: int, turt: Turtle) -> None:
    """Draws a line to the given coordinates."""
    turt.pendown
    turt.speed(0)
    turt.hideturtle()
    turt.goto(x, y)


def hinapants() -> None:
    """Draws Hina's pants."""
    pants: Turtle = Turtle()
    prepare_pen(-300, 410, pants)
    pants.color((0, 0, 0), (176, 136, 254))
    pants.begin_fill()
    pants.goto(-300, 375)
    pants.goto(-298, 360)
    pants.goto(-260, 356)
    pants.goto(-210, 358)
    pants.goto(-170, 364)
    pants.goto(-140, 370)
    pants.goto(-137, 410)
    pants.goto(-300, 410)
    pants.end_fill()
    pants.penup()
    pants.goto(-170, 370)
    pants.pendown()
    pants.goto(-205, 380)
    pants.goto(-215, 377)


def hinashirt() -> None:
    """Draws Hina's shirt."""
    shirt: Turtle = Turtle()
    prepare_pen(-300, 375, shirt)
    shirt.color((0, 0, 0), (227, 152, 250))
    shirt.begin_fill()
    shirt.goto(-310, 375)
    shirt.goto(-310, 345)
    shirt.goto(-305, 320)
    shirt.goto(-240, 324)
    shirt.goto(-200, 327)
    shirt.goto(-180, 330)
    shirt.goto(-160, 333)
    shirt.goto(-140, 337)
    shirt.goto(-134, 340)
    shirt.goto(-132, 344)
    shirt.goto(-133, 385)
    shirt.goto(-138, 384)
    shirt.goto(-140, 370)
    shirt.goto(-170, 364)
    shirt.goto(-210, 358)
    shirt.goto(-260, 356)
    shirt.goto(-298, 360)
    shirt.goto(-300, 375)
    shirt.end_fill()


def hinajacket() -> None:
    """Draws Hina's jacket."""
    jacket: Turtle = Turtle()
    prepare_pen(-310, 345, jacket)
    jacket.color((0, 0, 0), (249, 237, 252))
    jacket.begin_fill()
    jacket.goto(-314, 345)
    jacket.goto(-315, 343)
    jacket.goto(-311, 303)
    jacket.goto(-300, 303)
    jacket.goto(-311, 302)
    jacket.goto(-312, 297)
    jacket.goto(-330, 260)
    jacket.goto(-331, 259)
    jacket.goto(-332, 254)
    jacket.goto(-331, 248)
    jacket.goto(-331, 245)
    jacket.goto(-290, 140)
    jacket.goto(-297, 160)
    jacket.goto(-310, 140)
    jacket.goto(-311, 138)
    jacket.goto(-309, 135)
    jacket.goto(-297, 120)
    jacket.goto(-297, 117)
    jacket.goto(-297, 113)
    jacket.goto(-304, -20)
    jacket.goto(-305, -30)
    jacket.goto(-303, -33)
    jacket.goto(-280, -70)
    jacket.goto(-303, -33)
    jacket.goto(-340, -46)
    jacket.goto(-360, -47)
    jacket.goto(-375, -45)
    jacket.goto(-380, -45)
    jacket.goto(-390, -60)
    jacket.goto(-391, -61)
    jacket.goto(-389, -65)
    jacket.goto(-380, -85)
    jacket.goto(-377, -110)
    jacket.goto(-375, -114)
    jacket.goto(-373, -116)
    jacket.goto(-330, -150)
    jacket.goto(-115, -20)
    jacket.goto(-190, -40)
    jacket.goto(-115, -20)
    jacket.goto(-110, 10)
    jacket.goto(-107, 40)
    jacket.goto(-114, 100)
    jacket.goto(-123, 120)
    jacket.goto(-135, 140)
    jacket.goto(-150, 120)
    jacket.goto(-135, 140)
    jacket.goto(-120, 185)
    jacket.goto(-100, 240)
    jacket.goto(-101, 290)
    jacket.goto(-110, 300)
    jacket.goto(-120, 300)
    jacket.goto(-110, 301)
    jacket.goto(-111, 335)
    jacket.goto(-123, 340)
    jacket.goto(-124, 360)
    jacket.goto(-133, 363)
    jacket.goto(-133, 385)
    jacket.goto(-132, 344)
    jacket.goto(-134, 340)
    jacket.goto(-140, 337)
    jacket.goto(-160, 333)
    jacket.goto(-180, 330)
    jacket.goto(-200, 327)
    jacket.goto(-240, 324)
    jacket.goto(-305, 320)
    jacket.goto(-310, 345)
    jacket.end_fill()
    # Pockets.
    jacket.penup()
    jacket.goto(-130, 300)
    jacket.pendown()
    jacket.goto(-180, 270)
    jacket.goto(-200, 270)
    jacket.goto(-201, 250)
    jacket.goto(-195, 220)
    jacket.goto(-170, 190)
    jacket.goto(-165, 170)
    jacket.goto(-135, 165)
    jacket.goto(-120, 190)
    jacket.penup()
    jacket.goto(-185, 240)
    jacket.pendown()
    jacket.goto(-160, 190)
    jacket.goto(-155, 175)
    # Undershirt.
    jacket.penup()
    jacket.goto(-250, 90)
    jacket.pendown()
    jacket.color((0, 0, 0), (248, 99, 189))
    jacket.begin_fill()
    jacket.goto(-270, 50)
    jacket.goto(-280, 10)
    jacket.goto(-200, 10)
    jacket.goto(-230, 70)
    jacket.goto(-250, 90)
    jacket.end_fill()


def hina() -> None:
    """Draw's Hina."""
    hina: Turtle = Turtle()
    prepare_pen(-140, -30, hina)
    hina.color((0, 0, 0), (255, 247, 215))
    hina.begin_fill()
    hina.goto(-138, -45)
    hina.goto(-130, -45)
    hina.goto(-90, -20)
    hina.goto(-88, -21)
    hina.goto(-86, -21)
    hina.goto(-86, -22)
    hina.goto(-73, -50)
    hina.goto(-70, -50)
    hina.goto(-67, -50)
    hina.goto(-60, -65)
    hina.goto(-47, -77)
    hina.goto(-46, -78)
    hina.goto(-46, -78)
    hina.goto(-45, -80)
    hina.goto(-74, -105)
    hina.goto(-75, -112)
    hina.goto(-75, -115)
    hina.goto(-76, -117)
    hina.goto(-68, -130)
    hina.goto(-65, -132)
    hina.goto(-63, -135)
    hina.goto(-61, -150)
    hina.goto(-60, -175)
    hina.goto(-62, -200)
    hina.goto(-69, -210)
    hina.goto(-90, -235)
    hina.goto(-130, -240)
    hina.goto(-170, -245)
    hina.goto(-200, -240)
    hina.goto(-210, -230)
    hina.goto(-250, -180)
    hina.goto(-250, -130)
    hina.goto(-200, -80)
    hina.goto(-200, -60)
    hina.goto(-140, -30)
    hina.end_fill()
    # Arm.
    hina.penup()
    hina.goto(-280, 10)
    hina.pendown()
    hina.begin_fill()
    hina.goto(-270, 30)
    hina.goto(-250, 40)
    hina.goto(-230, 50)
    hina.goto(-250, 30)
    hina.goto(-230, 50)
    hina.goto(-190, 90)
    hina.goto(-70, 150)
    hina.goto(-60, 155)
    hina.goto(-40, 160)
    hina.goto(-20, 130)
    hina.goto(-10, 100)
    hina.goto(0, 20)
    hina.goto(5, 10)
    hina.goto(15, -7)
    hina.goto(20, -30)
    hina.goto(22, -40)
    hina.goto(14, -45)
    hina.goto(9, -32)
    hina.goto(4, -37)
    hina.goto(3, -50)
    hina.goto(-4, -57)
    hina.goto(-8, -47)
    hina.goto(-8, -59)
    hina.goto(-15, -65)
    hina.goto(-16, -60)
    hina.goto(-20, -45)
    hina.goto(-27, -40)
    hina.goto(-27, -60)
    hina.goto(-26, -63)
    hina.goto(-24, -65)
    hina.goto(-25, -68)
    hina.goto(-27, -69)
    hina.goto(-33, -65)
    hina.goto(-39, -30)
    hina.goto(-34, -60)
    hina.goto(-40, -58)
    hina.goto(-47, -27)
    hina.goto(-47, -23)
    hina.goto(-40, -6)
    hina.goto(-30, 4)
    hina.goto(-55, 87)
    hina.goto(-60, 93)
    hina.goto(-200, 0)
    hina.goto(-202, -20)
    hina.goto(-214, -40)
    hina.goto(-230, -50)
    hina.goto(-250, -50)
    hina.goto(-270, -30)
    hina.goto(-274, -20)
    hina.goto(-280, 10)
    hina.end_fill()


def hinaface() -> None:
    """Draws Hina's face."""
    face: Turtle = Turtle()
    prepare_pen(-100,-145, face)
    face.color((0, 0, 0), (0, 0, 0))
    face.begin_fill()
    face.goto(-90, -135)
    face.goto(-87,-128)
    face.goto(-92,-130)
    face.goto(-88,-124)
    face.goto(-96,-130)


def hinahair() -> None:
    """Draws Hina's hair."""
    hair: Turtle = Turtle()
    prepare_pen(-23, -60, hair)
    hair.color((0, 0, 0), (68, 68, 68))
    hair.begin_fill()
    hair.goto(-10, -145)
    hair.goto(-6, -165)
    hair.goto(-7, -200)
    hair.goto(-11, -210)
    hair.goto(-70, -265)
    hair.goto(-140, -270)
    hair.goto(-160, -280)
    hair.goto(-200, -280)
    hair.goto(-250, -260)
    hair.goto(-267, -240)
    hair.goto(-268, -200)
    hair.goto(-265, -140)
    hair.goto(-230, -90)
    hair.goto(-210, -80)
    hair.goto(-200, -60)
    hair.goto(-190, -55)
    hair.goto(-170, -100)
    hair.goto(-180, -110)
    hair.goto(-185, -120)
    hair.goto(-185, -130)
    hair.goto(-170, -135)
    hair.goto(-140, -150)
    hair.goto(-143, -130)
    hair.goto(-145, -110)
    hair.goto(-133, -90)
    hair.goto(-135, -70)
    hair.goto(-136, -67)
    hair.goto(-136, -62)
    hair.goto(-128, -100)
    hair.goto(-131, -120)
    hair.goto(-120, -150)
    hair.goto(-115, -170)
    hair.goto(-95, -185)
    hair.goto(-97, -181)
    hair.goto(-98, -176)
    hair.goto(-98, -166)
    hair.goto(-96, -163)
    hair.goto(-80, -140)
    hair.goto(-40, -120)
    hair.goto(-30, -100)
    hair.goto(-23, -60)
    hair.end_fill()
    # Pigtail.
    hair.penup()
    hair.color((0, 0, 0), (74, 74, 74))
    hair.goto(-180, -130)
    hair.begin_fill()
    hair.pendown()
    hair.goto(-165, -138)
    hair.goto(-175, -150)
    hair.goto(-200, -145)
    hair.goto(-230, -160)
    hair.goto(-280, -165)
    hair.goto(-310, -160)
    hair.goto(-340, -149)
    hair.goto(-360, -120)
    hair.goto(-363, -115)
    hair.goto(-367, -106)
    hair.goto(-368, -90)
    hair.goto(-400, -85)
    hair.goto(-430, -87)
    hair.goto(-400, -80)
    hair.goto(-370, -80)
    hair.goto(-365, -83)
    hair.goto(-367, -60)
    hair.goto(-350, -40)
    hair.goto(-345, -20)
    hair.goto(-343, -40)
    hair.goto(-344, -60)
    hair.goto(-330, -90)
    hair.goto(-315, -40)
    hair.goto(-290, -20)
    hair.goto(-285, 10)
    hair.goto(-285, 20)
    hair.goto(-280, 10)
    hair.goto(-273, -30)
    hair.goto(-275, -50)
    hair.goto(-270, -70)
    hair.goto(-275, -50)
    hair.goto(-250, -15)
    hair.goto(-240, -10)
    hair.goto(-230, 0)
    hair.goto(-228, 10)
    hair.goto(-225, -10)
    hair.goto(-245, -45)
    hair.goto(-260, -80)
    hair.goto(-250, -58)
    hair.goto(-190, -120)
    hair.goto(-200, -145)
    hair.goto(-190, -120)
    hair.goto(-180, -130)
    hair.end_fill()

 
def water() -> None:
    """Draws the water."""
    water: Turtle = Turtle()
    water.color((101, 152, 193), (101, 152, 193))
    prepare_pen(-733, 0, water)
    water.begin_fill()
    draw_to(732, 0, water)
    draw_to(732, 100, water)
    draw_to(400, 50, water)
    draw_to(0, 50, water)
    draw_to(-400, 100, water)
    draw_to(-733, 50, water)
    draw_to(-733, 0, water)
    draw_to(732, 0, water)
    water.end_fill()
    # Fill in top of screen
    water.penup()
    water.goto(733, 410)
    water.pendown()
    water.begin_fill()
    draw_to(-733, 350, water)
    draw_to(0, 300, water)
    draw_to(100, 200, water)
    draw_to(733, 200, water)
    draw_to(732, 410, water)
    draw_to(-733, 410, water)
    draw_to(-733, 350, water)
    water.end_fill()


def land() -> None:
    """Draws the land."""
    land: Turtle = Turtle()
    land.color((237, 223, 192), (117, 167, 117))
    prepare_pen(-733, 0, land)
    # Make land base
    land.begin_fill()
    draw_to(732, 0, land)
    draw_to(732, -400, land)
    draw_to(-733, -400, land)
    draw_to(-733, 0, land)
    land.end_fill()
    # Second part of land base
    land.penup()
    land.goto(732, 200)
    land.begin_fill()
    draw_to(100, 200, land)
    draw_to(0, 300, land)
    draw_to(-733, 350, land)
    draw_to(-733, 50, land)
    draw_to(-400, 100, land)
    draw_to(0, 50, land)
    draw_to(400, 50, land)
    draw_to(733, 100, land)
    draw_to(733, 200, land)
    land.end_fill()


def city(x: int, y: int, height: int, width: int) -> None:
    """Draw an urban formation at a set point."""
    city: Turtle = Turtle()
    city.hideturtle()
    color: int = randint(75, 155)
    city.color((color, color, color), (color, color, color))
    prepare_pen(x, y, city)
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
    city.goto(x, (y + height))
    city.pendown()
    top_color: int = randint(200, 230)
    city.color((top_color, top_color, top_color), (top_color, top_color, top_color))
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