import turtle
import math
import numpy as np

x0 = -200
y0 = 1
V0 = 40
a = 1                            # Угол альфа в радианах
V0x = V0*math.cos(a)
V0y = V0*math.sin(a)
g = 9.8                          # скорость свободного падения
t = 1
Vx = V0*math.cos(a)             # скорость изменения Х
x = x0 + Vx * t
y = V0 * math.sin(a) * t - g*t**2/2
y1 = (-g/(2*V0**2*math.cos(a)**2)) * x**2 + math.tan(a)*x
Vy = V0 * math.sin(a) - g*t
tp = 2*V0*math.sin(a)/g        #время полета
t1 = 2*V0*math.sin(a)/(g*2)    #время через которое точка занимает самое высокое положение
H = V0**2 * math.sin(a)**2/(2*g) #высота максимальная
L = (V0**2 * 2*(math.sin(a)*math.cos(a)))/g  # растояние которое пролетает точка
q = 0

def L(V0):
    L = L = (V0**2 * 2*(math.sin(a)*math.cos(a)))/g
    return L



def current_x(t):

    current_x = x0 + Vx * t
    x = current_x
    return x


def current_y(t):
    current_y = y0 + V0 * math.sin(a) * t - g*t**2/2
    y = current_y
    return y


turtle.penup()
turtle.goto(-200, 1)
turtle.pendown()
turtle.shape('circle')



def Vx(V0):
    Vx = V0 * math.cos(a)
    return Vx
def Vy(V0, t):
    Vy = V0 * math.sin(a) - g * t
    return Vy



def x(t,V0):
    x = x0 + Vx(V0)*t
    return x
def y(t,V0):
    y = V0 * math.sin(a) * t - g*t**2/2
    return y
def tp(V0):
    tp = 2 * V0 * math.sin(a) / g
    return tp


T = tp(V0)*10
Ti = int(T)

def Hill(V0):
    turtle.goto(x0,y0)
    T = tp(V0) * 10
    Ti = int(T)

    for t in range(1,Ti,1):
        t = t /10
        Vx(V0)
        Vy(V0,t)
        x(t,V0)
        y(t,V0)
        X = x(t,V0)
        Y = y (t,V0)
        if Y >= 0:
            turtle.goto(X,Y)

        if Y <= 0:
            q = t
            return q


V0 = 60
for i in range(7):
    V0 = V0*0.75
    Hill(V0)
    x0 = x0 + L(V0)
















