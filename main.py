# main.py
import pygame
import sys
from menu import main_menu
import game

# Initialize Pygame
pygame.init()

# Set up some constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Lu-Ci-Oh')

# Show the main menu
choice = main_menu(window, WINDOW_WIDTH, WINDOW_HEIGHT)

if choice == "start_game":

    turn = 0

    # deal cards and set up environment
    player1, player2 = game.start_game()
    print(player1.deck)
    print(player2.deck)

    # Display player 1's hand
    card_width = 100
    card_height = 130
    margin = 10  # Space between cards
    start_x = 120
    start_y = WINDOW_HEIGHT - card_height - margin  # Bottom of the screen
    game.showHand(window, player1.hand, start_x, start_y, card_width, card_height, margin)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

       # Clear the previous frame
        window.fill((0, 0, 0))  # Fill with black color

        # Reload the field
        game.reloadField(player1, card_width, card_height, window)

        # Redraw the smaller cards
        game.showHand(window, player1.hand, start_x, start_y, card_width, card_height, margin)

        # Handle card hover
        hovering = game.handle_card_hover(window, player1, start_x, start_y, card_width, card_height, margin)

        pygame.display.flip()  # Update the display
                

pygame.quit()
