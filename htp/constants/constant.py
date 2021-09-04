import pygame
from pygame.locals import *

# ----- Window --------------------------------------
WIDTH, HEIGHT = 600,600

# ----- Colors --------------------------------------
BLACK = (0,0,0)
GRAY = (100,100,100)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (252,227,0)

# ----- Gameplay ------------------------------------
FPS = 60

WIN_CONDITION = 5

# User Event
INCREASESCORE = pygame.USEREVENT + 1
INCREASEMISSSCORE = pygame.USEREVENT + 2
HITAZOMBIE = pygame.USEREVENT + 3