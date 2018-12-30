import pygame

color={
    'red': (255,99,71),
    'green': (60,179,113),
    'blue': (112,197,206),
    'yellow':(222, 216, 149),
    'white':(255,255,255),
    'black':(0,0,0)
}

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
        'start_pos_y':200,
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
    'goal': {
        'width':100,
        'height':130,
        'from_top':100
    },

    'background': {
        'cloud_intensity':10,
        'cloud_frequency':200,
        'bush_intensity':2,
        'bush_frequency':1,
        'cloud_height':150,
        'tree_offset':20,
        'max_cloud': {
            'width':300,
            'height':150,
            'velocity_x':-6
        },
        'max_grass':{
            'width':10,
            'height':10
        },
        'max_bush':{
            'width':80,
            'height':60
        },
        'tree':{
            'width':300,
            'height':450
        }
    },

    'color': {
        'sky': color['blue'],
        'floor': color['green'],
        'font': color['white']
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

