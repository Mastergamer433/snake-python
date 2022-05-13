import pygame
pygame.init()
class Peice:
    def __init__(self,x,y,CELL_SIZE):
        self.CELL_SIZE = CELL_SIZE
        self.x=x
        self.y=y
        self.rect=pygame.Rect(self.x*CELL_SIZE,self.y*CELL_SIZE,CELL_SIZE,CELL_SIZE) 
    def setRect(self):
        self.rect.x = self.x * self.CELL_SIZE
        self.rect.y = self.y * self.CELL_SIZE
