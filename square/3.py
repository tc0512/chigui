import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import turtle
import sympy as sp
import graphicssystem as gs

turtle.setup(720, 720)
turtle.setworldcoordinates(-5, -5, 5, 5)
A = gs.Point(0, 0)
B = gs.Point(1, 0)
s1 = gs.Seg(A, B)
s1.plot(c="red")
A.plot(label="A")
B.plot(label="B")
C = gs.Point(2/5, 1/5)
C.plot(label="C")
c1 = gs.Circle(C, float(A.distance(C)))
c1.plot(speed=0)
p = c1.intersection(s1)[0]
D = gs.Point(p.x, p.y)
D.plot(label="D")
r = gs.Ray(D, C)
p1, p2 = r.intersection(c1)
E = gs.Point(p1.x, p1.y)
s2 = gs.Seg(D, E)
s2.plot()
E.plot(label="E")
turtle.done()
