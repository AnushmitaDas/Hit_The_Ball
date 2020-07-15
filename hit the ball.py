import pygame,sys
from person import Person
from settings import Settings
import gameFunctions as gf
from ball import Ball
from pygame.sprite import Group
from play_button import Play_Button
from score import Score
def rungame():
    bb=Settings()
    pygame.init()
    screen=pygame.display.set_mode((bb.width,bb.height))
    ADDBALL= pygame.USEREVENT + 1
    pygame.time.set_timer(ADDBALL,2000)
    person=Person(screen)
    ball= Group()
    play_button= Play_Button(screen,bb)
    score= Score(screen,bb)
    while True:
        gf.check_events(bb,screen,person,ball,ADDBALL,play_button)   
        screen.fill(bb.bg_color)
        if bb.game_active==True:
            ball.draw(screen)
            gf.update_balls(ball,person,screen,bb,score)
            person.update() 
        else:
            play_button.draw_button()
            pygame.mouse.set_visible(True)
        score.draw_button()
        person.blitme()
        pygame.display.flip()

        
rungame()