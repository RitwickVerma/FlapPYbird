import pygame
import math
from src.config import config, control
from src.bird import Bird
from src.ball import Ball
from src.background import Background

class Game:

    game_width=config['game']['width']
    game_floor=config['game']['floor']
    game_height=config['game']['height']

    def __init__(self, display):
        self.display = display

        self.game_width=config['game']['width']
        self.game_floor=config['game']['floor']
        self.game_height=config['game']['height']

        self.k_up=control['bird']['up']
        self.k_left=control['bird']['left']
        self.k_right=control['bird']['right']
        self.k_pause=control['game']['pause']
        self.k_quit=control['game']['quit']
        self.k_fullscreen=control['game']['fullscreen']
        
    def loop(self):

        bird=Bird(self.display)
        ball=Ball(self.display)
        background=Background(self.display)

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
                bird.rect.x-=bird.vx+bird.ax
                bird.rect.y-=bird.vy+bird.ay

                ball.rect.x-=ball.vx+ball.ax
                ball.rect.y-=ball.vy+ball.ay
                
                bird.vx, ball.vx=ball.vx, bird.vx
                bird.vy, ball.vy=ball.vy, bird.vy                
            

            background.draw()    
            bird.draw()
            ball.draw()

            pygame.display.update()

            clock.tick(config['game']['fps'])

    def pause(self):
        paused=True
        #pygame.draw.rect(self.display,)
        text=pygame.font.SysFont('cabinsketch',200).render('PAUSED',True,config['color']['font'])
        rect=text.get_rect()
        rect.center=(self.game_width/2,self.game_floor/2)
        self.display.blit(text,rect)

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