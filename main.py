import os,sys
import pygame

# Import Custom Game Settings
from settings import Settings
from ship import Ship

class AlienInvasion():
    '''Overall Class To Manage Behaviour & Assets of Game'''

    def __init__(self):
        '''Initiating the game & creating game resource'''

        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)

    def run_game(self):
        '''Start the main loop for the game'''
        while True:

            #Lookg For Events
            self._check_events()
            
            # Making Sure Display's color is persistant
            self.screen.fill(self.settings.bg_color)

            # Calling To Create Ship Instance
            self.ship.blitme()

            # Diplay the refreshed screen to user continously
            pygame.display.flip()
    
    def _check_events(self):
        # Responds to key and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



if __name__ == '__main__':
    # Create a game instance for alien invasion & run it
    ai = AlienInvasion()
    ai.run_game()
