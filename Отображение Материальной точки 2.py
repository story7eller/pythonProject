import turtle
import math
x0 = -100
y0 = 1
V0 = 40
a = 1 # Угол альфа в радианах
V0x = V0*math.cos(a)
V0y = V0*math.sin(a)
g = 9.8
t = 1
Vx = V0*math.cos(a)

x = Vx * t
y = V0 * math.sin(a) * t - g*t**2/2
Vy = V0 * math.sin(a) - g*t
tp = 2*V0*math.sin(a)/g
t1 = 2*V0*math.sin(a)/(g*2)
H = V0**2 * math.sin(a)**2/(2*g)
turtle.penup()
turtle.goto(x0, y0)
turtle.pendown()
turtle.speed(1)
for i in range(100):
    x = x0 + V0*math.cos(a) * t
    y = y0 + V0 * math.sin(a) * t - g * t ** 2 / 2
    turtle.goto(x, y)
    t = t + 0.1


print(t1, tp, H)


