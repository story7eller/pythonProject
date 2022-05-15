import turtle

inp = open('input.txt', 'r')
print(inp)
A = []
A.extend(inp)
for i in range(len(A)):
    A[i] = int(A[i])

print(A)





def zero():
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(80)
    turtle.setheading(0)
    turtle.forward(40)
    turtle.setheading(270)
    turtle.forward(80)
    turtle.setheading(180)
    turtle.forward(40)
    turtle.setheading(0)
    turtle.forward(40)
    turtle.penup()
    space()
def space():
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(16)
    turtle.pendown()
def one():
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.setheading(45)
    turtle.forward((40**2+40**2)**0.5)
    turtle.setheading(270)
    turtle.forward(80)
    turtle.penup()
    space()
def action(z,o):
    turtle.setheading(z)
    turtle.forward(o)
def two():
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    action(90, 40)
    action(0, 40)
    action(270, 40)
    action(225, (40**2 + 40**2)**0.5)
    action(0, 40)
    space()
def three():
    turtle.setheading(90)
    turtle.forward(20)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    turtle.forward(20)
    action(0, 40)
    action(270, 40)
    action(180, 40)
    action(0, 40)
    action(270, 40)
    action(180 , 40)
    action(0, 40)
    space()
def four():

    turtle.penup()
    action(90, 40)
    turtle.pendown()
    action(90,40)
    action(270,40)
    action(0, 40)
    action(90, 40)
    action(270, 80)
    space()
def five():
    turtle.penup()
    action(90, 40)
    turtle.pendown()
    action(90, 40)
    action(0, 40)
    action(180, 40)
    action(270, 40)
    action(0, 40)
    action(270 , 40)
    action(180, 40)
    action(0, 40)
    space()
def six():

    action(90, 40)
    turtle.pendown()
    action(90, 40)
    action(0, 40)
    action(180, 40)
    action(270, 40)
    action(0, 40)
    action(270, 40)
    action(180, 40)
    action(0, 40)
    space()
def seven():
    turtle.penup()
    action(90, 70)
    turtle.pendown()
    action(90, 10)
    action(0, 40)
    action(248.5, (80**2 + 40**2)**0.5)
    turtle.penup()
    action(0, 40)
    space()

def eight():
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(80)
    turtle.setheading(0)
    turtle.forward(40)
    turtle.setheading(270)
    turtle.forward(40)
    action(180, 40)
    turtle.setheading(0)
    turtle.forward(40)
    action(270,40)
    action(180,40)
    turtle.penup()
    action(0,40)
    space()
def nine():
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.forward(40)
    turtle.setheading(0)
    turtle.forward(40)
    turtle.setheading(270)
    turtle.forward(40)
    action(180, 40)
    turtle.setheading(0)
    turtle.forward(40)
    action(270, 40)
    action(180, 40)
    turtle.penup()
    action(0, 40)
    space()


for elem in A:

    if elem == 0:
        zero()
    if elem == 1:
        one()
    if elem == 2:
        two()
    if elem == 3:
        three()
    if elem == 4:
        four()
    if elem == 5:
        five()
    if elem == 6:
        six()
    if elem == 7:
        seven()
    if elem == 8:
        eight()
    if elem == 9:
        nine()
turtle.shape('turtle')
turtle.color('blue')
turtle.speed(1)
turtle.exitonclick()