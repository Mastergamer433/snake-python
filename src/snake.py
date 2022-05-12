import pygame
pygame.init()
class Snake:
    def __init__(self,CELL_SIZE,GAME_SIZE):
        self.GAME_SIZE=GAME_SIZE
        self.dir='w'
        self.x=20
        self.y=10
        self.score=0
        self.gameOver=False
        self.peices=[]
        self.CELL_SIZE=CELL_SIZE
        self.head=pygame.Rect(
                            self.x*self.CELL_SIZE,
                            self.y*self.CELL_SIZE,
                            self.CELL_SIZE,
                            self.CELL_SIZE
        ) 
    def move(self):
        if self.x==self.GAME_SIZE:
            self.x=0
        elif self.x==0:
            self.x=GAME_SIZE+1
        if self.y==self.GAME_SIZE:
            self.y=0
        elif self.y==0:
            self.y=GAME_SIZE+1
 
        self.head.x=self.x*self.CELL_SIZE
        self.head.y=self.y*self.CELL_SIZE
        for i in range(len(self.peices)):
            if i==1:
                peices[i].x=self.x
            else:
                self.peices[i].x=self.peices[i-1].x
        if self.dir=='w':
            self.y-=1
            
        elif self.dir=='s':
            self.y+=1
        elif self.dir=='a':
            self.x-=1
        elif self.dir=='d':
            self.x+=1
    def check(self,apple):
        for peice in self.peices:
            if self.x==peice.x and self.y==peice.y:
                return 2
        if self.x==apple.x and self.y==apple.y:
            return 1
