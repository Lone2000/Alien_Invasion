import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    ''' Overall Bullet Class  '''

    def __init__(self,ai_game):
        ''' Intilizes all the charactertics of bullet and behaviour '''
        super().__init__()

        self.settings = ai_game.settings
        self.screen =  ai_game.screen
        self.color = self.settings.bullet_color

        # Create Bullet rect at (0,0) & Correct the position 
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullet's Position as a float
        self.y = float(self.rect.y)

    def update(self):
        '''Handles the movement and updated positon of Bullet'''
        self.speed = self.settings.bullet_speed
        #Movement of Bullet from Ship -> In vertical axis
        self.y -= self.speed   
        #Update the Bullet rect positon
        self.rect.y = self.y 

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
