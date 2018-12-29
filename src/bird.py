import pygame
from src.config import config

class Bird(pygame.sprite.Sprite):
    def __init__(self,display):
        pygame.sprite.Sprite.__init__(self)

        self.display=display

        self.game_width=config['game']['width']
        self.game_floor=config['game']['floor']
        self.game_height=config['game']['height']

        self.vx=config['bird']['velocity_x']
        self.vy=config['bird']['velocity_y']
        self.ax=config['bird']['acceleration_x']
        self.ay=config['bird']['acceleration_y']
        self.vjy=config['bird']['velocity_jump_y']
        
        self.image=pygame.transform.scale(pygame.image.load('src/img_res/flappy.png').convert_alpha(),(config['bird']['width'],config['bird']['height']))
        self.mask=pygame.mask.from_surface(self.image)
        self.rect=pygame.Rect(self.image.get_rect())

        self.rect.x=config['bird']['start_pos_x']
        self.rect.y=config['bird']['start_pos_y']
        
        self.bird_flipped=False
    
    def draw(self):
        self.physiks()        
        self.display.blit(pygame.transform.rotozoom(self.image, self.vy*(1 if self.bird_flipped else -1),1),self.rect)        

    def physiks(self):   
        
        self.vx=self.vx*0.8
        self.vx+=self.ax
        self.rect.x+=self.vx
        
        
        self.vy+=self.ay
        self.rect.y+=self.vy

        if(self.rect.right>self.game_width or self.rect.left<0):
            self.vx=-self.vx
            

        if((self.rect.bottom>self.game_floor or self.rect.top<0)):
            self.vy=-self.vy
            
        self.rect.left = self.clip(self.rect.left, 0, self.game_width)
        self.rect.right = self.clip(self.rect.right, 0, self.game_width)        
        self.rect.top = self.clip(self.rect.top, 0, self.game_floor)
        self.rect.bottom = self.clip(self.rect.bottom, 0, self.game_floor)                

    def clip(self,val, minval, maxval):
        return min(max(val, minval), maxval)

            
    
    def move_up(self):
        if(self.rect.top>0):
            self.vy=self.vjy
            
    """def move_down(self):
        if(self.py<self.mbot):
            self.vy=-self.vuy"""
    
    def move_left(self):
        if(self.rect.left>0):
            self.vx=-config['bird']['velocity_x']
            if(not self.bird_flipped):
                self.image=pygame.transform.flip(self.image,True,False)
                self.bird_flipped=True
    
    def move_right(self):
        if(self.rect.right<self.game_width):
            self.vx=config['bird']['velocity_x']
            if(self.bird_flipped):
                self.image=pygame.transform.flip(self.image,True,False)
                self.bird_flipped=False
