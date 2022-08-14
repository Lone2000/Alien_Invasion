import pygame

class Girl():
    '''Overall Class of the Girl'''

    def __init__(self,ai_game):
        '''Intilize the girl element and screen position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load up image of Girl + Position
        self.image = pygame.image.load('images/Kristina.bmp')
        self.rect = self.image.get_rect()

        #Position relative to Screen
        self.rect.center = self.screen_rect.center
        

    def blitme(self):
        #Drawing the instance to the screen
        self.screen.blit(self.image,self.rect)
    

        
