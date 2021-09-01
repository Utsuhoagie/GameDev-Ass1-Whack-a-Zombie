
def timeFunc(timer: int):
    if timer == 0:
        timer = 60
    
    print(str(timer))
    timer -= 10

run = True
timer = 60

while run:
    timeFunc(timer)