import pygame
from src.config import config

class Ball(pygame.sprite.Sprite):
    def __init__(self,display):
        pygame.sprite.Sprite.__init__(self)

        self.display=display

        self.game_width=config['game']['width']
        self.game_floor=config['game']['floor']
        self.game_height=config['game']['height']
        
        self.r=config['ball']['radius']
        self.vx=config['ball']['velocity_x']
        self.vy=config['ball']['velocity_y']
        self.ax=config['ball']['acceleration_x']
        self.ay=config['ball']['acceleration_y']

        self.rotvar=0

        self.image=pygame.transform.scale(pygame.image.load('src/img_res/football.png').convert_alpha(),(2*self.r,2*self.r))
        self.mask=pygame.mask.from_surface(self.image)
        
        self.rect=pygame.Rect(self.image.get_rect())
        self.rect.x=config['ball']['start_pos_x']
        self.rect.y=config['ball']['start_pos_y']

    
    def draw(self):
        self.physiks()
        self.display.blit(self.rot_center(self.image, self.rotvar),self.rect)   
        self.rotvar-=self.vx*0.5
        

    def physiks(self):   

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


    def rot_center(self,image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotozoom(image, angle,1)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image