import pygame
from pygame.draw import*
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
grey = (230, 230, 230)
polygon(screen, grey, [(0, 0), (0, 600), (600, 600), (600, 0)])
yellow = (255, 255, 0)

center = (300, 300)

left_eye = (250, 275)
red = (255, 0, 0)
black = (0, 0, 0)
circle(screen, yellow, center, 110) # желтый круг в центре
circle(screen, red, left_eye, 20) # красный глаз
circle(screen, black, left_eye, 20, width=2) #ободок черный левого глаза
circle(screen, black, left_eye, 8) # зрачек левого глаза
right_eye = (350, 275)
circle(screen, red, right_eye, 17) # красный глаз правый
circle(screen, black, right_eye, 17, width=2)# ободок правого глаза
circle(screen, black, right_eye, 8) # зрачек правого глаза
circle(screen, black, center, 110, width=1)
#260,257

def eye_brows(x,y,c,v,h,z):
    # координаты потом длинна половинок и потом высота потом угол
    x1, y1 = x, y
    b = c*math.cos(z*math.pi/180)
    x2 = x - b
    a = c*math.sin(z*math.pi/180)
    y2 = y - a
    b2 = h*math.cos(z*math.pi/180)
    x3 = x2 + b2
    a2 = h*math.sin(z*math.pi/180)
    y3 = y2 - a2
    x4 = x + b2
    y4 = y - a2
    polygon(screen, black, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)])
    x5, y5 = x, y
    b3 = v*math.cos(z*math.pi/180)
    x6 = x + b3
    a3 = v*math.sin(z*math.pi/180)
    y6 = y + a3
    b4 = h*math.cos(z*math.pi/180)
    x7 = x6 + b4
    a4 = h*math.sin(z*math.pi/180)
    y7 = y6 - a4
    x8 = x + b4
    y8 = y - a4
    polygon(screen, black, [(x5, y5), (x6, y6), (x7, y7), (x8, y8)])

#
eye_brows(260, 257, 80, 30, 15, 20)
eye_brows(341, 251, 30, 55, 15, -20)
eye_brows(255, 357, 10, 100, 30, 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()        

