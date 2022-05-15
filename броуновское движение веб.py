import turtle
from random import randint


number_of_turtles = 25
steps_of_time_number = 100

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.setheading(randint(0, 360))
    unit.turtlesize(0.4)



for i in range(steps_of_time_number):
    for g in range(len(pool)):
        angle1 = pool[g].heading()
        x1, y1 = pool[g].pos()
        for h in range(len(pool)):
            if g != h:
                x2, y2 = pool[h].pos()
                angle2 = pool[h].heading()
                dx = abs(x2 - x1)
                dy = abs(y2 - y1)
                if dx <= 4 and dy <= 4:
                    pool[h].seth(-angle2)
                    pool[g].seth(-angle1)
                    pool[h].fd(5)
                    pool[g].fd(5)
        if x1 < -200 or x1 > 200:
            pool[g].seth(180 - angle1)
        elif y1 < -200 or y1 > 200:
            pool[g].seth(-angle1)
        pool[g].fd(2)



