import sys, pygame
import settings, consts
from humanShip import humanShip
import gameFunctions as game
from alienShip import Alien

def initGame():
    """Initialize the game and create a screen object"""
    pygame.init() 
     # Create the principal surface of the game (The window).
    screen = pygame.display.set_mode(consts.SCREEN_DIMENSIONS)
    
    # Configure Screen General Surface
    settings.configureScreen(screen)

    # Create a ship Surface
    ship = humanShip(screen)

    aliens = pygame.sprite.Group()

    game.createAliens(screen, aliens)

    #Start the main loop for the game.
    while True:
        game.checkEvents(ship, aliens)
        ship.move()
        ship.bullets.update()
        aliens.update()
        print(len(aliens))
        # Redraw the screen during each pass through the loop. 
        game.redrawSurfaces(screen, aliens, ship)
        collisions = pygame.sprite.groupcollide(ship.bullets, aliens, True, True)
        #Make the most recently drawn screen visible.
        pygame.display.flip()

#Run the game and start the fun.
initGame()