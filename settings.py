import pygame
class Settings():
    def __init__(self):
        self.width=900
        self.height=600
        self.bg_color=(255,255,255)
        self.lives=3
        self.ball_increase_speed= 0.5
        self.score=0
        self.highscore=0
        self.increase_count=2
        self.game_active=False
        

    def reset(self):
        self.lives=3
        self.count= 0
        self.ball_speed= 1
        self.max_count=3
        pygame.mouse.set_visible(False)
        self.score=0