import pygame
import os
import importlib
from player import Player
import random

# Set up some constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def start_game():
    
  # Get a list of all the Python files in the cards directory
    card_files = [f for f in os.listdir("cards") if f.endswith('.py')]

    # Import all the card classes
    cards = []
    for file in card_files:
        module_name = file[:-3]  # Remove the .py extension
        module = importlib.import_module('cards.' + module_name)
        card_class = getattr(module, module_name)
        cards.append(card_class)

    # Create the players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Create the players' decks
    player1.deck = [random.choice(cards)() for _ in range(10)]
    player2.deck = [random.choice(cards)() for _ in range(10)]

    # Each player draws 5 cards
    player1.hand = [player1.deck.pop() for _ in range(5)]
    player2.hand = [player2.deck.pop() for _ in range(5)]

    return player1, player2


def showHand(window, hand, start_x, start_y, card_width, card_height, margin):
    for i, card in enumerate(hand):
        # Load the card image
        image = pygame.image.load(card.image1)
        scaled_image = pygame.transform.scale(image, (card_width, card_height))

        # Calculate the position of the card
        x = start_x + i * (card_width + margin)
        y = start_y

        # Draw the card on the screen
        window.blit(scaled_image, (x, y))



def handle_card_hover(window, hand, start_x, start_y, card_width, card_height, margin):
    # Get the current mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the mouse button is pressed
    mouse_pressed = pygame.mouse.get_pressed()[0]  # Left button

    # Check if the mouse is over a card
    for i, card in enumerate(hand):
        # Calculate the position and size of the card
        x = start_x + i * (card_width + margin)
        y = start_y
        rect = pygame.Rect(x, y, card_width, card_height)

        if rect.collidepoint(mouse_pos):
            # Load the card image
            image = pygame.image.load(card.image2)
            scaled_image = pygame.transform.scale(image, (card_width * 2, card_height * 2))  # Double size

            # Calculate the position of the enlarged card
            x = (WINDOW_WIDTH - card_width * 2) // 2  # Center of the screen
            y = (WINDOW_HEIGHT - card_height * 2) // 2

            # Draw the enlarged card on the screen
            window.blit(scaled_image, (x, y))

            if mouse_pressed:
                # Remove the card from the hand
                del hand[i]

                # Redraw the hand
                showHand(window, hand, start_x, start_y, card_width, card_height, margin)

                # Load the card image
                image = pygame.image.load(card.image1)
                scaled_image = pygame.transform.scale(image, (card_width * 2, card_height * 2))  # Double size

                # Calculate the position of the enlarged card
                x = (WINDOW_WIDTH - card_width * 2) // 2  # Center of the screen
                y = (WINDOW_HEIGHT - card_height * 2) // 2

                # Draw the summoned card on the screen
                window.blit(scaled_image, (x, y))

            return True  # Return True if a card is being hovered over

    return False  # Return False if no card is being hovered over