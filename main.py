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

# ----- Sprites -------------------------------------

HAMMER_W, HAMMER_H = 32,32

# ----- Sounds --------------------------------------

SWING_SFX = pg.mixer.Sound(os.path.join("Assets/Sounds","swing.ogg"))
HIT_SFX = pg.mixer.Sound(os.path.join("Assets/Sounds","bonk.ogg"))


# ----- Fonts ---------------------------------------

FONT = pg.font.SysFont("arial",15)
WIN_FONT = pg.font.SysFont("comicsans",50)

# ----- Gameplay ------------------------------------
FPS = 60

WIN_CONDITION = 5
WIN = pg.USEREVENT + 1




# ----- Classes -------------------------------------

class Timer:
    def __init__(self, time: int):
        self.time = time
    
    def decreaseBy(self,decr):
        self.time -= decr
    
    def setTo(self, time: int):
        self.time = time

    def getTime(self) -> int:
        return self.time

class Hammer:
    def __init__(self, timer: Timer = None, position: tuple = None):
        self.timer = timer
        self.position = position

    def setTimer(self, timer: Timer):
        self.timer = timer

    def setPos(self, position: tuple):
        self.position = position

    def getTimer(self) -> Timer:
        return self.timer

    def getPos(self) -> tuple:
        return self.position
    


class ScoreController:
    def __init__(self, score: int, win: int):
        self.score = score
        self.miss = 0
        self.win = win
    
    def getScore(self) -> int:
        return self.score

    def getMiss(self) -> int:
        return self.miss

    def toString(self, type: str) -> str:
        if type == "score":
            return str(self.score)
        elif type == "miss":
            return str(self.miss)

    def setScore(self, score: int):
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

def draw_screen(rectList, textList, scoreController: ScoreController, hammer: Hammer):
    # draw background
    SCREEN.fill(BLACK)

    # draw objects to click on
    [pg.draw.rect(SCREEN,GREEN,rect) for rect in rectList]  # 

    # spacing between lines of text
    text_y_displace = 0

    # draw text
    for text in textList:
        str = FONT.render(text,1,WHITE)     # this is a surface
        SCREEN.blit(str,(WIDTH//2 - str.get_width()//2, 15 + text_y_displace))
        text_y_displace += 30

    # clear list of text
    textList.clear()

    # draw hammer if clicked, automatically disappears after 20 frames
    if hammer.getTimer() != None and hammer.getTimer().getTime() != 0:
        hammerRect = pg.Rect(hammer.getPos()[0] - HAMMER_W//2, hammer.getPos()[1] - HAMMER_H//2, 
                            HAMMER_W, HAMMER_H)
        pg.draw.rect(SCREEN,YELLOW,hammerRect)
        hammer.getTimer().decreaseBy(1)

    # WIN event
    if scoreController.isWon():
        pg.event.post(pg.event.Event(WIN))

    # update display
    pg.display.update()


def draw_winText():
    str = WIN_FONT.render("You win!",1,RED)
    SCREEN.blit(str,(WIDTH//2 - str.get_width()//2, 150))

    pg.display.update()

# ----- Main ----------------------------------------

def main():
    pg.event.clear()    # clear events from last game

    run = True
    clock = pg.time.Clock()

    hammer = Hammer()

    rectList = []
    textList = []
    
    scoreController = ScoreController(0,WIN_CONDITION)
    winFlag = False

    rect = pg.Rect(50,50,100,100)
    rectList.append(rect)

    goalText = "Goal: " + str(WIN_CONDITION)
    scoreText = "Your score: 0"
    missText = "You missed: 0"

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
            if event.type == pg.MOUSEBUTTONDOWN and winFlag == False:
                # set timer and position of hammer to draw
                hammer.setTimer(Timer(20))
                hammer.setPos(pg.mouse.get_pos())   # this is CENTER of hammer

                # play swing SFX
                SWING_SFX.play()

                # check if hit or miss
                if (
                    (pg.mouse.get_pos()[0] >= rect.x)
                and (pg.mouse.get_pos()[0] <= rect.x + rect.width)
                and (pg.mouse.get_pos()[1] >= rect.y)
                and (pg.mouse.get_pos()[1] <= rect.y + rect.width)
                    ):
                    HIT_SFX.play()
                    scoreController.incrScore()
                    scoreText = "Your score: " + scoreController.toString("score")
                else:
                    scoreController.incrMiss()
                    missText = "You missed: " + scoreController.toString("miss")

            if event.type == WIN:
                run = False
                winFlag = True
                break

        if winFlag:
            draw_winText()
            pg.time.delay(2000)     # wait 2s
            break

        textList.append(goalText)
        textList.append(scoreText)
        textList.append(missText)

        draw_screen(rectList,textList,scoreController,hammer)



    if winFlag:
        main()
    else:
        pg.quit()


if __name__ == '__main__':
    main()