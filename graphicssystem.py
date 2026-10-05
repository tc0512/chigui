# graphicssystem.py
# The base graphics system for reppsiository `chigui`
# popular alias: `gs`

import turtle
import math
import sympy as sp

screen = turtle.Screen()

class Point(sp.Point2D):
    def __init__(self, *args, **kwargs):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()

    def plot(self, label=""):
        self.t.clear()
        self.t.goto(float(self.x), float(self.y))
        self.t.dot(5)
        self.t.write(label)

    def delete(self):
        self.t.clear()

class Seg(sp.Segment2D):
    def __init__(self, *args, **kwargs):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()

    def plot(self):
        self.t.clear()
        self.t.goto(float(self.p1.x), float(self.p1.y))
        self.t.pendown()
        self.t.goto(float(self.p2.x), float(self.p2.y))
        self.t.penup()

    def delete(self):
        self.t.clear()

class Ray(sp.Ray2D):
    def __init__(self, *args, **kwargs):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()

    def plot(self):
        self.t.clear()
        x0 = float(self.source.x)
        y0 = float(self.source.y)
        dx = float(self.direction.x)
        dy = float(self.direction.y)
        angle = math.degrees(math.atan2(dy, dx))
        self.t.goto(x0, y0)
        self.t.setheading(angle)
        self.t.pendown()
        self.t.forward(100)
        self.t.penup()

    def delete(self):
        self.t.clear()

# ---------- Tests ---------- #
turtle.setup(720, 720)
turtle.setworldcoordinates(-10, -10, 10, 10)
s1 = Seg(Point(2, 3), Point(0, 0))
s2 = Seg(Point(0, 0), Point(1, 1))
s1.plot()
s2.plot()
turtle.done()
