import pygame
import sys

def main():
    pygame.init()

    surface = pygame.display.set_mode((320, 240))

    fps = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill((0, 0, 0))

        size = 26
        start_x = 320 / 2 - (size * 9) / 2
        start_y = 240 / 2 - (size * 9) / 2
        COLOR_WHITE = (255, 255, 255)

        for y in range(9):
            for x in range(9):
                rect = (start_x + x * size, start_y + y * size, size + 1, size + 1)
                pygame.draw.rect(surface, COLOR_WHITE, rect, 1)

        pygame.display.flip()

        fps.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()