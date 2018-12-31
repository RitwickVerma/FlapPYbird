import pygame
from src.config import config

class Goal():
    def __init__(self,display,player):
        self.display=display

        self.game_width=config['game']['width']
        self.game_floor=config['game']['floor']
        self.game_height=config['game']['height']

        self.w=config['goal']['width']
        self.h=config['goal']['height']

        self.image_front=pygame.transform.scale(pygame.image.load('src/img_res/goal_front.png').convert_alpha(),(int(self.w),int(self.h)))
        #self.rect_front=pygame.Rect(self.image_front.get_rect())

        self.image_back=pygame.transform.scale(pygame.image.load('src/img_res/goal_back.png').convert_alpha(),(int(self.w),int(self.h)))
        self.rect=pygame.Rect(self.image_back.get_rect())

        if(player==1):
            self.rect.left=0
        else:
            self.image_front=pygame.transform.flip(self.image_front,True,False)
            self.image_back=pygame.transform.flip(self.image_back,True,False)
            self.rect.right=self.game_width

        self.rect.top=config['goal']['from_top']

    def draw_front(self):
        self.display.blit(self.image_front,self.rect)

    def draw_back(self):
        self.display.blit(self.image_back,self.rect)