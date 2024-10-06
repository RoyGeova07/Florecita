from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0,-40)

# Draw leaves
for i in range(16):
    for j in range(18):
        color('#FFA216'), rt(90)
        circle(150-j*6, 90), lt(90)
        circle(150-j*6, 90), rt(180)
    circle(40,24)

# aqui se dibuja el centro de la flor
color('black') 
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
golden_ang = 137.508
phi = golden_ang*(pi/180)

for i in range(140):
    r = 4*sqrt(i)
    theta = i*phi
    x = r*cos(theta)
    y = r*sin(theta)
    penup(), goto(x, y)
    setheading(i*golden_ang)
    pendown(), stamp()

# aqui se define los puntos para dibujar las letras con un tamanio mejor
def point(x, y, radius=6):
    penup(), goto(x, y), pendown()
    color('white'), fillcolor('#FFA216')  
    begin_fill(), circle(radius), end_fill()

# Funcion para R
def Dibujar_R(x, y):
    Posicion_R = [(x, y), (x, y+9), (x, y+18), (x, y+27), (x, y+36),
                   (x+9, y+36), (x+18, y+36), (x+18, y+27), (x+18, y+18),
                   (x+9, y+18), (x, y+18), (x+18, y), (x+9, y+9)]
    
    for pos in Posicion_R:
        point(*pos, radius=5)

# Funcion para O
def Dibujar_O(x, y):
    Posicion_O = [(x, y+6), (x, y+12), (x, y+18), (x, y+24),
                   (x+6, y+30), (x+12, y+24), (x+12, y+18), (x+12, y+12), (x+12, y+6),
                   (x+6, y), (x, y+6)]
    
    for pos in Posicion_O:
        point(*pos, radius=5)

# Funcion para Y
def Dibujar_Y(x, y):
    Posicion_Y = [(x, y+30), (x+6, y+24), (x+12, y+18), 
                   (x+12, y+12), (x+12, y+6), (x+12, y),
                   (x+18, y+18), (x+24, y+24), (x+30, y+30)]
    
    for pos in Posicion_Y:
        point(*pos, radius=5)

# aqui se centre las letrAs
Dibujar_R(-50, -20)  
Dibujar_O(-10, -20)  
Dibujar_Y(20, -20)   

hideturtle()
done()

