# Mr.Ching example updated
# Date: Oct.22, 2020
# Class: ICS3U1-02
# Description: Draws a circle that bounces and a circle that infinitely goes down and reappears a the top (comment out)

# Start up python
import pygame
pygame.init()
SIZE = (400, 400)
screen = pygame.display.set_mode(SIZE)

# Colours
normal = (205, 83, 52)
hilight = (237, 184, 139)
bkgrd = (46, 40, 42)
ballClr = normal

# Clear the screen, draw off screen and then display
def drawScene(scrn, y):
 global ballClr
 screen.fill(bkgrd)
 pygame.draw.circle(scrn, ballClr, (200, y), 50)
 pygame.display.flip()

# Variables
running = True
myClock = pygame.time.Clock()
y = 50
up = False

# Game loop
while running:
 # Check all the events that happen
 for evnt in pygame.event.get():
  # if the user tries to close the window, then raise the "flag"
  if evnt.type == pygame.QUIT:
   running = False

 drawScene(screen, y)
 
 # Forever ball
 #if (y < 450):
  #y += 5
 #elif (y > -50):
  #y = 0
 
 # Bouncy ball
 if (y > 400):
  up = False
  ballClr = hilight
 elif (y < 0):
  up = True
  ballClr = normal
 
 if up:
  y += 5
 else:
  y -= 5
 
 # waits long enough to have 60 fps
 myClock.tick(100)

pygame.quit()