import pygame
from pygame.sprite import Sprite
class Person(Sprite):
    def __init__(self,screen):
        super(Person,self).__init__()
        self.image= pygame.image.load("images/boy.bmp")
        self.rect= self.image.get_rect()
        self.screen= screen
        self.screen_rect= self.screen.get_rect()
        self.rect.centerx= self.screen_rect.centerx
        self.rect.bottom= self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False
        self.x= float(self.screen_rect.centerx)

    def blitme(self):
        self.rect.centerx=self.x
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right==True and self.rect.right<self.screen_rect.right:
            self.x=self.x+1.5
        if self.moving_left==True and self.rect.left>self.screen_rect.left:
            self.x=self.x-1.5

        self.rect.centerx=self.x

    def center_person(self):
        self.x= self.screen_rect.centerx


