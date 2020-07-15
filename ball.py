import pygame
from pygame.sprite import Sprite
import random
class Ball(Sprite):
    def __init__(self,bb,screen):
        super(Ball,self).__init__()
        self.image= pygame.image.load("images/ball.bmp")
        self.screen=screen
        self.bb=bb
        self.rect= self.image.get_rect()
        self.screen_rect= self.screen.get_rect()
        self.rect.y= self.rect.height - 50
        self.rect.x= random.randrange(self.rect.width,self.screen_rect.width-self.rect.width)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.rect.move_ip(0, self.bb.ball_speed)
    

