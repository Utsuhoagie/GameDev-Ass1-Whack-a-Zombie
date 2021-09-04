from objects.AnimatedZombie import AnimatedZombie
from managers.MouseInput import MouseInput
from objects.Hole import Hole
import sys
sys.path.append("/")
import pygame
from pygame.locals import *
from managers.ScoreController import ScoreController
from objects.Zombie import Zombie
from constants.constant import *

class App:
    def __init__(self, width = 640, height = 400):
        self._clock = pygame.time.Clock()
        self._running = True
        self.screen = None
        self.size = self.weight, self.height = width, height
        self._assets = dict()

        # manager
        self._scoreManager = None

        # game objects

        self._background = None
        self._holeList = []
        self._zombieList = []

        # variables
        self._scoreText = "Your score: 0"
        self._missText = "You missed: 0"

        # flag
        self._winFlag = False
        self.isHit = False

        self.FONT = None
        self.WIN_FONT = None


    def execute(self):
        if self._init() == False:
            self._running = False

        # load assets
        self._preload()
        
        # create object
        self._create()


        # event handling, gets all event from the event queue
        while( self._running ):
            delta = self._clock.tick(FPS)
            # process the the event queue
            for event in pygame.event.get():
                self._handleEvent(event)
            self._update(delta)
            self._render()
        self._on_cleanup()

    
    def _init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    # all used assets will be load here
    def _preload(self):
        # ----- Fonts ---------------------------------------
        self._assets["logo"] = pygame.image.load("./assets/logo/logo.jpg")
        self._assets["hole"] = pygame.image.load("./assets/objects/hole.png")
        self._assets["hole"] = pygame.transform.scale(self._assets["hole"], (212, 152))
        # self._assets["zombie"] = pygame.image.load("./assets/objects/zombie.png")
        # self._assets["zombie"] = pygame.transform.scale(self._assets["zombie"], (54, 101))
        self._assets["zombie"] = pygame.image.load("./assets/sprites/ZombieHead.png")
        self._assets["zombieDead"] = pygame.image.load("./assets/sprites/ZombieDead.png")

    def _create(self):
        self.FONT = pygame.font.SysFont("arial",15)
        self.WIN_FONT = pygame.font.SysFont("comicsans",50)

        self._scoreManager = ScoreController(self,0, WIN_CONDITION, self.FONT)

        pygame.display.set_icon(self._assets["logo"])
        pygame.display.set_caption("Zombie Shooter")

        self._holeList.append(Hole(self, 0, 100, self._assets["hole"], 212, 152))
        # self._zombieList.append(Zombie(self, 60, 110, self._assets['zombie'], 54, 101))
        self._zombieList.append(AnimatedZombie(self, 60, 110, [self._assets['zombie'], self._assets['zombieDead']], 54, 101))

    def _handleEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            MouseInput.setDown()
        elif event.type == pygame.MOUSEBUTTONUP:
            MouseInput.setUp()
        elif event.type == INCREASESCORE:
            self._scoreManager.incrScore()
        elif event.type == INCREASEMISSSCORE:
            self._scoreManager.incrMiss()
    def _update(self, delta):
        self._scoreManager.update()

        [hole.update(delta) for hole in self._holeList]
        [zombie.update(delta) for zombie in self._zombieList]

        # handle input
        if not self.isHit and MouseInput.isClick():
            pygame.event.post(pygame.event.Event(INCREASEMISSSCORE))
            pygame.mixer.music.load("./assets/sounds/swing.ogg")
            pygame.mixer.music.play()

        # reset global variable
        self.isHit = False

        # for system
        MouseInput.update()
        
    def _render(self):
        # erase the screen
        self.screen.fill(BLACK)

        self._background = self.screen.fill((255,255,255))

        self._scoreManager.draw()

        [hole.draw() for hole in self._holeList]
        [zombie.draw() for zombie in self._zombieList]

        # reload the screen
        pygame.display.flip()
    def _on_cleanup(self):
        pygame.quit()
 
if __name__ == "__main__" :
    theApp = App(WIDTH, HEIGHT)
    theApp.execute()