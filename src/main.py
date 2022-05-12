import pygame
from snake import Snake
from apple import Apple
from peice import Peice
import time
#from color import *

pygame.init()

WIDTH,HEIGHT=300,300
GAME_SIZE=30
CELL_SIZE=WIDTH/GAME_SIZE
clock = pygame.time.Clock()
WIN=pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    done=False

    apple=Apple(CELL_SIZE,GAME_SIZE)
    snake=Snake(CELL_SIZE,GAME_SIZE)

    while done==False: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type==pygame.KEYDOWN:
                snake.dir=event.unicode
        WIN.fill((0,0,0))
        checkResult=snake.check(apple)
        if checkResult==1:
            time.sleep(0.5)
            snake.peices.append(Peice(snake.x,snake.y,CELL_SIZE))
            snake.score+=1
            apple=Apple(CELL_SIZE,GAME_SIZE)
            print("Score:", snake.score)
        elif checkResult==2:
            snake.gameOver=True
            done=True
        snake.move()
        pygame.draw.rect(WIN,(0,200,0),snake.head)
        pygame.draw.rect(WIN,(200,0,0),apple.rect)
        for peice in snake.peices:
            pygame.draw.rect(WIN,(0,255,0),peice.rect)
        pygame.display.flip()
        clock.tick(5)
    if snake.gameOver==True:
        time.sleep(1)
        pygame.quit()
    else:
        pygame.quit
if __name__ == "__main__":
    main()
