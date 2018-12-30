import pygame
import operator
import random
from src.config import config

class Background():

    game_width=config['game']['width']
    game_floor=config['game']['floor']
    game_height=config['game']['height']

    def __init__(self,display):
        self.display=display  
    
        self.cloud_intensity=config['background']['cloud_intensity']
        self.cloud_frequency=config['background']['cloud_frequency']
        self.bush_intensity=config['background']['bush_intensity']

        self.clouds=[]
        self.generate_clouds()
        self.clouds.sort(key=operator.attrgetter('sizefactor'))

        self.grass=[]
        self.generate_grass()

        self.bushes=[]
        #self.generate_bushes()

        self.trees=[]
        self.generate_trees()


    def draw(self):
        self.display.fill(config['color']['sky'])
        pygame.draw.rect(self.display,config['color']['floor'],(0,self.game_floor,self.game_width,self.game_height-self.game_floor))
        
        for cloud in self.clouds:
            cloud.draw()
            if(cloud.rect.right<0):
                cloud.rect.x+=1600+cloud.w
        
        for grass in self.grass:
            grass.draw()

        for bush in self.bushes:
            bush.draw()
        
        for tree in self.trees:
            tree.draw()
    
    
    def generate_clouds(self):  
        for i in range(self.cloud_intensity):
            cloud=Cloud(self.display)
            cloud.rect.x=random.randrange(0,self.game_width+400,self.cloud_frequency)
            self.clouds.append(cloud)

    def generate_grass(self):    
        for i in range(-10,self.game_width+10,15):
            grass=Grass(self.display)
            grass.rect.left=i
            self.grass.append(grass)

    def generate_bushes(self):    
        for i in range(self.bush_intensity):
            bush=Bush(self.display)
            bush.rect.left=i
            self.bushes.append(bush)
        
    def generate_trees(self):
        tree1=Tree(self.display)
        tree1.rect.left=config['background']['tree_offset']
        #tree1.image=pygame.transform.flip(tree1.image,True,False)
        self.trees.append(tree1)

        tree2=Tree(self.display)
        tree2.rect.right=self.game_width-config['background']['tree_offset']
        tree2.image=pygame.transform.flip(tree2.image,True,False)
        self.trees.append(tree2)

    def generate_goals(self):
        goal1=Goal(self.display)
        goal1.rect.left=0
        #tree1.image=pygame.transform.flip(tree1.image,True,False)
        self.goals.append(goal1)

        goal2=Goal(self.display)
        goal2.rect.right=self.game_width
        goal2.image=pygame.transform.flip(goal2.image,True,False)
        self.goals.append(goal2)
        


class Cloud(Background):    
    def __init__(self,display):
        self.display=display
        
        self.sizefactor=random.randint(33,100)/100
        
        self.w=int(config['background']['max_cloud']['width']*self.sizefactor)
        self.h=int(config['background']['max_cloud']['height']*self.sizefactor)
        
        self.vx=config['background']['max_cloud']['velocity_x']
        
        self.image=pygame.transform.scale(pygame.image.load('src/img_res/cloud.png').convert_alpha(),(int(self.w),int(self.h)))
        self.rect=pygame.Rect(self.image.get_rect())

        self.rect.y=random.randint(-1,config['background']['cloud_height'])

    
    def draw(self):
        self.physiks()
        self.display.blit(self.image,self.rect)
   
    def physiks(self):
        self.rect.x+=int(self.vx*self.sizefactor)


class Grass(Background):
    def __init__(self,display):
        self.display=display

        self.w=config['background']['max_grass']['width']
        self.h=config['background']['max_grass']['height']

        self.image=pygame.transform.scale(pygame.image.load('src/img_res/grass.png').convert_alpha(),(int(self.w),int(self.h)))
        self.rect=pygame.Rect(self.image.get_rect())
        self.rect.bottom=Background.game_floor

    def draw(self):
        self.display.blit(self.image,self.rect)

class Bush(Background):
    def __init__(self,display):
        self.display=display

        self.sizefactor=1#random.randint(50,100)/100

        self.w=int(config['background']['max_bush']['width']*self.sizefactor)
        self.h=int(config['background']['max_bush']['height']*self.sizefactor)

        self.image=pygame.transform.scale(pygame.image.load('src/img_res/bush.png').convert_alpha(),(int(self.w),int(self.h)))
        self.rect=pygame.Rect(self.image.get_rect())
        
        self.rect.bottom=self.game_floor+10

    def draw(self):
        self.display.blit(self.image,self.rect)

class Tree(Background):
    def __init__(self,display):
        self.display=display

        self.w=config['background']['tree']['width']
        self.h=config['background']['tree']['height']

        self.image=pygame.transform.scale(pygame.image.load('src/img_res/tree.png').convert_alpha(),(int(self.w),int(self.h)))
        self.rect=pygame.Rect(self.image.get_rect())
        
        self.rect.bottom=self.game_floor+15

    def draw(self):
        self.display.blit(self.image,self.rect)
