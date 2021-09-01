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
WHITE = (255,255,255)
BLUE = (5,40,240)

# ----- Fonts ---------------------------------------

CLICKED_FONT = pg.font.SysFont("arial",40)

# ----- Gameplay ------------------------------------
FPS = 60

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

class Bool:
    def __init__(self,data):
        self.data = data
    
    def get(self):
        return self.data
    
    def set(self,data):
        self.data = data

# ----- Functions -----------------------------------

# ---------- Handlers -------------

# ---------- Draw -----------------

def draw_screen(rect: pg.Rect, mustMove: Bool, textList, textTimer: Timer):
    SCREEN.fill(WHITE)

    if mustMove.get() == False:
        pg.draw.rect(SCREEN,BLUE,rect)
    else:
        rect.x = random.randrange(0, WIDTH -  rect.width - 50)
        rect.y = random.randrange(0, HEIGHT -  rect.height - 50)
        pg.draw.rect(SCREEN,BLUE,rect)
        mustMove.set(False)

    i = 0

    for text in textList:
        SCREEN.blit(CLICKED_FONT.render(text,1,BLACK),(50,50 + i))
        i += 50
    
    if textList:
        timerCounter = CLICKED_FONT.render(str(textTimer.getTimer()),1,BLACK)
        SCREEN.blit(timerCounter,(WIDTH - timerCounter.get_width() - 20,50))
    else:
        textTimer.setTo(textTimer.getTimer(),False)

    if textTimer.getTimer() == 0 and textList:
        textList.remove(textList[0])

        textTimer.setTo(FPS,True)

    pg.display.update()

def draw_text():
    print("You clicked")
    text = CLICKED_FONT.render("You clicked",1,BLACK)

    location = (50,50)

    SCREEN.blit(text,location)

    pg.time.delay(5000)

# ----- Main ----------------------------------------
def main():
    run = True
    clock = pg.time.Clock()

    rect = pg.Rect(250,250,200,200)
    textList = []

    textTimer = Timer(0,False)
    mustMove = Bool(False)

    while run:
        if textList:
            textTimer.decreaseBy(1)
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                if (pg.mouse.get_pos()[0] >= rect.x and pg.mouse.get_pos()[0] <= rect.x + rect.width and 
                pg.mouse.get_pos()[1] >= rect.y and pg.mouse.get_pos()[1] <= rect.y + rect.height):
                    #draw_text()
                    textList.append("You clicked")
                    textTimer.setTo(FPS,True)
                    mustMove.set(True)



        draw_screen(rect,mustMove,textList,textTimer)

    pg.quit()


if __name__ == '__main__':
    main()