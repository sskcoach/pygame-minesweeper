import pygame
import sys
from const import *


def main():
    pygame.init()

    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps = pygame.time.Clock()

    FIELD_MINE = "M"

    mine_field = [
        [None, None, None, None, None, None, None, None, None, ],
        [None, None, None, None, None, None, None, None, None, ],
        [None, FIELD_MINE, None, None, FIELD_MINE, None, None, None, None, ],
        [None, None, None, None, None, None, None, None, None, ],
        [None, None, None, None, None, None, None, None, None, ],
        [None, None, None, FIELD_MINE, None, None, None, None, None, ],
        [None, None, None, None, None, None, FIELD_MINE, None, None, ],
        [None, FIELD_MINE, None, None, None, None, None, None, None, ],
        [None, None, None, None, None, None, None, None, None, ],
    ]

    print(mine_field)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill(BLACK)

        size = int(SCREEN_HEIGHT / 9)
        start_x = SCREEN_WIDTH / 2 - (size * 9) / 2
        start_y = SCREEN_HEIGHT / 2 - (size * 9) / 2

        for y in range(9):
            for x in range(9):
                rect = (start_x + x * size, start_y + y * size, size + 1, size + 1)
                pygame.draw.rect(surface, WHITE, rect, 1)
                value = mine_field[y][x]
                if value == FIELD_MINE:
                    pygame.draw.rect(surface, WHITE, rect, 10)

        pygame.display.flip()

        fps.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
