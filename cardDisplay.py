import pygame

class CardDisplay:
    def __init__(self, window, card_width, card_height, margin):
        self.window = window
        self.card_width = card_width
        self.card_height = card_height
        self.margin = margin

    def load_and_scale_image(self, image_path, scale=1):
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, (self.card_width*scale, self.card_height*scale))

    def calculate_position(self, start_x, start_y, index):
        x = start_x + index * (self.card_width + self.margin)
        y = start_y
        return x, y

    def draw_card(self, image, position):
        self.window.blit(image, position)

        
    def showHand(self, hand, start_x, start_y):
        for i, card in enumerate(hand):
            image = self.load_and_scale_image(card.image1)
            position = self.calculate_position(start_x, start_y, i)
            self.draw_card(image, position)

