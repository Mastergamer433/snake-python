import pygame
pygame.init()


class Snake:
    # Constructor
    def __init__(self, CELL_SIZE, GAME_SIZE):
        self.GAME_SIZE = GAME_SIZE
        self.dir = 'w'
        self.x = 20
        self.y = 10
        self.score = 0
        self.gameOver = False
        self.peices = []
        self.CELL_SIZE = CELL_SIZE
        self.head = pygame.Rect(
                            self.x*self.CELL_SIZE,
                            self.y*self.CELL_SIZE,
                            self.CELL_SIZE,
                            self.CELL_SIZE
        )

    # Move the snake and the peices
    def move(self):
        if self.x == self.GAME_SIZE:
            self.x = 0
        elif self.x == 0:
            self.x = self.GAME_SIZE+1
        if self.y == self.GAME_SIZE:
            self.y = 0
        elif self.y == 0:
            self.y = self.GAME_SIZE+1
        if self.dir == 'w':
            self.y -= 1
        elif self.dir == 's':
            self.y += 1
        elif self.dir == 'a':
            self.x -= 1
        elif self.dir == 'd':
            self.x += 1
        self.head.x = self.x*self.CELL_SIZE
        self.head.y = self.y*self.CELL_SIZE
        for i in range(len(self.peices)):
            if i == 0:
                if self.peices[i].x<self.x and self.peices[i].y<self.y:
                    self.peices[i].x = self.x+1
                    self.peices[i].y = self.y+1
                elif self.peices[i].x>self.x and self.peices[i].y>self.y:
                    self.peices[i].x= self.x-1
                    self.peices[i].y = self.y-1
            if i == 0:
                if self.peices[i].x > self.x:
                    self.peices[i].x = self.x+1
                elif self.peices[i].x < self.x:
                    self.peices[i].x = self.x-1
                if self.peices[i].y > self.y:
                    self.peices[i].y = self.y-1
                elif self.peices[i].y < self.y:
                    self.peices[i].y = self.y-1
            else:
                if self.peices[i].x > self.peices[i-1].x:
                    self.peices[i].x = self.peices[i-1].x-1
                elif self.peices[i].x < self.peices[i-1].x:
                    self.peices[i].x = self.peices[i-1].x+1
                if self.peices[i].y > self.peices[i-1].y:
                    self.peices[i].y = self.peices[i-1].y-1
                elif self.peices[i].y < self.peices[i-1].y:
                    self.peices[i].y = self.peices[i-1].y+1

    # Check if the snake collides with somthing
    def check(self, apple):
        for peice in self.peices:
            if self.x == peice.x and self.y == peice.y:
                print("collided with peice")
                print(peice.x, peice.y)
                print(self.x, self.y)
                return 2
        if self.x == apple.x and self.y == apple.y:
            return 1
