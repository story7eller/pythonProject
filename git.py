import pygame
from pygame.draw import*
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.update()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()