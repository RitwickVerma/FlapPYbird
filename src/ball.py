import pygame
import pygame.gfxdraw
from src.config import config

class Ball(pygame.sprite.Sprite):
    def __init__(self,display):
        pygame.sprite.Sprite.__init__(self)
        self.px=config['ball']['start_pos_x']
        self.py=config['ball']['start_pos_y']
        self.r=config['ball']['radius']
        self.vx=config['ball']['velocity_x']
        self.vy=config['ball']['velocity_y']
        self.ax=config['ball']['acceleration_x']
        self.ay=config['ball']['acceleration_y']
        self.mtop=0
        self.mbot=config['game']['floor']-2*self.r
        self.mlef=0
        self.mrig=config['game']['width']-2*self.r
        self.display=display
        self.rotvar=0

        self.image=pygame.transform.scale(pygame.image.load('src/football.png').convert_alpha(),(2*self.r,2*self.r))
        self.mask=pygame.mask.from_surface(self.image)
        
        self.rect=pygame.Rect(self.px,self.py,2*self.r, 2*self.r)
    
    def draw(self):
        self.physiks()
        self.rect=pygame.Rect(self.px,self.py,2*self.r, 2*self.r)
        #self.image=pygame.transform.rotate(self.image,5)
        self.display.blit(self.rot_center(self.image, self.rotvar),self.rect)   
        self.rotvar-=self.vx*0.5
        

    def physiks(self):   
        self.px+=self.vx
        self.vx+=self.ax

        self.py+=self.vy
        self.vy+=self.ay

        if(self.px>=self.mrig or self.px<=self.mlef):
            self.vx=-self.vx+self.ax

        if(self.py>=self.mbot or self.py<=self.mtop):
            self.vy=-self.vy+self.ay


    def rot_center(self,image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotozoom(image, angle,1)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image