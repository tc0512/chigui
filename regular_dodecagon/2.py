import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import turtle
import graphicssystem as gs
turtle.setup(720, 720)
turtle.setworldcoordinates(-4, -4, 4, 4)
A = gs.Point(0, 0)
A.plot(label="A")
c1 = gs.Circle(A, 1)
c1.plot(speed=0)
turtle.done()
