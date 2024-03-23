import pygame
import sys

def main_menu(window, WINDOW_WIDTH, WINDOW_HEIGHT):
    menu_font = pygame.font.Font(None, 50)
    option1 = menu_font.render("1. Start Game", True, (255, 255, 255))
    option2 = menu_font.render("2. Quit", True, (255, 255, 255))

    option1_rect = option1.get_rect()
    option1_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - option1.get_height() // 2 - 25)

    option2_rect = option2.get_rect()
    option2_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + option2.get_height() // 2 + 25)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if option1_rect.collidepoint(pygame.mouse.get_pos()):
                    window.fill((0, 0, 0))
                    pygame.display.update()
                    return "start_game"

                elif option2_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        window.fill((0, 0, 0))  # Fill the screen with black
        window.blit(option1, option1_rect.topleft)
        window.blit(option2, option2_rect.topleft)
        pygame.display.update()