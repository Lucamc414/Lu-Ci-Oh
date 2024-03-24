import pygame
import os
import importlib
from player import Player
import random
from cardDisplay import CardDisplay

# Set up some constants
WINDOW_WIDTH = 1700
WINDOW_HEIGHT = 900

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

def handle_card_hover(player, card_display, start_x, start_y):
    card_width = card_display.card_width
    card_height = card_display.card_height

    # Get the player's hand
    hand = player.hand

    # Get the current mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the mouse button is pressed
    mouse_pressed = pygame.mouse.get_pressed()[0]  # Left button

    # Check if the mouse is over a card
    for i, card in enumerate(hand):
        position = card_display.calculate_position(start_x, start_y, i)
        rect = pygame.Rect(*position, card_width, card_height)

        # If the mouse is over a card, display the card and check if it is clicked
        if rect.collidepoint(mouse_pos):
            image = card_display.load_and_scale_image(card.image2, 2)
            enlarged_position = WINDOW_WIDTH - card_width * 2 - 10, (WINDOW_HEIGHT - card_height * 2) // 2
            card_display.draw_card(image, enlarged_position)

            # If the card is clicked, summon it and remove it from the hand
            if mouse_pressed:
                if summon(card, player, card_display):
                    del hand[i]
                    card_display.showHand(hand, start_x, start_y)
                    image = card_display.load_and_scale_image(card.image1)
                    card_display.draw_card(image, enlarged_position)

            return True  # Return True if a card is being hovered over

    # Check if the mouse is over a card in the monster zone
    for i, card in enumerate(player.gameArea.mainMonsterZone):
        position = card_display.calculate_position(player.gameArea.monsterx, player.gameArea.monstery, i)
        rect = pygame.Rect(*position, card_width, card_height)

        # If the mouse is over a card, display the card
        if rect.collidepoint(mouse_pos):
            image = card_display.load_and_scale_image(card.image2, 2)
            enlarged_position = WINDOW_WIDTH - card_width * 2 - 10, (WINDOW_HEIGHT - card_height * 2) // 2
            card_display.draw_card(image, enlarged_position)
            return True

    # Check if the mouse is over a card in the spell zone
    for i, card in enumerate(player.gameArea.spellTrapZone):
        position = card_display.calculate_position(player.gameArea.spellx, player.gameArea.spelly, i)
        rect = pygame.Rect(*position, card_width, card_height)

        # If the mouse is over a card, display the card
        if rect.collidepoint(mouse_pos):
            image = card_display.load_and_scale_image(card.image2, 2)
            enlarged_position = WINDOW_WIDTH - card_width * 2 - 10, (WINDOW_HEIGHT - card_height * 2) // 2
            card_display.draw_card(image, enlarged_position)
            return True

    return False  # Return False if no card is being hovered over

def summon(card, player, card_display):
    success = False

    # Check the type of the card and add it to the appropriate zone if there is space
    if card.type == "Entity":
        if len(player.gameArea.mainMonsterZone) < 5:
            player.gameArea.mainMonsterZone.append(card)
            success = True
    elif card.type == "Magic" or card.type == "Trap":
        if len(player.gameArea.spellTrapZone) < 5:
            player.gameArea.spellTrapZone.append(card)
            success = True

    # Update the display
    reloadField(player, card_display)
    pygame.display.update()

    return success

def reloadField(player, card_display):
    # Draw all the cards in the monster zone
    for i, card in enumerate(player.gameArea.mainMonsterZone):
        image = card_display.load_and_scale_image(card.image1)
        position = card_display.calculate_position(player.gameArea.monsterx, player.gameArea.monstery, i)
        card_display.draw_card(image, position)

    # Draw all the cards in the spell zone
    for i, card in enumerate(player.gameArea.spellTrapZone):
        image = card_display.load_and_scale_image(card.image1)
        position = card_display.calculate_position(player.gameArea.spellx, player.gameArea.spelly, i)
        card_display.draw_card(image, position)