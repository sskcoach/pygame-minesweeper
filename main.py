import pygame
import sys
from const import *
from board import Board


def main():
    pygame.init()

    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps = pygame.time.Clock()

    board = Board(9, 9)

    running = True
    game_is_over = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                game_is_over = board.on_click(event.pos, event.button)
                if game_is_over:
                    board.open_all_mines()

        surface.fill(BLACK)

        board.draw(surface)

        if game_is_over:
            draw_game_over(surface)

        pygame.display.flip()

        fps.tick(FPS)

    pygame.quit()
    sys.exit()


def draw_game_over(surface):
    font = pygame.font.Font(None, 46)
    text = font.render("Game Over", True, RED, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    surface.blit(text, text_rect)


if __name__ == "__main__":
    main()
