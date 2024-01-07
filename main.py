import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image(os.path.join("assets", "bird1.png"))),
    pygame.transform.scale2x(pygame.image(os.path.join("assets", "bird2.png"))),
    pygame.transform.scale2x(pygame.image(os.path.join("assets", "bird3.png"))),
]
PIPE_IMG = pygame.transform.scale2x(pygame.image(os.path.join("assets", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image(os.path.join("assets", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image(os.path.join("assets", "bg.png")))
