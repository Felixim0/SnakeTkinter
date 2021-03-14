from tkinter import *
from time import sleep
from random import randint
window =Tk()
window.configure(background='black')

w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.overrideredirect(1)
window.geometry("%dx%d+0+0" % (w, h))


canvasHeight = round(h, -1)
canvasWidth = round(w, -1)
lengthOfSnake = 4
angle = "Right"


window.title("Snake Game 2.0")
canvas = Canvas(bg="black",height=canvasHeight,width=canvasWidth,highlightthickness=0)
canvas.grid(column=1,row=1,columnspan=2)

score = -1 #Starting Score (actually one less)
sleepyTime2 = 0.08 # Starting wait time
sleepyTime = sleepyTime2 # how long snake sleeps by defualt
minTime = 0.03 # How slow its allowed to go
takeTime= 0.01 # Time taken from sleepyTime every level increment

x=canvasHeight/2
y=canvasWidth/2

snakeCO = [] 
appleCO = []
appleCO2= []
completedLevels = [0]

appleOnScreen = False
game = True

def checkAppleCO():
    global appleCO
    for i in range (0,len(snakeCO)):
        if snakeCO[i] == appleCO:
            #Make new apple Co-ordinates, as the previous ones were located at a position on the snake
            appleCO = [randint(1,canvasWidth/20)*20,randint(1,canvasHeight/20)*20]
            checkAppleCO()
        else:
            return appleCO

def makeApple():
    global appleCO,appleOnScreen,snakeCO,score
    if appleOnScreen == False:
        appleCO = [randint(1,canvasWidth/20)*20,randint(1,canvasHeight/20)*20]
        appleCO = checkAppleCO()

        canvas.create_rectangle(appleCO[0]-10,appleCO[1]-10, appleCO[0]+10,appleCO[1]+10, fill="green", outline='red',width=3)
        appleOnScreen = True
        score = score + 1
    else:
        canvas.create_rectangle(appleCO[0]-10,appleCO[1]-10, appleCO[0]+10,appleCO[1]+10, fill="green", outline='red',width=3)
        
for j in range(0,lengthOfSnake):
    tempArray=[(j*20),(canvasHeight)]
    snakeCO.append(tempArray[:])

for i in range (0,len(snakeCO)):
    canvas.create_rectangle(snakeCO[i][0]-10,snakeCO[i][1]-10, snakeCO[i][0]+10,snakeCO[i][1]+10, fill="white", outline='red',width=3)

def writeSnakeToScreen(v1,v2):
    global snakeCO
    if snakeCO[len(snakeCO)-1][0] < canvasWidth-canvasWidth:
        snakeCO[len(snakeCO)-1][0] = snakeCO[len(snakeCO)-1][0] + canvasWidth+20

    elif snakeCO[len(snakeCO)-1][0] > canvasWidth:
        snakeCO[len(snakeCO)-1][0] = snakeCO[len(snakeCO)-1][0] - canvasWidth-20

    if snakeCO[len(snakeCO)-1][1] < canvasHeight-canvasHeight:
        snakeCO[len(snakeCO)-1][1] = snakeCO[len(snakeCO)-1][1] + canvasHeight+20

    elif snakeCO[len(snakeCO)-1][1] > canvasHeight:
        snakeCO[len(snakeCO)-1][1] = snakeCO[len(snakeCO)-1][1] - canvasHeight-20
        
    snakeCO.append([snakeCO[len(snakeCO)-1][0]+v1,snakeCO[len(snakeCO)-1][1]+v2])
    canvas.delete(ALL)
    for i in range (0,len(snakeCO)):
        if i == len(snakeCO)-1:
            canvas.create_rectangle(snakeCO[i][0]-10,snakeCO[i][1]-10, snakeCO[i][0]+10,snakeCO[i][1]+10, fill="white", outline='red',width=5)
        else:
            canvas.create_rectangle(snakeCO[i][0]-10,snakeCO[i][1]-10, snakeCO[i][0]+10,snakeCO[i][1]+10, fill="white", outline='red',width=3)
            
def mainProgram():
    global game, minTime
    while True:
        global x,y,snakeCO,angle,appleCO,appleOnScreen,score,sleepyTime,completedLevels,takeTime,lengthOfSnake,canvasHeight,cheat

        
        if checkIfSnakeToutchingSelf(snakeCO) == True:
            print("Game Over")
            canvas.create_text(y,x,fill="white",font=("Times 80 italic bold"),text="You Lose :(")
            
            canvas.create_text((y-y/2+((y/2)/2)),x/2,fill="white",font=("Sans 80 italic bold"),text="Score:")
            canvas.create_text((y+y/2),x/2,fill="white",font=("Sans 80 italic bold"),text=str(score))
            window.update()
            print("Attempting to restart")
            sleep(5)
            snakeCO = []
            for j in range(0,lengthOfSnake):
                tempArray=[(j*20),(canvasHeight)]
                snakeCO.append(tempArray[:])

            for i in range (0,len(snakeCO)):
                canvas.create_rectangle(snakeCO[i][0]-10,snakeCO[i][1]-10, snakeCO[i][0]+10,snakeCO[i][1]+10, fill="white", outline='red',width=3)
                
            angle = "Right"
            appleOnScreen = False

            sleepyTime = sleepyTime2
            
        else:
            if angle == "Down":
                writeSnakeToScreen(0,20)

            if angle == "Up":
                writeSnakeToScreen(0,-20)
                
            if angle == "Left":
                writeSnakeToScreen(-20,0)
                
            if angle == "Right":
                writeSnakeToScreen(20,0)

            if (snakeCO[len(snakeCO)-1] == appleCO) or (cheat == True):
                appleOnScreen = False
                cheat=False
            else:
                snakeCO.pop(0)
                
            makeApple()

            if (score % 5 == 0) and (completedLevels[len(completedLevels)-1] != score) and (sleepyTime > minTime) :
                print("LevelUp")
                completedLevels.append(score)
                sleepyTime=sleepyTime-takeTime
            
            window.update()
            sleep(sleepyTime)

def checkIfSnakeToutchingSelf(snakeCO):
    temp = snakeCO[:]
    for i in range (0,len(temp)):
        for j in range (0,len(temp)):
            if (temp[i] == temp[j]) and (i != j):
                return True

def directionUP(e):
    global angle
    if angle == "Down":
        doNothing=True
    else:
        angle = "Up"
def directionDOWN(e):
    global angle
    if angle == "Up":
        doNothing=True
    else:
        angle = "Down"
def directionLEFT(e):
    global angle
    if angle == "Right":
        doNothing=True
    else:
        angle = "Left"
def directionRIGHT(e):
    global angle
    if angle == "Left":
        doNothing=True
    else:
        angle = "Right"
def cheat(e):
    global cheat
    cheat = True
window.bind("<Up>",directionUP)
window.bind("<Down>",directionDOWN)
window.bind("<Right>",directionRIGHT)
window.bind("<Left>",directionLEFT)

window.bind("c",cheat)

mainProgram()

window.mainloop()
