from random import randint
import turtle

number_of_turtles = 25
steps_of_time_number = 100
V = 800*800
turtle_space = (V / 25)**0.5
print(turtle_space)

pool = [turtle.Turtle('circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-400, 400), randint(-400, 400))

for i in range(steps_of_time_number):
    for unit in pool:
        unit.setheading(randint(0, 360))
        unit.forward(3)