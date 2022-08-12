import os,sys
import pygame

# Import Custom Game Settings
from settings import Settings

class AlienInvasion():
    '''Overall Class To Manage Behaviour & Assets of Game'''

    def __init__(self):
        '''Initiating the game & creating game resource'''

        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        '''Start the main loop for the game'''
        while True:
            # Look for key and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Making Sure Display's color is persistant
            self.screen.fill(self.settings.bg_color)

            # Diplay the refreshed screen to user continously
            pygame.display.flip()

if __name__ == '__main__':
    # Create a game instance for alien invasion & run it
    ai = AlienInvasion()
    ai.run_game()
