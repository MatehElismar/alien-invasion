import pygame, consts

def configureScreen(screen): 

    # Set the Tittle of the window.
    pygame.display.set_caption(consts.TITLE)

    # Set Background color
    screen.fill(consts.MAIN_COLOR)
 
    return screen