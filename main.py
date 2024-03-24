# main.py
import pygame
import sys
from menu import main_menu
import game
from cardDisplay import CardDisplay  # Import the CardDisplay class

# Initialize Pygame
pygame.init()

# Set up some constants
WINDOW_WIDTH = 1700
WINDOW_HEIGHT = 900

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
    card_width = 150
    card_height = 195
    margin = 10  # Space between cards
    start_x = 120
    start_y = WINDOW_HEIGHT - card_height - margin  # Bottom of the screen

    # Create a CardDisplay instance
    card_display = CardDisplay(window, card_width, card_height, margin)

    # Use the CardDisplay instance to show the hand
    card_display.showHand(player1.hand, start_x, start_y)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the previous frame
        window.fill((0, 0, 0))  # Fill with black color

        # Use the CardDisplay instance to reload the field
        game.reloadField(player1, card_display)

        # Use the CardDisplay instance to redraw the smaller cards
        card_display.showHand(player1.hand, start_x, start_y)

        # Use the CardDisplay instance to handle card hover
        hovering = game.handle_card_hover(player1, card_display, start_x, start_y)

        pygame.display.flip()  # Update the display

pygame.quit()