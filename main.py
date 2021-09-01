import pygame as pg
import os
import random
pg.init()

# ----- Window --------------------------------------
WIDTH, HEIGHT = 600,600
SCREEN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Clicky")

# ----- Colors --------------------------------------

BLACK = (0,0,0)
GRAY = (100,100,100)
WHITE = (255,255,255)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (252,227,0)


# ----- Fonts ---------------------------------------

FONT = pg.font.SysFont("arial",15)
WIN_FONT = pg.font.SysFont("comicsans",50)

# ----- Gameplay ------------------------------------
FPS = 60

WIN_CONDITION = 5
WIN = pg.USEREVENT + 1

# ----- Classes -------------------------------------

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


class ScoreController:
    def __init__(self, score, win):
        self.score = score
        self.miss = 0
        self.win = win
    
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


# ----- Functions -----------------------------------

# ---------- Handlers -------------

# ---------- Draw -----------------

def draw_screen(rectList, textList, scoreController: ScoreController):
    SCREEN.fill(BLACK)

    [pg.draw.rect(SCREEN,GREEN,rect) for rect in rectList]


    text_y_displace = 0

    for text in textList:
        str = FONT.render(text,1,WHITE)     # this is a surface
        SCREEN.blit(str,(WIDTH//2 - str.get_width()//2, 30 + text_y_displace))
        text_y_displace += 40

    textList.clear()

    if scoreController.isWon():
        pg.event.post(pg.event.Event(WIN))

    pg.display.update()


def draw_winText():
    str = WIN_FONT.render("You win!",1,RED)
    SCREEN.blit(str,(WIDTH//2 - str.get_width()//2, 150))

    pg.display.update()

# ----- Main ----------------------------------------
def main():
    run = True
    clock = pg.time.Clock()

    rectList = []
    textList = []
    
    scoreController = ScoreController(0,WIN_CONDITION)
    winFlag = False

    rect = pg.Rect(50,50,100,100)
    rectList.append(rect)

    scoreText = "Your score: 0"
    missText = "You missed: 0"

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
            if event.type == pg.MOUSEBUTTONDOWN and not winFlag:
                print("Clicked once, winFlag = " + str(winFlag))
                if (
                    (pg.mouse.get_pos()[0] >= rect.x)
                and (pg.mouse.get_pos()[0] <= rect.x + rect.width)
                and (pg.mouse.get_pos()[1] >= rect.y)
                and (pg.mouse.get_pos()[1] <= rect.y + rect.width)
                    ):
                    scoreController.incrScore()
                    scoreText = "Your score: " + scoreController.toString("score")
                else:
                    scoreController.incrMiss()
                    missText = "You missed: " + scoreController.toString("miss")
            if event.type == WIN:
                run = False
                winFlag = True
                print("Won! winFlag = " + str(winFlag))
                break

        if winFlag:
            draw_winText()
            pg.time.delay(2000)
            break

        textList.append(scoreText)
        textList.append(missText)

        draw_screen(rectList,textList,scoreController)

    if winFlag:
        main()
    else:
        pg.quit()


if __name__ == '__main__':
    main()