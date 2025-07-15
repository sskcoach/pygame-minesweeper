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

    # size: 26

    start_x = 320 / 2 - (26 * 9) / 2
    start_y = 240 / 2 - (26 * 9) / 2

    for y in range(9):
        for x in range(9):
            pygame.draw.rect(surface, (255, 255, 255),
                             (start_x + x * 26, start_y + y * 26, 27, 27), 1)

    pygame.display.flip()

    fps.tick(60)

pygame.quit()
sys.exit()
