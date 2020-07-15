import pygame,sys
from ball import Ball
def check_events(bb,screen,person,ball,ADDBALL,play_button):
    for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()
            elif event.type== pygame.KEYDOWN:
                check_keydown(event,bb,screen,person)
            elif event.type== pygame.KEYUP:
                check_keyup(event,bb,screen,person)
            elif event.type == ADDBALL and bb.game_active==True:
                new_ball = Ball(bb,screen)
                ball.add(new_ball)
                if bb.count<bb.max_count:
                    bb.count+=1
                else:
                    bb.count=0
                    bb.max_count*=bb.increase_count
                    bb.ball_speed+=bb.ball_increase_speed
            elif event.type== pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y= pygame.mouse.get_pos()
                check_play_button(bb,play_button,mouse_x,mouse_y,ball,person,screen)
    
def check_keydown(event,bb,screen,person):
    if event.key== pygame.K_RIGHT:
        person.moving_right=True
    elif event.key== pygame.K_LEFT:
        person.moving_left=True

def check_keyup(event,bb,screen,person):
    if event.key== pygame.K_RIGHT:
        person.moving_right=False
    elif event.key== pygame.K_LEFT:
        person.moving_left=False

def update_balls(ball,person,screen,bb,score):
    screen_rect= screen.get_rect()
    for b in ball.sprites():
        if b.rect.bottom >= screen_rect.bottom and bb.lives>0:
            b.kill()
            bb.lives=bb.lives-1
            score.prep_person()
        elif bb.lives<=0:
            bb.game_active=False
    if pygame.sprite.spritecollideany(person,ball):
        bb.score+=1
        score.prep_score("Score- "+str(bb.score))
        if bb.score>bb.highscore:
            bb.highscore=bb.score
        score.prep_highscore("High Score- "+str(bb.highscore))
        ball.remove(ball)
    ball.update()
    
def check_play_button(bb,play_botton,mouse_x,mouse_y,ball,person,screen):
    if play_botton.rect.collidepoint(mouse_x,mouse_y) and bb.game_active==False:
        bb.game_active=True
        bb.reset()
        ball.empty()
        person.center_person()
