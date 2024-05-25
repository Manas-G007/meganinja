import pygame as pyg
import numpy as np
from gameObject import GameObj
from text import Text
from time import sleep

pyg.init()
disp=pyg.display

# screen config
screenSize=500,700
screen=disp.set_mode(screenSize)
icon=pyg.image.load("assets/ninja.jpg")
disp.set_icon(icon)
disp.set_caption("ninja")
bg=GameObj("assets/bg.png",0,0,0,0,0)

running=True
score=0
black=0,0,0
counter=10

# game object
playerSize=64
player=GameObj("assets/player.png",
               int(screenSize[0]/2)
               ,screenSize[1]-2*playerSize,0.6,-0.6,1)

# obstacle
obstacles=[]

for i in range(2):
    obstacles.append(
        GameObj("assets/obstacle.png",
                        -10 if i%2==0 else screenSize[0]-290
                        ,i*-500,0.3,0,0.3)
    )

for id,obstacle in enumerate(obstacles):
        if id%2!=0:
            obstacle.gameObj=pyg.transform.flip(obstacle.gameObj,True,False)

# hit
collide=False

def isHit():
    global collide
    for id,obstacle in enumerate(obstacles):
        if id%2==0:
            if obstacle.y+60>player.y and obstacle.x+200>player.x:
                collide=True
        else:
            if obstacle.y+60>player.y and obstacle.x+100<player.x<screenSize[0]:
                collide=True

def boundaryPlayer():
    if player.x<0:
            player.speedX=0
            player.dir=False
        
    if player.x>screenSize[0]-playerSize:
        player.speedX=0
        player.dir=True

def flipPlayer():
    player.gameObj=pyg.transform.flip(player.gameObj,True,False)

def resetObstacle():
    global score
    for obstacle in obstacles:
        if obstacle.y>screenSize[1]:
            score+=10
            obstacle.posY(0)
# render
def renderPlayer():
    screen.blit(player.gameObj,(player.x,player.y))

def renderBg():
    bg.gameObj = pyg.transform.scale(bg.gameObj,screenSize)
    screen.blit(bg.gameObj,(bg.x,bg.y),)

def renderObstacle():
    for obstacle in obstacles:
        obstacle.gameObj=pyg.transform.scale(obstacle.gameObj,(300,90))
        screen.blit(obstacle.gameObj,(obstacle.x,obstacle.y))

def renderScore():
    screen.blit(Text(f"Score : {score}",black).text,(screenSize[0]/2 - 80, 20))
    
def renderGameOver(timer):
    screen.blit(Text("Game Over",black).text,(screenSize[0]/2 - 120,screenSize[1]/2 - 50))
    screen.blit(Text(f"Restart in {timer} ...",black).text,(screenSize[0]/2 - 120,screenSize[1]/2))

def resetGame():
    global score,timer,collide,obstacles
    score=0
    timer=10
    collide=False
    obstacles.clear()
    for i in range(2):
        obstacles.append(
            GameObj("assets/obstacle.png",
                            -10 if i%2==0 else screenSize[0]-290
                            ,i*-500,0.3,0,0.3)
        )

    for id,obstacle in enumerate(obstacles):
        if id%2!=0:
            obstacle.gameObj=pyg.transform.flip(obstacle.gameObj,True,False)


# Each frame update
def update():
    global running,counter
    for event in pyg.event.get():
        # event handling
        if event.type==pyg.QUIT:
            running=False
        if event.type==pyg.KEYDOWN:
            if event.key==pyg.K_SPACE:
                if player.x<0 or player.x>screenSize[0]-playerSize:
                    flipPlayer()
                if player.dir:
                    player.setSpeedX(-player.speedVal)
                else:
                    player.setSpeedX(player.speedVal)            

    # live movement
    player.posX(player.x+player.speedX)
    for obstacle in obstacles:
        obstacle.posY(obstacle.y+obstacle.speedY)

    # boundary
    boundaryPlayer()
    resetObstacle()

    # hit
    isHit()

    if collide:
        renderBg()
        if counter==0:
            resetGame()
        else:
            counter-=1
            sleep(1)
            renderGameOver(counter)
    else:
        renderBg()
        renderObstacle()
        renderPlayer()
        renderScore()
    
    disp.update()

def main():
    while running:
        update()

if __name__=="__main__":
    main()