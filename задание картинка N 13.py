import pygame
from pygame.draw import*
import math
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((470, 600))
green = (21, 68, 6)
brown = (87, 71, 30)
yellow = (131, 86, 62)
polygon(screen, green, [(0, 0), (0, 600), (600, 600), (600, 0)])
polygon(screen, brown, [(0, 380), (0, 600), (600, 600), (600, 380)])


def tree(x, y, width):

    x1 = x
    y1 = y
    x4 = x + width
    y2 = 0
    y3 = 0
    x3 = x4
    y4 = y
    x2 = x1
    polygon(screen, yellow, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)])

hedgehogs = (255, 223, 196)


def hedgehog(x, y, width, hight):
    x1 = x
    y1 = y
    x2 = x
    y2 = y + hight
    x3 = x + width
    y3 = y2
    x4 = x3
    y4 = y

    ellipse(screen, hedgehog, b)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
def Ship(x, y, hight, wight):
    x1 = x
    y1 = y

    angle = randint(-30, 30)
    anglerad = math.radians(angle)
    h3 = wight * math.sin(anglerad)
    w3 = wight *math.cos(anglerad)
    x3 = x + w3
    y3 = y - h3
    len1= ((wight/2)**2 + hight**2)**0.5
    kosa = (len1**2 + (wight/2)**2 - hight**2)/ (2*len1*hight)
    kosb = math.cos(0) - math.cos(anglerad) - kosa
    len2 = len1*kosb
    x2 = x1 + len2
    h2 = (len1**2 - len2**2)**0.5
    y2 = y - h2
    polygon(screen, black, [(x2, y2), (x3, y3), (x1, y1)])

apple = (79, 168, 61)

ellipse(screen, hedgehogs, [384, 525, 13, 10])
ellipse(screen, hedgehogs, [370, 535, 16, 12])
ellipse(screen, hedgehogs, [244, 525, 14, 11])
ellipse(screen, hedgehogs, [255, 535, 16, 12])
ellipse(screen, hedgehogs, [245, 470, 150, 80])
ellipse(screen, white, [245, 470, 150, 80], width=1)
circle(screen, apple, [315, 495], 18)
for i in range(40):
    x = randint(245, 375)
    y = randint(470, 530)
    Ship(x, y, 65, 15)
ellipse(screen, hedgehogs, [370, 500, 40, 26])
ellipse(screen, white, [370, 500, 40, 26], width=1)

ellipse(screen, white, [265, 478, 8, 20]) # грибочек
ellipse(screen, red, [259, 468, 21, 17]) # шляпка грибочка
A2 = 245
A1 = 245 + 150
B1 = 470 + 80
B2 = 470
centerx = A2 + 75
centery = B2 + 40
c = (75**2 - 40**2)**0.5
print(c)
a = 75
F1 = (centerx - c, centery)
F2 = (centerx + c, centery)
existent = c/a
b = (a**2 - c**2)**0.5


# c расстояние от центра до фокуса
# 2а расстояние от произвольной точки элипса до фокусов








def eyes(x, y, distance, size):
    radius = size
    circle(screen, black, (x, y), radius)
    y2 = y - distance * math.sin(60*math.pi/180)
    x2 = x + distance * math.cos(60*math.pi/180)
    circle(screen, black, (x2, y2), radius)
eyes(390,513, 8, 2)

tree(0, 420, 44)
tree(66, 580, 101)
tree(317, 420, 42)
tree(426, 455, 32)
pygame.display.update()
clock = pygame.time.Clock()
finished = False



while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

