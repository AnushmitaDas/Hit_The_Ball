import pygame

class Play_Button():
    def __init__(self,screen,bb):
        self.width,self.height=200,50
        self.screen=screen
        self.screen_rect= self.screen.get_rect()
        
        self.button_color=(255,105,180)
        self.text_color=(255,255,255)
        self.text_font= pygame.font.SysFont(None,48)
        self.rect= pygame.Rect(0,0,self.width,self.height)
        self.rect.center= self.screen_rect.center

        self.prep("PLAY")

    def prep(self,msg):
        self.msg_img= self.text_font.render(msg,True,self.text_color,self.button_color)
        self.msg_img_rect= self.msg_img.get_rect()
        self.msg_img_rect.center= self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_img,self.msg_img_rect)
