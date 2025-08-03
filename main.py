import pygame
import sys
from const import *
from board import Board


def main():
    pygame.init()

    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps = pygame.time.Clock()

    running = True

    max_mine_count = 10
    board = Board(9, 9, max_mine_count)
    game_is_over = False
    game_is_clear = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if game_is_over or game_is_clear:
                    board = Board(9, 9, max_mine_count)
                    game_is_over = False
                    game_is_clear = False

                    continue
                shift = pygame.key.get_mods() & pygame.KMOD_SHIFT
                game_is_over = board.on_click(event.pos, event.button, shift)
                if game_is_over:
                    board.open_all_mines()
                else:
                    game_is_clear = board.is_clear()

        surface.fill(BLACK)

        board.draw(surface)

        if game_is_over:
            draw_game_over(surface)
        if game_is_clear:
            draw_game_clear(surface)

        pygame.display.flip()

        fps.tick(FPS)

    pygame.quit()
    sys.exit()


def draw_game_over(surface):
    font = pygame.font.Font(None, 46)
    text = font.render("Game Over", True, RED, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    surface.blit(text, text_rect)

    font = pygame.font.Font(None, 25)
    text = font.render("Tap anywhere to restart.", True, BLUE, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    surface.blit(text, text_rect)


def draw_game_clear(surface):
    font = pygame.font.Font(None, 46)
    text = font.render("Game Clear!!!", True, BLUE, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    surface.blit(text, text_rect)

    font = pygame.font.Font(None, 25)
    text = font.render("Tap anywhere to restart.", True, BLUE, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    surface.blit(text, text_rect)


if __name__ == "__main__":
    main()
