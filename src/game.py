import pygame
import math
from src.config import config, control
from src.bird import Bird
from src.ball import Ball
from src.background import Background
from src.goal import Goal

class Game:

    game_width=config['game']['width']
    game_floor=config['game']['floor']
    game_height=config['game']['height']

    def __init__(self, display):
        self.display = display

        self.game_width=config['game']['width']
        self.game_floor=config['game']['floor']
        self.game_height=config['game']['height']

        self.k_p1_up=control['p1_bird']['up']
        self.k_p1_left=control['p1_bird']['left']
        self.k_p1_right=control['p1_bird']['right']
        self.k_p2_up=control['p2_bird']['up']
        self.k_p2_left=control['p2_bird']['left']
        self.k_p2_right=control['p2_bird']['right']

        self.k_pause=control['game']['pause']
        self.k_quit=control['game']['quit']
        self.k_fullscreen=control['game']['fullscreen']

        self.p1_bird=Bird(self.display,1)
        self.p2_bird=Bird(self.display,2)
        self.ball=Ball(self.display)
        self.background=Background(self.display)
        self.p1_goal=Goal(self.display,1)
        self.p2_goal=Goal(self.display,2)
        self.p1_score=0
        self.p2_score=0
        self.last_touch=0
        
    def game_loop(self):

        

        clock = pygame.time.Clock()
        
        running=True
        while running:

            events=pygame.event.get()            
            for event in events:
                if(event.type == pygame.QUIT):
                    exit()
                if(event.type == pygame.KEYDOWN):
                    if(event.key == self.k_pause):
                        self.pause()
                    if(event.key == self.k_quit):
                        exit()
                    if(event.key == self.k_fullscreen):
                        pygame.display.toggle_fullscreen()


            key_pressed=pygame.key.get_pressed()
            if(key_pressed[self.k_p1_up]):
                self.p1_bird.move_up()
            if(key_pressed[self.k_p1_left]):
                self.p1_bird.move_left()
            if(key_pressed[self.k_p1_right]):
                self.p1_bird.move_right()
            if(key_pressed[self.k_p2_up]):
                self.p2_bird.move_up()
            if(key_pressed[self.k_p2_left]):
                self.p2_bird.move_left()
            if(key_pressed[self.k_p2_right]):
                self.p2_bird.move_right()
   
            self.detect_collision()

            self.check_goal()
            
            self.background.draw()
            
            self.write(str(self.p1_score)+'-'+str(self.p2_score),150,self.game_width/2,100)

            self.p1_goal.draw_back() 
            self.p2_goal.draw_back()   
            self.p1_bird.draw()
            self.p2_bird.draw()
            self.ball.draw()
            self.p1_goal.draw_front()
            self.p2_goal.draw_front()

            pygame.display.update()

            clock.tick(config['game']['fps'])


    def pause(self):
        paused=True
        #pygame.draw.rect(self.display,)
        self.write('PAUSED',200,self.game_width/2,self.game_floor/2)

        pygame.display.update()
        while paused:
            events=pygame.event.get()            
            for event in events:
                if(event.type == pygame.QUIT):
                    exit()
                if(event.type == pygame.KEYDOWN):
                    if(event.key == self.k_pause):
                        paused=False
                    if(event.key == self.k_quit):
                        exit()
                    if(event.key == self.k_fullscreen):
                        pygame.display.toggle_fullscreen()
    

    def detect_collision(self):
        if(pygame.sprite.collide_mask(self.p1_bird,self.ball) is not None):     
                self.p1_bird.rect.x-=self.p1_bird.vx+self.p1_bird.ax
                self.p1_bird.rect.y-=self.p1_bird.vy+self.p1_bird.ay

                self.ball.rect.x-=self.ball.vx+self.ball.ax
                self.ball.rect.y-=self.ball.vy+self.ball.ay
                
                self.p1_bird.vx, self.ball.vx=self.ball.vx, self.p1_bird.vx
                self.p1_bird.vy, self.ball.vy=self.ball.vy, self.p1_bird.vy

                self.last_touch=1

        if(pygame.sprite.collide_mask(self.p2_bird,self.ball) is not None):     
                self.p2_bird.rect.x-=self.p2_bird.vx+self.p2_bird.ax
                self.p2_bird.rect.y-=self.p2_bird.vy+self.p2_bird.ay

                self.ball.rect.x-=self.ball.vx+self.ball.ax
                self.ball.rect.y-=self.ball.vy+self.ball.ay
                
                self.p2_bird.vx, self.ball.vx=self.ball.vx, self.p2_bird.vx
                self.p2_bird.vy, self.ball.vy=self.ball.vy, self.p2_bird.vy

                self.last_touch=2     


    def check_goal(self):
        if(self.ball.rect.centerx<self.p1_goal.rect.right and self.ball.rect.centerx>self.p1_goal.rect.right-50 and self.ball.rect.top>self.p1_goal.rect.top and self.ball.rect.bottom<self.p1_goal.rect.bottom and self.ball.vx!=0):
            self.p1_score+=1
            if(self.last_touch==2):
                self.write('GOOOAL!!',200,self.game_width/2,self.game_height/2)
            else:
                self.write('OWN GOAL!',150,self.game_width/2,self.game_height/2)
            pygame.display.update()
            pygame.time.delay(1000)

        
        if(self.ball.rect.centerx>self.p2_goal.rect.left and self.ball.rect.centerx<self.p2_goal.rect.left+50 and self.ball.rect.top>self.p2_goal.rect.top and self.ball.rect.bottom<self.p2_goal.rect.bottom and self.ball.vx!=0):
            self.p2_score+=1
            if(self.last_touch==1):
                self.write('GOOOAL!!',200,self.game_width/2,self.game_height/2)
            else:
                self.write('OWN GOAL!',150,self.game_width/2,self.game_height/2)
        
            pygame.display.update()

            pygame.time.delay(1000)

    def write(self,text,size,x,y,color=config['color']['font']):
        text=pygame.font.SysFont('cabinsketch',size).render(text,True,color)
        rect=text.get_rect()
        rect.center=(x,y)
        self.display.blit(text,rect)