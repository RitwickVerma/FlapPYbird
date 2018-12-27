import pygame

config = {
    'game': {
        'caption': 'FlapPYball',
        'width': 1600,
        'height': 900,
        'floor':800,
        'fps': 45,
    },
    'bird': {
        'start_pos_x':500,
        'start_pos_y':300,
        'width': 60,
        'height': 42,
        'velocity_x':30,
        'velocity_y':0,
        'acceleration_x':0,
        'acceleration_y':3,
        'velocity_jump_y':-30
    },
    'ball': {
        'start_pos_x':800,
        'start_pos_y':300,
        'radius': 40,
        'velocity_x':0,
        'velocity_y':0,
        'acceleration_x':0,
        'acceleration_y':3
    },

    'background': {
        'cloud_intensity':10,
        'max_cloud': {
            'width':300,
            'height':150,
            'velocity_x':-6
        }
    },

    'color': {
        'ball': (255,99,71),
        'floor': (222, 216, 149),
        'sky': (112,197,206),
    }
}

control={
    'bird':{
        'up':pygame.K_UP,
        'left':pygame.K_LEFT,
        'right':pygame.K_RIGHT
    },
    'game':{
        'pause':pygame.K_p,
        'quit':pygame.K_ESCAPE,
        'fullscreen':pygame.K_f
    }
}