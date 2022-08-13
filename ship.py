import pygame

class Ship():
    '''Overall class for the object Ship'''

    def __init__(self, ai_game):
        '''Initiating the ship element & Position on screen'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship and get rect element of it
        self.image = pygame.image.load('images/ship.bmp')
        #self.image = pygame.transform.scale(self.image, (100,78))

        self.rect = self.image.get_rect()

        #Position the Ship at bottom of Screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        #Going to Draw the Ship To Screen
        self.screen.blit(self.image, self.rect)