import pygame
import sys

pygame.init()

surface = pygame.display.set_mode((320, 240))

fps = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.fill((0, 0, 0))

    pygame.display.flip()

    fps.tick(60)

pygame.quit()
sys.exit()
