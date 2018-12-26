import pygame
import math
from src.config import config,control
from src.bird import Bird
from src.ball import Ball

class Game:
    def __init__(self, display):
        self.display = display
        self.w=config['game']['width']
        self.h=config['game']['height']
        self.floor=config['game']['floor']

        self.k_up=control['bird']['up']
        self.k_left=control['bird']['left']
        self.k_right=control['bird']['right']
        self.k_pause=control['game']['pause']
        self.k_quit=control['game']['quit']
        self.k_fullscreen=control['game']['fullscreen']
        
    def loop(self):

        bird=Bird(self.display)
        ball=Ball(self.display)

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
            if(key_pressed[self.k_up]):
                bird.move_up()
            if(key_pressed[self.k_left]):
                bird.move_left()
            if(key_pressed[self.k_right]):
                bird.move_right()

            if(pygame.sprite.collide_mask(bird,ball) is not None):     
                bird.px=bird.px-bird.vx+bird.ax
                bird.py=bird.py-bird.vy+bird.ay
                
                bird.vx, ball.vx=ball.vx, bird.vx
                bird.vy, ball.vy=ball.vy, bird.vy                

            
            self.display.fill(config['color']['sky'])
            
            pygame.draw.rect(self.display,config['color']['floor'],(0,self.floor,self.w,self.h-self.floor))

            
            bird.draw()
            ball.draw()

            pygame.display.update()


            clock.tick(config['game']['fps'])

    def pause(self):
        paused=True
        #pygame.draw.rect(self.display,config['color']['floor'],(700,200,150,200))
        #pygame.display.update()
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