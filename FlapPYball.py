import pygame
from src.game import Game
from src.config import config
#from pygame.locals import *
 
def main():
    display=pygame.display.set_mode((config['game']['width'],config['game']['height']))
    pygame.display.set_caption(config['game']['caption'])
    pygame.font.init()
    flappyball=Game(display)
    flappyball.loop()
 
if __name__ == "__main__":
    main()