import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import turtle
import sympy as sp
import graphicssystem as gs

turtle.setup(720, 720)
turtle.setworldcoordinates(-2, -2, 3, 3)
A = gs.Point(0, 0)
B = gs.Point(1, 0)
s1 = gs.Seg(A, B)
s1.plot(c="red")
A.plot(label="A")
B.plot(label="B")
C = gs.Point(2/5, 1/5)
C.plot(label="C")
c1 = gs.Circle(C, A.distance(C))
c1.plot()
p = c1.intersection(s1)[1]
D = gs.Point(p.x, p.y)
D.plot(label="D")
r1 = gs.Ray(D, C)
p1, p2 = r1.intersection(c1)
E = gs.Point(p1.x, p1.y)
s2 = gs.Seg(D, E)
s2.plot()
E.plot(label="E")
c2 = gs.Circle(A, A.distance(B))
c2.plot()
r2 = gs.Ray(A, E)
p = r2.intersection(c2)[0]
F = gs.Point(p.x, p.y)
s3 = gs.Seg(A, F)
s3.plot(c="red")
F.plot(label="F")
c3 = gs.Circle(B, A.distance(B))
c3.plot()
c4 = gs.Circle(F, A.distance(F))
c4.plot()
p1, p2 = c3.intersection(c4)
G = gs.Point(p2.x, p2.y)
G.plot(label="G")
s4 = gs.Seg(F, G)
s4.plot(c="red")
s5 = gs.Seg(G, B)
s5.plot(c="red")
turtle.done()
