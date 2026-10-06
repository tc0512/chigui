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
        self.t.setundobuffer(None)
        self.t.hideturtle()
        self.t.penup()

    def plot(self, speed=3, label="", c="black"):
        self.t.clear()
        self.t.speed(speed)
        self.t.goto(float(self.x), float(self.y))
        self.t.pencolor(c)
        self.t.dot(5)
        self.t.write(label)

    def delete(self):
        self.t.clear()

class Seg(sp.Segment2D):
    def __init__(self, *args, **kwargs):
        self.t = turtle.Turtle()
        self.t.setundobuffer(None)
        self.t.hideturtle()
        self.t.penup()

    def plot(self, speed=3, label="", c="black"):
        self.t.clear()
        self.t.speed(speed)
        self.t.goto(float(self.p1.x), float(self.p1.y))
        self.t.pendown()
        self.t.pencolor(c)
        self.t.goto(float(self.p2.x), float(self.p2.y))
        self.t.write(label)
        self.t.penup()

    def delete(self):
        self.t.clear()

class Ray(sp.Ray2D):
    def __init__(self, *args, **kwargs):
        self.t = turtle.Turtle()
        self.t.setundobuffer(None)
        self.t.hideturtle()
        self.t.penup()

    def plot(self, speed=3, L=1000, label="", c="black"):
        self.t.clear()
        x0 = float(self.source.x)
        y0 = float(self.source.y)
        dx = float(self.direction.x)
        dy = float(self.direction.y)
        angle = math.degrees(math.atan2(dy, dx))
        self.t.speed(speed)
        self.t.goto(x0, y0)
        self.t.pencolor(c)
        self.t.write(label)
        self.t.setheading(angle)
        self.t.pendown()
        self.t.forward(L)
        self.t.penup()

    def delete(self):
        self.t.clear()

class Line(sp.Line2D):
    def __init__(self, *args, **kwargs):
        self.t = turtle.Turtle()
        self.t.setundobuffer(None)
        self.t.hideturtle()
        self.t.penup()

    def plot(self, speed=3, L=1000, label="", c="black"):
        self.t.clear()
        p1 = self.p1
        p2 = self.p2
        x1, y1 = float(p1.x), float(p1.y)
        x2, y2 = float(p2.x), float(p2.y)
        dx = x2-x1
        dy = y2-y1
        norm = math.hypot(dx, dy)
        dx /= norm
        dy /= norm
        self.t.speed(speed)
        self.t.pencolor(c)
        self.t.goto(x1, y1)
        self.t.write(label)
        self.t.goto(x1-dx*L, y1-dy*L)
        self.t.pendown()
        self.t.goto(x2+dx*L, y2+dy*L)
        self.t.penup()

    def delete(self):
        self.t.clear()

class Circle(sp.Circle):
    def __init__(self, *args, **kwargs):
        self.t = turtle.Turtle()
        self.t.setundobuffer(None)
        self.t.hideturtle()
        self.t.penup()

    def plot(self, steps=100, speed=3, label="", c="black"):
        self.t.clear()
        cx = float(self.center.x)
        cy = float(self.center.y)
        r = float(self.radius)
        self.t.goto(cx, cy - r)
        self.t.setheading(0)
        self.t.pendown()
        self.t.speed(speed)
        self.t.pencolor(c)
        self.t.write(label)
        self.t.circle(r, steps=steps)
        self.t.penup()
        self.t.speed(3)

    def delete(self):
        self.t.clear()
