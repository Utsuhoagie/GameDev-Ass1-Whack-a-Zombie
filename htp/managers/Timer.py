class Timer:
    def __init__(self, timer, active):
        self.timer = timer
        self.active = active
    
    def decreaseBy(self,decr):
        self.timer -= decr
    
    def setTo(self,timer,active):
        self.timer = timer
        self.active = active

    def getTimer(self):
        return self.timer

    def isActive(self):
        return self.active