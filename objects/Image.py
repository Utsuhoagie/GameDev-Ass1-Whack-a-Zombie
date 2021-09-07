import pygame
from pygame.locals import *

class Image:
    def __init__(self, screen, x, y, image, width, height):
        self._screen = screen
        self._image = image
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    def update(self,delta):
        pass

    def updatePos(self, x, y):
        self._x = x
        self._y = y

    def draw(self):
        self._screen.screen.blit(self._image, (self._x, self._y))

    def _isInImage(self, mouseXPos, mouseYPos):
        if (
            (mouseXPos >= self._x)
        and (mouseXPos <= self._x + self._width)
        and (mouseYPos >= self._y)
        and (mouseYPos <= self._y + self._height)
            ):
            return True
        return False

    def getTopLeftPos(self):
        return (self._x, self._y)