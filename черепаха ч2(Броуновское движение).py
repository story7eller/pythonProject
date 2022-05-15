import turtle
import numpy as np
from random import random, randint

turtle.color('red')
def a():
    return(randint(0, 360))


turtle.speed(1000)
turtle.shape('turtle')

for i in range(10000):
    x = a()
    y = a()/10
    turtle.setheading(x)
    turtle.forward(y)
turtle.go()

