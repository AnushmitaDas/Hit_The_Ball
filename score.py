import pygame
from pygame.sprite import Group
from person import Person
class Score():
    def __init__(self,screen,bb):
        self.width,self.height=200,50
        self.screen=screen
        self.screen_rect= self.screen.get_rect()
        self.bb=bb
        
        self.button_color=(255,255,255)
        self.text_color=(255,105,180)
        self.text_font= pygame.font.SysFont(None,48)
        self.prep_score("Score- "+str(bb.score))
        self.prep_highscore("High Score- "+str(bb.highscore))
        self.prep_person()
        

    def prep_score(self,msg):
        self.score_rect= pygame.Rect(0,0,self.width,self.height)
        self.score_rect.right= self.screen_rect.right -20
        self.score_rect.top= self.screen_rect.top + 20
        self.score_img= self.text_font.render(msg,True,self.text_color,self.button_color)
        self.score_img_rect= self.score_img.get_rect()
        self.score_img_rect.center= self.score_rect.center

    def draw_button(self):
        self.screen.blit(self.score_img,self.score_img_rect)
        self.screen.blit(self.highscore_img,self.highscore_img_rect)
        self.persons.draw(self.screen)

    def prep_highscore(self,msg):
        self.highscore_rect= pygame.Rect(0,0,self.width,self.height)
        self.highscore_rect.right= self.screen_rect.centerx
        self.highscore_rect.top= self.screen_rect.top +5
        self.highscore_img= self.text_font.render(msg,True,self.text_color,self.button_color)
        self.highscore_img_rect= self.highscore_img.get_rect()
        self.highscore_img_rect.center= self.highscore_rect.center

    def prep_person(self):
        self.persons= Group()
        for person_no in range(self.bb.lives):
            person= Person(self.screen)
            person.rect.x= 10+ person_no * person.rect.width 
            person.rect.y= 10
            self.persons.add(person)

