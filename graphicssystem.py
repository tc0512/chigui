# graphicssystem.py
# The base graphics system for reppsiository `chigui`
# popular alias: `gs`

import turtle
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

# ---------- Tests ---------- #
A = Point(0, 0)
A.plot("A")
B = Point(100, 100)
B.plot("B")
__import__("time").sleep(5)
B.delete()
turtle.done()
