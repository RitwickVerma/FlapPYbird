import pygame
import operator
import random
from src.config import config

class Background:
    def __init__(self,display):
        self.display=display
        self.w=config['game']['width']
        self.h=config['game']['height']
        self.floor=config['game']['floor']
        self.cloud_intensity=config['background']['cloud_intensity']
        
        self.clouds=[]
        self.generate_clouds()
        self.clouds.sort(key=operator.attrgetter('sizefactor'))

    def draw(self):

        self.display.fill(config['color']['sky'])
        pygame.draw.rect(self.display,config['color']['floor'],(0,self.floor,self.w,self.h-self.floor))
        
        for cloud in self.clouds:
            cloud.draw()
            if(cloud.rect.right<0):
                cloud.px+=1600+cloud.w
    
    
    def generate_clouds(self):
    
        for i in range(self.cloud_intensity):
            cloud=Cloud(self.display)
            cloud.px=random.randrange(0,2000,200)
            self.clouds.append(cloud)


    def get_width(self):
        return self.w

class Cloud(Background):    
    def __init__(self,display):
        self.display=display
        
        self.sizefactor=random.randint(33,100)/100
        
        self.w=config['background']['max_cloud']['width']*self.sizefactor
        self.h=config['background']['max_cloud']['height']*self.sizefactor
        
        self.px=2000
        self.py=random.randint(-1,200)
        self.vx=config['background']['max_cloud']['velocity_x']
        
        self.image=pygame.transform.scale(pygame.image.load('src/cloud.png').convert_alpha(),(int(self.w),int(self.h)))
        self.rect=pygame.Rect(self.px,self.py,self.w,self.h)

    def draw(self):
        self.physiks()
        self.rect=pygame.Rect(self.px,self.py,self.w,self.h)
        self.display.blit(self.image,self.rect)

    def physiks(self):
        self.px+=int(self.vx*self.sizefactor)