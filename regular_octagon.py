import turtle
import math
import graphicssystem as gs

turtle.setup(720, 720)
turtle.setworldcoordinates(-5, -5, 5, 5)
O = gs.Point(0, 0)
O.plot(label="O")
c1 = gs.Circle(O, 1)
c1.plot(speed=0)
turtle.done()
