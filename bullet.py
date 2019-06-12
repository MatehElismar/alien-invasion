import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite):
    def __init__(self, ship):
        super().__init__() 
        self.ship = ship 
        self.speed = 1
        self.rect = pygame.Rect(0, 0, 3, 15)
        self.color = (0,0,0)
        self.bulletDirection = {
            "right": False,
            "left": False,
            "top": True,
            "bottom": False 
        }
        

        # Define the pos
        self.setRect()


    def setRect(self):
        # Start each new ship at the bottom center of the screen (We adjust the position depending of the values of the screen rectangle)
        self.rect.width = 3
        self.rect.height = 15
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top


        # The properties of the Rectangles acept only integer values.
        # For currancy purpuses we need to acept decimal values to manage the speed of the objects and the game
        # So, we save the float value of the center to update the values through this variable; the original center is still acepting only integer values but it works because this
        #  Ej.
        # x = 1.5 => 1;
        #  x =+ 4 => 1;
        #  x+=4 => 2
        # Al usar una variable flotante para aumentar la velocidad y la entera para tomar el valor aveces seguira con el mismo valor aunque lo cambiemos [esto hace que el cambio de velocidad no se afecte en algunas vueltas del bucle]
        # Espero recordar esto.
        self.y = float(self.rect.top)

    def update(self):
        if self.bulletDirection["top"]:
            self.y -= self.speed
            self.rect.top = self.y

    def draw(self):
        pygame.draw.rect(self.ship.screen, self.color, self.rect)
