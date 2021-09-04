from typing import Tuple


class MouseInput:
    _isDown = False
    _isUp = False
    _isClick = False
    def setDown():
        if not MouseInput._isDown:
            MouseInput._isDown = True
            MouseInput._isClick = False
    def setUp():
        if MouseInput._isDown:
            MouseInput._isDown = False
            MouseInput._isClick = True
        
    def isClick():
        return MouseInput._isClick
    def isUp():
        return not MouseInput._isDown
    def isDown():
        return MouseInput._isDown

    def update():
        MouseInput._isClick = False