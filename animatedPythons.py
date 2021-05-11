# Name: Yusra Hassan
# Date: Oct. 1, 2020
# Description: A simple animation of pythons slithering across the screen

# Colour Key
DARK_GREEN = (33, 87, 22)
GREEN = (156, 204, 51)
RED = (171, 46, 46)
NAVY = (14, 31, 66)

# Starts-up pygame
import pygame
pygame.init()
SIZE = (600, 600)
screen = pygame.display.set_mode(SIZE)
screen.fill(NAVY)

# Draws a python going left and a python going right
def drawPythonRight(snakeX, snakeY):
    pygame.draw.rect(screen, GREEN, (snakeX, snakeY, 450, 40))
    pygame.draw.circle(screen, GREEN, (snakeX, snakeY + 20), 20)
    pygame.draw.polygon(screen, GREEN, ((snakeX + 460, snakeY - 10), (snakeX + 520, snakeY + 20), (snakeX + 460, snakeY + 50), (snakeX + 400, snakeY + 20)))
    pygame.draw.rect(screen, RED, (snakeX + 510, snakeY + 15, 40, 10))
    for counter in range(45):
        pygame.draw.line(screen, DARK_GREEN, (counter * 10 + snakeX, snakeY), (counter * 10 + snakeX - 10, snakeY + 40), 3)
        pygame.draw.line(screen, DARK_GREEN, (counter * 10 + snakeX, snakeY), (counter * 10 + snakeX, snakeY + 40), 3)    
def drawPythonLeft(snakeX, snakeY):
    pygame.draw.rect(screen, GREEN, (snakeX, snakeY, 450, 40))
    pygame.draw.circle(screen, GREEN, (snakeX + 450, snakeY + 20), 20)
    pygame.draw.polygon(screen, GREEN, ((snakeX - 20, snakeY - 10), (snakeX + 35, snakeY + 20), (snakeX +- 20, snakeY + 50), (snakeX - 80, snakeY + 20)))
    pygame.draw.rect(screen, RED, (snakeX - 110, snakeY + 15, 40, 10))
    for counter in range(45):
        pygame.draw.line(screen, DARK_GREEN, (counter * 10 + snakeX, snakeY), (counter * 10 + snakeX + 10, snakeY + 40), 3)
        pygame.draw.line(screen, DARK_GREEN, (counter * 10 + snakeX, snakeY), (counter * 10 + snakeX, snakeY + 40), 3)

    
for repeat in range(6): # repeats snakes moving 6 times in each direction
    for right in range(600): # simulates movement to the right
        screen.fill(NAVY)
        drawPythonRight(2 * right - 500, repeat * 100)
        pygame.display.flip()
        pygame.time.wait(5)
    for left in range(600, 0, -1): # simulates movement to the left
        screen.fill(NAVY)
        drawPythonLeft(2 * left - 500, repeat * 100 + 50)
        pygame.display.flip()
        pygame.time.wait(5)  

pygame.quit()

