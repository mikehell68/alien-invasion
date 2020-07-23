import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """ Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen

        # Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_game.settings.bullet_width, ai_game.settings.bullet_height)
        self.rect.centerx = ai_game.ship.rect.centerx
        self.rect.top = ai_game.ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_game.settings.bullet_color
        self.speed_factor = ai_game.settings.bullet_speed_factor
    
    def update(self):
        """ move the bullet up the screen """
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw the bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)

class HBullet(Sprite):
    """ A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """ Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen

        # Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_game.settings.hbullet_width, ai_game.settings.hbullet_height)
        self.rect.centery = ai_game.ship.rect.centery
        self.rect.right = ai_game.ship.rect.right

        # Store the bullet's position as a decimal value
        self.x = float(self.rect.x)

        self.color = ai_game.settings.bullet_color
        self.speed_factor = ai_game.settings.bullet_speed_factor
    
    def update(self):
        """ moves the bullet up the screen """
        # Update the decimal position of the bullet
        self.x += self.speed_factor
        # Update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        # Draw the bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
        