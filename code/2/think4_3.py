from swampy.TurtleWorld import *
import math


def square(t, length, sides):
    angle = int(360 / sides)
    radius = abs(length / (2 * math.sin(math.pi / sides)))
    print radius
    print math.pi
    print math.sin(math.pi / sides)
    print sides
    print length
    interior_angle = (180 - 360 / sides) / 2
    for i in range(0, sides):
        fd(t, length)
        lt(t, angle)
    for i in range(1, sides):
        lt(t, interior_angle)
        fd(t, radius)
        rt(t, 180 - angle)
        fd(t, radius)
        lt(t, 180 - interior_angle)
    print t


def next_polygon(t, length):
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
polygon_turtle = Turtle()
polygon_turtle.set_delay(0.00001)
next_polygon(polygon_turtle, -150)
square(polygon_turtle, 80, 5)
next_polygon(polygon_turtle, 200)
square(polygon_turtle, 80, 6)
next_polygon(polygon_turtle, -300)
square(polygon_turtle, 80, 7)
wait_for_user()
