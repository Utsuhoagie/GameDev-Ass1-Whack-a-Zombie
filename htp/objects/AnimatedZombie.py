from managers.MouseInput import MouseInput
from .Image import Image
from enum import Enum
import pygame
from pygame.locals import *
from constants.constant import *
from constants.constant import *
import random

class State(Enum):
    SHOWED = 1
    SHOWING = 2
    HIDED = 3
    HIDEING = 4
    DIEING = 5
    DIED = 6

DISTANCE = 35

class AnimatedZombie(Image):
    def __init__(self, screen, x, y, imageList, width, height, holeImagePos):
        super().__init__(screen, x, y, imageList[0], width, height)
        self.state = State.HIDED
        self._SHOWEDX = x
        self._SHOWEDY = y
        self._HIDEDX = x
        self._HIDEDY = y + DISTANCE
        self._x = self._HIDEDX
        self._y = self._HIDEDY
        self._holdImagePos = holeImagePos
        self._timer = random.randint(HIDEDTIME[0], HIDEDTIME[1])

        # for animation
        self._frames = imageList
        self._image = imageList[0]

    def update(self, delta):
        if self.state == State.HIDED:
            self._minusTime(delta)
            if self._timer == 0:
                self.state = State.SHOWING
                self._timer = ANIMATIONTIME
        elif self.state == State.SHOWING:
            minusTime = self._minusTime(delta)
            if self._timer == 0:
                self.state = State.SHOWED
                self._timer = random.randint(SHOWEDTIME[0], SHOWEDTIME[1])

            self._handleInput()

            self._y -= minusTime * DISTANCE/ANIMATIONTIME
        elif self.state == State.SHOWED:
            self._minusTime(delta)

            if self._timer == 0:
                self.state = State.HIDEING
                self._timer = ANIMATIONTIME

            # handle input
            self._handleInput()

        elif self.state == State.HIDEING:
            minusTime = self._minusTime(delta)
            if self._timer == 0:
                self.state = State.HIDED
                self._timer = random.randint(HIDEDTIME[0], HIDEDTIME[1])

            self._handleInput()

            self._y += minusTime * DISTANCE/ANIMATIONTIME
        elif self.state == State.DIEING:
            minusTime = self._minusTime(delta)
            if self._timer == 0:
                self.state = State.DIED
                self._timer = random.randint(DIEDTIME[0], DIEDTIME[1])

            # handle input
            # if pygame.mouse.get_pressed()[0]:
            if MouseInput.isClick():
                mX = pygame.mouse.get_pos()[0]
                mY = pygame.mouse.get_pos()[1]
                if self._isInImage(mX, mY):
                    self._screen.sounds['bonk'].play()
                    self._screen.isHit = True
            
        elif self.state == State.DIED:
            # revive
            self._timer = random.randint(HIDEDTIME[0], HIDEDTIME[1])
            self.state = State.HIDED

            self._x = self._HIDEDX
            self._y = self._HIDEDY
            pass

        self._updateAnimation(delta)

    def _isInImage(self, mouseXPos, mouseYPos):
        if (
            (mouseXPos >= self._x)
        and (mouseXPos <= self._x + self._width)
        and (mouseYPos >= self._y)
        and (mouseYPos <= self._holdImagePos[1] + HOLEOFFSET)
            ):
            return True
        return False

    def _handleInput(self):
        if MouseInput.isClick():
            mX = pygame.mouse.get_pos()[0]
            mY = pygame.mouse.get_pos()[1]
            if self._isInImage(mX, mY):
                self.state = State.DIEING
                self._timer = DIEINGTIME
                pygame.event.post(pygame.event.Event(INCREASESCORE))
                self._screen.sounds['bonk'].play()
                self._screen.isHit = True

    def _updateAnimation(self, delta):
        if self.state != State.DIED and self.state != State.DIEING:
            self._image = self._frames[0]
        else:
            self._image = self._frames[1]

    def draw(self):
        if self.state == State.HIDED:
            return
        elif self.state == State.SHOWING:
            # self._screen.screen.blit(self._image, (self._x, self._y), (0, 0, self._width, 176 - self._y))
            super().draw()
        elif self.state == State.SHOWED:
            # self._screen.screen.blit(self._image, (self._x, self._y), (0, 0, self._width, 176 - self._y))
            super().draw()
        elif self.state == State.HIDEING:
            # self._screen.screen.blit(self._image, (self._x, self._y), (0, 0, self._width, 176 - self._y))
            super().draw()
        elif self.state == State.DIEING:
            # self._screen.screen.blit(self._image, (self._x, self._y), (0, 0, self._width, 176 - self._y))
            super().draw()

    # minus time and return minus time
    def _minusTime(self, delta):
        if self._timer - delta > 0:
            self._timer -= delta
            return delta
        else:
            minusTime = self._timer
            self._timer = 0
            return minusTime
