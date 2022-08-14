import pygame

class Ship():
    '''Overall class for the object Ship'''

    def __init__(self, ai_game):
        '''Initiating the ship element & Position on screen'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        #Load the ship and get rect element of it
        self.image = pygame.image.load('images/ship.bmp')
        #self.image = pygame.transform.scale(self.image, (100,78))

        self.rect = self.image.get_rect()

        #Position the Ship at bottom of Screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement Flags
        self.moving_right = False
        self.moving_left = False

        # Add a decimal value for ship's Horizontal postion
        self.x = float(self.rect.x)
    
    def update(self):
        '''Updates the position of the ship relative to last position'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update Rect Position from self.x
        self.rect.x = self.x

    def blitme(self):
        #Going to Draw the Ship To Screen
        self.screen.blit(self.image, self.rect)
