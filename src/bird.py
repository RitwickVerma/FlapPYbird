import pygame
from src.config import config

class Bird(pygame.sprite.Sprite):
    def __init__(self,display):
        pygame.sprite.Sprite.__init__(self)
        self.px=config['bird']['start_pos_x']
        self.py=config['bird']['start_pos_y']
        self.vx=config['bird']['velocity_x']
        self.vy=config['bird']['velocity_y']
        self.ax=config['bird']['acceleration_x']
        self.ay=config['bird']['acceleration_y']
        self.vjy=config['bird']['velocity_jump_y']
        self.mtop=0
        self.mbot=config['game']['floor']-config['bird']['height']
        self.mlef=0
        self.mrig=config['game']['width']-config['bird']['width']
        self.display=display
        self.image=pygame.transform.scale(pygame.image.load('src/flappy.png').convert_alpha(),(config['bird']['width'],config['bird']['height']))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect=pygame.Rect(self.px,self.py,config['bird']['width'],config['bird']['height'])
        self.bird_flipped=False
    
    def draw(self):
        self.physiks()
        self.rect=pygame.Rect(self.px, self.py, self.rect.width, self.rect.height)   
           
        self.display.blit(pygame.transform.rotozoom(self.image, self.vy*(1 if self.bird_flipped else -1),1),self.rect)        

    def physiks(self):   
        self.px+=self.vx
        self.vx+=self.ax
        self.vx=self.vx*0.8

        self.py+=self.vy
        self.vy+=self.ay
        #self.vy=self.vy*0.9

        if(self.px>=self.mrig or self.px<=self.mlef):
            self.vx=-self.vx+self.ax

        if(self.py>=self.mbot or self.py<=self.mtop):
            self.vy=-self.vy+self.ay
    
    def move_up(self):
        if(self.py>self.mtop):
            self.vy=self.vjy
            
    """def move_down(self):
        if(self.py<self.mbot):
            self.vy=-self.vuy"""
    
    def move_left(self):
        if(self.px>self.mlef):
            self.vx=-config['bird']['velocity_x']
            if(not self.bird_flipped):
                self.image=pygame.transform.flip(self.image,True,False)
                self.bird_flipped=True
    
    def move_right(self):
        if(self.px<self.mrig):
            self.vx=config['bird']['velocity_x']
            if(self.bird_flipped):
                self.image=pygame.transform.flip(self.image,True,False)
                self.bird_flipped=False
