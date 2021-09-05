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

# Zombie
SHOWEDTIME = (50, 400)
ANIMATIONTIME = 100
HIDEDTIME = (1000, 3000)
DIEINGTIME = 2000
DIEDTIME = (1000, 3000)

# Hole properties
# If hole at position (0, 0) => the center bottom y of hole will be (..., 180)
HOLEOFFSET = 90 # have calculate the current hole image with the scale