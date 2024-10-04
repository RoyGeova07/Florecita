from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0, -40)

# Aqui se dibuja la flor
for i in range(16):
    for j in range(16):
        color('#FFA216')
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

color('black')
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
golden_ang = 137.508
phi = golden_ang * (pi / 180)

for i in range(140):
    r = 4 * sqrt(i)
    theta = i * phi
    x = r * cos(theta)
    y = r * sin(theta)
    penup()
    goto(x, y)
    setheading(i * golden_ang)
    pendown()
    stamp()

def circulo(x, y):
    penup()
    goto(x, y)
    pendown()
    color('black')
    fillcolor('#FFA216')
    begin_fill()
    circle(3)
    end_fill()

def Dibujar_R(x, y):
    Posicion_R = [(x,y),(x,y+20),(x+12,y+20),(x+12,y+10),
                  (x,y+10),(x,y),(x+12,y),(x+12,y+5)]

    for pos in Posicion_R:
        circulo(*pos)

def Dibujar_O(x,y):
    circulo(x+12,y+10)
    
def Dibujar_Y(x,y):
    Posicion_Y = [(x,y+20),(x+10,y+10),(x+20,y+20),
                  (x+10,y+10),(x+10,y),(x+20,y),(x+10,y)]
    
    for pos in Posicion_Y:
        circulo(*pos)
    


Dibujar_R(-60, 30)  #
Dibujar_O(-10, 30)  
Dibujar_Y(40, 30)   

hideturtle()
done()
