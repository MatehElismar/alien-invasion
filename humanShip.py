import pygame
from consts import IMAGESDIR 
from bullet import Bullet
class humanShip():
    def __init__(self, screen):
        "Initalize the HumanShip class. Needs the screen rectangle"
        self.speed = 1.3
        self.enableMovingRight = False
        self.enableMovingLeft = False
        self.screen = screen
        self.screenRect = screen.get_rect()

         # Create an empty group of bullets
        self.bullets = pygame.sprite.Group()
        
        # Load the ship image and get its rect
        self.image = pygame.image.load(IMAGESDIR + '/ship.bmp')
        self.rect = self.image.get_rect() # Get the dimensions of the image. By default is drawn on the positio (0,0) of the screen
        
        # Define the position of the ship
        self.setRect() 


    def setRect(self):
        # Start each new ship at the bottom center of the screen (We adjust the position depending of the values of the screen rectangle)
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom -5


        # The properties of the Rectangles acept only integer values.
        # For currancy purpuses we need to acept decimal values to manage the speed of the objects and the game
        # So, we save the float value of the center to update the values through this variable; the original center is still acepting only integer values but it works because this
        #  Ej.
        # x = 1.5 => 1;
        #  x =+ 4 => 1;
        #  x+=4 => 2
        # Al usar una variable flotante para aumentar la velocidad y la entera para tomar el valor aveces seguira con el mismo valor aunque lo cambiemos [esto hace que el cambio de velocidad no se afecte en algunas vueltas del bucle]
        # Espero recordar esto.
        self.center = float(self.rect.centerx)


    def fire(self):
        bullet = Bullet(self)
        self.bullets.add(bullet)

    def checkBulletsCollision(self):
        pass

    def draw(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 
    
    def move(self):
        if self.enableMovingRight and self.rect.right < self.screenRect.right:
            self.center += self.speed;
        elif self.enableMovingLeft and self.rect.left > 0:
            self.center -= self.speed;

        # We change the position in respect of the speed and the direction of the movement
        self.rect.centerx = self.center


    
    