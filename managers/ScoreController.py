from constants.constant import *

class ScoreController:
    def __init__(self, screen, score, win, font):
        self._screen = screen
        self.score = score
        self.miss = 0
        self.win = win
        self._font = font

        self._scoreText = "Your score: 0"
        self._missText = "You missed: 0"
    
    def getScore(self) -> int:
        return self.score

    def getMiss(self) -> int:
        return self.miss

    def toString(self,type) -> str:
        if type == "score":
            return str(self.score)
        elif type == "miss":
            return str(self.miss)

    def setScore(self,score):
        self.score = score

    def incrScore(self):
        self.score += 1

    def incrMiss(self):
        self.miss += 1

    def isWon(self) -> bool:
        return self.score >= self.win

    def update(self):
        self._scoreText = "Your score: " + str(self.score)
        self._missText = "You missed: " + str(self.miss)

    def draw(self):

        strScore = self._font.render(self._scoreText, 1, LIGHTGREEN)

        strMiss = self._font.render(self._missText, 1, LIGHTGREEN)

        pygame.draw.rect(self._screen.screen, BROWN, pygame.Rect(240,15,120,60))

        self._screen.screen.blit(strScore, (WIDTH//2 - strScore.get_width()//2, 20))

        self._screen.screen.blit(strMiss, (WIDTH//2 - strMiss.get_width()//2, 50))
