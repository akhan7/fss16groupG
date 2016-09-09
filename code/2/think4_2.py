from swampy.TurtleWorld import *
import math


def next_flower(t, length):
    pu(t)
    fd(t, length)
    pd(t)


def flower_line(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    flower_line(t, n, step_length, step_angle)
    lt(t, 180 - angle)
    flower_line(t, n, step_length, step_angle)


def flowers(t, sides, a, x):
    angle = 360 / sides
    for i in range(0, sides):
        arc(petal_turtle, 100, a * angle)
        lt(petal_turtle, x * angle)
        print petal_turtle


world = TurtleWorld()
petal_turtle = Turtle()
petal_turtle.set_delay(0.00001)
next_flower(petal_turtle, -100)
flowers(petal_turtle, 7, 1, 1.5)
next_flower(petal_turtle, 200)
flowers(petal_turtle, 10, 2, 2)
next_flower(petal_turtle, 200)
flowers(petal_turtle, 20, 1, 2)

wait_for_user()
