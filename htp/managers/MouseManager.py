from managers.MouseInput import MouseInput
from objects.Image import Image
import pygame
from pygame.locals import *

class MouseManager(Image):
    def __init__(self, screen, x, y, imageList, width, height, timer = 1000):
        super().__init__(screen, x, y, imageList[0], width, height)
        # self._x = self._HIDEDX
        # self._y = self._HIDEDY
        self._ORIGINTIMER = timer
        self._timer = self._ORIGINTIMER

        # for animation
        self._frames = imageList
        self._image = imageList[0]

        pygame.mouse.set_visible(False)

    def update(self, delta = 0):
        self._x = pygame.mouse.get_pos()[0] - 25
        self._y = pygame.mouse.get_pos()[1] - 50

        if pygame.mouse.get_pressed()[0]:
            self._image = self._frames[1]
        else:
            self._image = self._frames[0]