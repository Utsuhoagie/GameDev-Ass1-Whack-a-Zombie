from .Image import Image
from constants.constant import *

class Particle(Image):
    def __init__(self, screen, x, y, image, width, height):
        super().__init__(screen, x, y, image, width, height)
        self._timer = STARTIME
    
    def update(self,delta):
        self._minusTime(delta)
        
        # update position
        currentPos = super().getTopLeftPos()
        super().updatePos(currentPos[0] + STARDIRECTION[0], currentPos[1] + STARDIRECTION[1])

        # draw particle
        # self.draw()


    def draw(self):
        if self._timer > 0:
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
