import pygame
from pygame.draw import*
import math
from random import randint
import pygame.gfxdraw

pygame.init()

FPS = 30
screen = pygame.display.set_mode((470, 600))
red = (255, 0, 0)
green = (23, 117, 69)
skyblue = (157, 230, 253)
grey = (192, 212, 192)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (205, 205, 0, 128)
space = (182, 182, 182)

def background():
    polygon(screen, green, [(0, 300), (0, 600), (470, 600), (470, 300)])
    polygon(screen, skyblue, [(0, 0), (0, 300), (470, 300), (470, 0)])


background()
location = [300, 300]
location = [250, 200]
def body(location , width, height , k):
    x1 = location[0]
    y1 = location[1]
    ellipse(screen, grey, [x1, y1, width * k, height * k])

    center = [x1 +width/2*k, y1 + height/ 2*k]
    x1, y1 = location[0], location[1] - 11*k
    ellipse(screen, grey, [x1, y1, width * k, height * k])
    return center

def change_pos(pos, newpos, k) -> int :

    pos[0] = pos[0] + newpos[0]*k
    pos[1] = pos[1] + newpos[1]*k

    return pos

def left_leg( pos, location , width, height, k):
    center = pos
    x, y = center[0], center[1]
    width = width *k
    height = height * k
    ellipse(screen, grey, [x, y, width , height ])
    center = [x + width / 2, y + height / 2]
    return center
def right_leg(pos, location, width, height, k):
    center = pos
    x, y = center[0], center[1]
    width = width * k
    height = height * k

    ellipse(screen, grey, [x, y, width , height ])
    center = [x + width / 2, y + height / 2]
    return center
k = 1

def left_hand(pos, location, width, height, k):
    center = pos
    x, y = center[0], center[1]
    width = width * k
    height = height * k

    ellipse(screen, grey, [x, y, width, height])
    center = [x + width / 2, y + height / 2]
    return center


def alien(location, k):
    pos = body(location, 30, 40, k)
    body(location, 30, 40, k)
    left_leg(pos, 200, 18, 30, k)
    pos = left_leg(pos, 200, 15, 30, k)
    x = pos[0] - 3*k
    y = pos[1]
    pos = [x, y]
    left_leg(pos, location, 13, 30, k)
    y = pos[1] + 15*k
    x = pos[0] + 1*k
    pos = [x, y]
    left_leg(pos, location, 12, 20, k)
    y = pos[1] + 10*k
    pos = [x, y]
    left_leg(pos, location, 11, 16, k)
    y = pos[1] + 5*k
    pos = [x, y]
    left_leg(pos, location, 24, 11, k)
    pos = location
    y = pos[1] + 20*k
    pos = [location[0], y]
    right_leg(pos, 200, 18, 30, k)
    x = pos[0] - 3*k
    y = pos[1]
    pos = [x, y]
    left_leg(pos, location, 13, 30, k)
    y = pos[1] + 15*k
    x = pos[0] + 1*k
    pos = [x, y]
    left_leg(pos, location, 12, 20, k)
    y = pos[1] + 10*k
    pos = [x, y]
    left_leg(pos, location, 11, 16, k)
    y = pos[1] + 10*k
    pos = [x, y]
    right_leg(pos, 200, 11, 16, k)
    y = pos[1] + 6*k
    x = pos[0] - 12*k
    pos = [x, y]
    right_leg(pos, 200, 24, 11, k)
    pos = [location[0] - 5*k, location[1] - 20*k]
    left_hand(pos, 200, 15, 15, k)
    pos =[location[0] - 7*k, location[1] -14*k]
    left_hand(pos, 200, 14, 14, k)
    x = pos[0]
    x = x - 3*k
    y = pos[1] +5 * k
    pos = [x, y]
    left_hand(pos, 200, 14, 14, k)
    pos = [x - 2*k, y + 10*k]
    left_hand(pos, 200, 13, 13, k)
    pos = [x - 2*k, y + 10 * k]
    left_hand(pos, 200, 12, 12, k)
    pos = [x - 3 * k, y + 15 * k]
    left_hand(pos, 200, 12, 12, k)
    pos = [x - 2 * k, y + 18 * k]
    left_hand(pos, 200, 12, 12, k)
    pos = [location[0] + 15 *k, location[1] -20*k]
    left_hand(pos, 200, 15, 15, k)
    pos[0]= pos[0] + 10*k
    pos[1] = pos[1] + 5*k
    left_hand(pos, 200, 16, 12, k)
    pos[0], pos[1] = pos[0]+11*k, pos[1]+5*k
    left_hand(pos, 200, 16, 12, k)
    pos[0], pos[1] = pos[0] + 9*k, pos[1] -4*k
    left_hand(pos, 200, 16, 12, k)
    change_pos(pos, [5, - 10], k) # яблоко
    ellipse(screen, red, [pos[0], pos[1], 18*k, 18*k ])
    w = 40
    h = 20
    rect(screen, grey, [x, y-35*k, w*k, h*k], 30, border_radius=15)
    rect(screen, grey, [x + w/3*k, y - h * k, w/2 * k, h/2 * k], 30, border_radius=15)
    circle(screen, black, [pos[0]-28*k, pos[1]-12*k], 5*k, 0)
    circle(screen, white, [pos[0]-28*k, pos[1]-12*k], 2*k, 0)
    circle(screen, black, [pos[0] - 48 * k, pos[1] - 12 * k], 5 * k, 0)
    circle(screen, white, [pos[0] - 48 * k, pos[1] - 12 * k], 2 * k, 0)
    ellipse(screen, grey, [pos[0] - 50*k, pos[1] - 48*k, 10*k, 30*k])
    ellipse(screen, grey, [pos[0] - 51 * k, pos[1] - 60 * k, 8*k, 20*k])
    ellipse(screen, grey, [pos[0] - 53 * k, pos[1] - 64 * k, 7*k, 18*k])
    circle(screen,grey, [pos[0] - 55*k, pos[1]-65*k],6*k, 0 )
    ellipse(screen, grey, [pos[0] - 35 *k, pos[1] - 48*k, 10*k, 30*k])
    ellipse(screen, grey, [pos[0] - 36 * k, pos[1] - 60 * k, 8*k, 20*k])
    ellipse(screen, grey, [pos[0] - 38 * k, pos[1] - 64 * k, 7*k, 18*k])
    circle(screen, grey, [pos[0] - 40*k, pos[1]-65*k],6*k, 0 )


location = [330, 410]
alien(location, 1.3)
location = [160, 430]
alien(location, 0.7)
location = [180, 350]
alien(location, 0.5)
location = [130, 330]
alien(location, 0.5)
location = [80, 350]
alien(location, 0.5)
screen.set_alpha(128)

pygame.gfxdraw.filled_polygon(screen, ((140, 250), (70, 340), (210, 340)), (255, 255, 0, 127))
def light(abc, size):
    x = abc[0]
    y = abc[1]
    x1 = x - size/2
    y1 = y + size
    x2 = x + size/2
    y2 = y1
    x2 = x + size /2
    pygame.gfxdraw.filled_polygon(screen, [(x, y), (x1, y1), (x2, y2)], (255, 255, 0, 128))

abc = [250, 250]
light(abc, 60)
abc = [400, 222]
light(abc, 90)

def spaceship(skypos, size,n):

    ellipse(screen, space, [skypos[0], skypos[1], size*n, size*n/2])
    K = n
    n = n * 0.8

    ellipse(screen, white, [skypos[0] + size/8*n, skypos[1] - size/16*n, size*n, size*n/2])
    ellipse(screen, white, [skypos[0] + size/16*n, skypos[1] + size/4*n, size*n/8, size*n/16])
    ellipse(screen, white, [skypos[0] + size / 5 * n, skypos[1] + size / 3.0*k, size * n / 8, size * n / 16])
    ellipse(screen, white, [skypos[0] + size / 2.5 * n, skypos[1] + size / 2.6*k ,size * n / 8, size * n / 16])
    ellipse(screen, white, [skypos[0] + size / 1.6 * n, skypos[1] + size / 2.5 *k,size * n / 8, size * n / 16])
    ellipse(screen, white, [skypos[0] + size / 1.2 * n, skypos[1] + size / 2.7 ,size * n / 8, size * n / 16])
    ellipse(screen, white, [skypos[0] + size / 1.0 * n, skypos[1] + size / 3.2 ,size * n / 8, size * n / 16])
    ellipse(screen, white, [skypos[0] + size*1.11 * n, skypos[1] + size / 4.35 ,size * n / 8, size * n / 16])
skypos = [210, 210]
spaceship(skypos, 80, 1)
skypos = [80, 200]
spaceship(skypos,120, 1)
skypos = ( 352, 200)
spaceship(skypos, 100, 1)




pygame.display.update()
clock = pygame.time.Clock()
finished = False



while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
