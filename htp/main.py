from managers.MouseManager import MouseManager
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
        self.sounds = dict()

        # manager
        self._scoreManager = None
        self._mouseManager = None

        # game objects

        self._background = None
        self._holeList = []
        self._botHoleList = []
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
        # self._assets["hole"] = pygame.image.load("./assets/objects/hole.png")
        # self._assets["hole"] = pygame.transform.scale(self._assets["hole"], (212, 152))
        self._assets["topHole"] = pygame.image.load("./assets/objects/top_hole.png")
        self._assets["topHole"] = pygame.transform.scale(self._assets["topHole"], (212, 152))
        self._assets["botHole"] = pygame.image.load("./assets/objects/bot_hole.png")
        self._assets["botHole"] = pygame.transform.scale(self._assets["botHole"], (212, 152))
        # self._assets["zombie"] = pygame.image.load("./assets/objects/zombie.png")
        # self._assets["zombie"] = pygame.transform.scale(self._assets["zombie"], (54, 101))
        self._assets["zombie"] = pygame.image.load("./assets/sprites/ZombieHead.png")
        self._assets["zombieDead"] = pygame.image.load("./assets/sprites/ZombieDead.png")
        self._assets["bonkHammer"] = pygame.image.load("./assets/sprites/hammer.png")
        self._assets["readyHammer"] = pygame.transform.rotate(self._assets["bonkHammer"], -30)

        self.sounds['bonk'] = pygame.mixer.Sound("./assets/sounds/bonk.ogg")
        self.sounds['swing'] = pygame.mixer.Sound("./assets/sounds/swing.ogg")

        # background sound
        pygame.mixer.music.load("./assets/sounds/PvZSoundtrack.mp3")

    def _create(self):
        self.FONT = pygame.font.SysFont("arial",15)
        self.WIN_FONT = pygame.font.SysFont("comicsans",50)

        self._scoreManager = ScoreController(self,0, WIN_CONDITION, self.FONT)
        self._mouseManager = MouseManager(self, 20, -100, [self._assets['readyHammer'], self._assets['bonkHammer']], 90, 59)

        pygame.display.set_icon(self._assets["logo"])
        pygame.display.set_caption("Zombie Shooter")

        self._holeList.append(Hole(self, 0, 100, self._assets["topHole"], 212, 152))
        self._botHoleList.append(Hole(self, 0, 100, self._assets["botHole"], 212, 151))
        self._zombieList.append(AnimatedZombie(self, 60, 130, [self._assets['zombie'], self._assets['zombieDead']], 54, 101, self._botHoleList[0].getTopLeftPos()))

        self._holeList.append(Hole(self, 300, 100, self._assets["topHole"], 212, 152))
        self._botHoleList.append(Hole(self, 300, 100, self._assets["botHole"], 212, 151))
        self._zombieList.append(AnimatedZombie(self, 360, 130, [self._assets['zombie'], self._assets['zombieDead']], 54, 101, self._botHoleList[1].getTopLeftPos()))

        self._holeList.append(Hole(self, 0, 400, self._assets["topHole"], 212, 152))
        self._botHoleList.append(Hole(self, 0, 400, self._assets["botHole"], 212, 151))
        self._zombieList.append(AnimatedZombie(self, 60, 430, [self._assets['zombie'], self._assets['zombieDead']], 54, 101, self._botHoleList[2].getTopLeftPos()))

        self._holeList.append(Hole(self, 300, 400, self._assets["topHole"], 212, 152))
        self._botHoleList.append(Hole(self, 300, 400, self._assets["botHole"], 212, 151))
        self._zombieList.append(AnimatedZombie(self, 360, 430, [self._assets['zombie'], self._assets['zombieDead']], 54, 101, self._botHoleList[3].getTopLeftPos()))

        # background sound
        pygame.mixer.music.play(-1)

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
        self._mouseManager.update()

        [hole.update(delta) for hole in self._holeList]
        [zombie.update(delta) for zombie in self._zombieList]
        [hole.update(delta) for hole in self._botHoleList]

        # handle input
        if not self.isHit and MouseInput.isClick():
            pygame.event.post(pygame.event.Event(INCREASEMISSSCORE))
            self.sounds['swing'].play()

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
        [hole.draw() for hole in self._botHoleList]

        self._mouseManager.draw()
        # reload the screen
        pygame.display.flip()
    def _on_cleanup(self):
        pygame.quit()
 
if __name__ == "__main__" :
    theApp = App(WIDTH, HEIGHT)
    theApp.execute()