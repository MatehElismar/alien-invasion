import pygame 
from consts import IMAGESDIR
from time import sleep
class Alien(pygame.sprite.Sprite):
   
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.speedY = 0.1
        self.speedX = 1
        self.screenRect = screen.get_rect()
        self.xDirection = 1
        self.yDirection = 1
        
         # Create an empty group of bullets
        self.bullets = pygame.sprite.Group()
        
        # Load the ship image and get its rect
        self.image = pygame.image.load(IMAGESDIR + '/alien.bmp')
        self.rect = self.image.get_rect() # Get the dimensions of the image. By default is drawn on the positio (0,0) of the screen


        self.rect.x = self.rect.width
        # Lo creamos por encima del top para que este escondido y luego venga bajando
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        
    def setX(self, value):
        self.x = value
        self.rect.x = self.x 
    def fire(self):
        bullet = Bullet(self)
        self.bullets.add(bullet)

    def changeDirectionX(self):
        self.xDirection = self.xDirection* -1

    def changeDirectionY(self):
        self.yDirection = self.xDirection* -1

    def checkBulletsCollision(self):
        pass

    def draw(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 
    
    def update(self):
        if self.rect.right >= self.screenRect.right or self.rect.left <= 0:
            self.changeDirectionX()
        if self.xDirection == 1:
           self.x += self.speedX
        else:
           self.x -=  self.speedX

        self.rect.x = self.x

        if self.y == self.screenRect.centery or self.y <= 0:
            self.changeDirectionY()
        if self.yDirection:
            self.y += self.speedY
        else:
            self.y -= self.speedY
        self.rect.y = self.y
 

    
        