import sys, pygame
import consts
from alienShip import Alien
 
from consts import MAIN_COLOR

def keyDownEvents(event, ship, aliens):
    # Enable Ship Movement 
    if event.key == pygame.K_LEFT:
        ship.enableMovingLeft = True
        ship.enableMovingRight = False
    elif event.key == pygame.K_RIGHT:
        ship.enableMovingRight = True
        ship.enableMovingLeft = False
    elif event.key == pygame.K_SPACE:
        ship.fire()
    elif event.key == pygame.K_TAB:
        createAliens(ship.screen, aliens)


def keyUpEvents(event, ship):
    # Disable Ship Movement
    if event.key == pygame.K_RIGHT:
        ship.enableMovingRight = False
    elif event.key == pygame.K_LEFT:
        ship.enableMovingLeft = False

def checkEvents(ship, aliens):
    """Watch for events"""
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pass
            sys.exit()
        elif event.type == pygame.KEYDOWN: 
            keyDownEvents(event, ship, aliens)
        elif event.type == pygame.KEYUP: 
            keyUpEvents(event, ship)
        


def redrawSurfaces(screen, aliens, *surfaces):
    """Redraw the screen during each pass through the loop."""
    
    # Redraw the main surface of the game each time this function is called.
    screen.fill(MAIN_COLOR)

    for alien in aliens:
        alien.draw()
        if alien.bullets:
            for bullet in alien.bullets.sprites():
                bullet.draw()

    for surface in surfaces: 
        surface.draw()
        if surface.bullets:
            for bullet in surface.bullets.sprites():
                bullet.draw()


def createAliens(screen, aliens):
    alien = Alien(screen)
    XavailableSpace = consts.SCREEN_DIMENSIONS[0] - (2 * alien.rect.width)#ancho de la pantalla
    XalienNumber = int(XavailableSpace / ( 2 * alien.rect.width))

    for n in range(XalienNumber):
        alien = Alien(screen)
        alien.setX(alien.rect.width + 2 * alien.rect.width * n)
        aliens.add(alien)

 