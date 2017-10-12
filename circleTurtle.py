import turtle
import math

def circleTurtle():
    deg = 0
    r = 150
    while deg <= math.radians(360):
        xcor = r*math.cos(deg)
        ycor = r*math.sin(deg)
        turtle.goto(xcor, ycor)
        deg += math.radians(1)


def main():
    turtle.delay(0)
    turtle.pu()
    turtle.goto(150*math.cos(0), 150*math.sin(0))
    turtle.pd()
    circleTurtle()


if __name__ == '__main__':
    main()
