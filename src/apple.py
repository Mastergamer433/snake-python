import pygame
import random
pygame.init()
class Apple:
    def __init__(self,CELL_SIZE,GAME_SIZE):
        self.CELL_SIZE=CELL_SIZE
        self.GAME_SIZE=GAME_SIZE
        self.x=int(random.random()*self.GAME_SIZE)
        self.y=int(random.random()*self.GAME_SIZE)
        self.rect=pygame.Rect(
                self.x*self.CELL_SIZE,
                self.y*self.CELL_SIZE,
                self.CELL_SIZE,
                self.CELL_SIZE
        )

