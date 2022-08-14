import os,sys
import pygame

# Import Custom Game Settings
from settings import Settings
from ship import Ship
from bullet import Bullet
from pygame.sprite import Sprite
#from girl import Girl

class AlienInvasion():
    '''Overall Class To Manage Behaviour & Assets of Game'''

    def __init__(self):
        '''Initiating the game & creating game resource'''

        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        #self.girl = Girl(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        '''Start the main loop for the game'''
        while True:

            #Look For Events
            self._check_events()
            #Update Movement Of Ship
            self.ship.update()
            # Update Bullet's
            self._update_bullets()
            #Update Screen
            self._update_screen()

    
    def _check_events(self):
        # Responds to key and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        # Making Sure Display's color is persistant
        self.screen.fill(self.settings.bg_color)

        # Calling To Create Ship/Girl Instance
        self.ship.blitme()

        #self.girl.blitme()

        # Updating the Fired bullets onto the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


        # Diplay the refreshed screen to user continously
        pygame.display.flip()
    
    def _update_bullets(self):
        ''' This manages the bullet's and removal of old bullets '''
        self.bullets.update()
            # Remove bullets Which reach the top
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    
    def _check_keyup_events(self,event):
        '''Responds back to keyup events'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _check_keydown_events(self,event):
        '''Responds back to Keydown events'''
        if event.key == pygame.K_RIGHT:
            # Move the Ship to the Right in the x axis
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #Move the ship to the Left in the x-axis
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # Fire the bullet
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _fire_bullet(self):
        '''Creating an Instance for the bullet'''
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            #Add Each bullet to the group spirtes for us to keep a track of bullets on screen
            self.bullets.add(new_bullet)






if __name__ == '__main__':
    # Create a game instance for alien invasion & run it
    ai = AlienInvasion()
    ai.run_game()
