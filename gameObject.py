import pygame as pyg

class GameObj:
    def __init__(self,path,x,y,speedVal,speedX,speedY):
        self.gameObj=pyg.image.load(path)
        self.x=x
        self.y=y
        self.speedVal=speedVal
        self.speedX=speedX
        self.speedY=speedY
        self.dir=True

    def posXY(self,x,y):
        self.x,self.y=x,y

    def posX(self,x):
        self.x=x
    
    def posY(self,y):
        self.y=y

    def setSpeedX(self,speed):
        self.speedX=speed

    def setSpeedY(self,speed):
        self.speedY=speed
    