# Name: Yusra Hassan
# Date: September 23-29, 2020
# Class: ICS3U-02
# Description: Draws a cool character with a waterfall bacground using graphic arts

# Colour Key
SKIN = [(207, 150, 70), (186, 127, 60)]
BLUE = [(149, 222, 206),(70, 176, 144), (23, 103, 138), (14, 19, 117)]
WHITE = [(242, 227, 216), (216, 220, 227), (206, 237, 214)]
GREY = [(95, 107, 97), (219, 208, 182), (184, 183, 169), (135, 153, 149), (63, 68, 77)]
MAROON = [(179, 139, 109), (173, 81, 68), (120, 50, 40)]
GREEN = [(34, 133, 110), (21, 92, 76)]
DARK_BROWN = (48, 44, 32)
PURPLE = (74, 55, 74)

# Setting up
import random
import pygame
pygame.init()
SIZE = (600, 500)
screen = pygame.display.set_mode(SIZE)
screen.fill(WHITE[1])

# Defining scenery pattern functions
def drawPond(pondColour, pondX, pondY): # creates one row
    POND_CIRC_RADIUS = 50
    pygame.draw.circle(screen, pondColour, (POND_CIRC_RADIUS * 0 + pondX, pondY), POND_CIRC_RADIUS)
    pygame.draw.circle(screen, pondColour, (POND_CIRC_RADIUS * 2 + pondX, pondY), POND_CIRC_RADIUS)
    pygame.draw.circle(screen, pondColour, (POND_CIRC_RADIUS * 4 + pondX, pondY), POND_CIRC_RADIUS)
    pygame.draw.circle(screen, pondColour, (POND_CIRC_RADIUS * 6 + pondX, pondY), POND_CIRC_RADIUS)
    pygame.draw.circle(screen, pondColour, (POND_CIRC_RADIUS * 8 + pondX, pondY), POND_CIRC_RADIUS)
    pygame.draw.circle(screen, pondColour, (POND_CIRC_RADIUS * 10 + pondX, pondY), POND_CIRC_RADIUS)
    pygame.draw.circle(screen, pondColour, (POND_CIRC_RADIUS * 12 + pondX, pondY), POND_CIRC_RADIUS)
    pygame.draw.line(screen, WHITE[1], (0, pondY - 10), (600, pondY - 10), 3)
    pygame.draw.line(screen, WHITE[1], (0, pondY - 20), (600, pondY - 20), 3)
    pygame.draw.line(screen, WHITE[1], (0, pondY - 40), (600, pondY - 40), 3)    

def drawWaterfall(waterX): # creates one column
    FALL_SIZE = 30
    pygame.draw.line(screen, BLUE[0], (waterX, 0), (waterX, 270), 4)
    pygame.draw.line(screen, BLUE[0], (waterX, 1 * FALL_SIZE), (waterX + 30, 0), 4)
    pygame.draw.line(screen, BLUE[1], (waterX, 1 * FALL_SIZE), (waterX - 30, 0), 4)
    pygame.draw.line(screen, BLUE[1], (waterX, 2 * FALL_SIZE), (waterX + 30, FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[0], (waterX, 2 * FALL_SIZE), (waterX - 30, FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[2], (waterX, 3 * FALL_SIZE), (waterX + 30, 2 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[1], (waterX, 3 * FALL_SIZE), (waterX - 30, 2 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[0], (waterX, 4 * FALL_SIZE), (waterX + 30, 3 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[3], (waterX, 4 * FALL_SIZE), (waterX - 30, 3 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[2], (waterX, 5 * FALL_SIZE), (waterX + 30, 4 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[1], (waterX, 5 * FALL_SIZE), (waterX - 30, 4 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[2], (waterX, 6 * FALL_SIZE), (waterX + 30, 5 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[3], (waterX, 6 * FALL_SIZE), (waterX - 30, 5 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[1], (waterX, 7 * FALL_SIZE), (waterX + 30, 6 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[2], (waterX, 7 * FALL_SIZE), (waterX - 30, 6 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[3], (waterX, 8 * FALL_SIZE), (waterX + 30, 7 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[2], (waterX, 8 * FALL_SIZE), (waterX - 30, 7 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[3], (waterX, 9 * FALL_SIZE), (waterX + 30, 8 * FALL_SIZE), 4)
    pygame.draw.line(screen, BLUE[3], (waterX, 9 * FALL_SIZE), (waterX - 30, 8 * FALL_SIZE), 4)    

def drawStoneGroup(): # creates one cluster
    STONE_XY = 50 
    STONE_R1 = 20
    STONE_R2 = 40
    pygame.draw.circle(screen, GREY[random.randrange(1, 5)], (random.randrange(STONE_XY * 0, STONE_XY * 1), random.randrange(10, 230)), random.randrange(STONE_R1, STONE_R2))
    pygame.draw.circle(screen, GREY[random.randrange(1, 5)], (random.randrange(STONE_XY * 1, STONE_XY * 2), random.randrange(10, 230)), random.randrange(STONE_R1, STONE_R2))
    pygame.draw.circle(screen, GREY[random.randrange(1, 5)], (random.randrange(STONE_XY * 2, STONE_XY * 3), random.randrange(10, 250)), random.randrange(STONE_R1, STONE_R2))
    pygame.draw.circle(screen, GREY[random.randrange(1, 5)], (random.randrange(STONE_XY * 3, STONE_XY * 4), random.randrange(10, 230)), random.randrange(STONE_R1, STONE_R2))
    pygame.draw.circle(screen, GREY[random.randrange(1, 5)], (random.randrange(STONE_XY * 8, STONE_XY * 9), random.randrange(10, 230)), random.randrange(STONE_R1, STONE_R2))
    pygame.draw.circle(screen, GREY[random.randrange(1, 5)], (random.randrange(STONE_XY * 9, STONE_XY * 10), random.randrange(10, 230)), random.randrange(STONE_R1, STONE_R2))
    pygame.draw.circle(screen, GREY[random.randrange(1, 5)], (random.randrange(STONE_XY * 10, STONE_XY * 11), random.randrange(10, 230)), random.randrange(STONE_R1, STONE_R2))
    pygame.draw.circle(screen, GREY[random.randrange(1, 5)], (random.randrange(STONE_XY * 11, STONE_XY * 12), random.randrange(10, 230)), random.randrange(STONE_R1, STONE_R2))

def drawCirclesFoam(foamX, foamY): # creates one circle
    FOAM_COLOUR = random.randrange(0, 3)
    CIRCLE_BACK = (250, 246, 200)
    pygame.draw.circle(screen, WHITE[FOAM_COLOUR], (foamX,foamY), 30)
    pygame.draw.circle(screen, CIRCLE_BACK, (foamX,foamY), 30, 3)
    pygame.draw.circle(screen, WHITE[FOAM_COLOUR], (foamX,foamY), 20)
    pygame.draw.circle(screen, CIRCLE_BACK, (foamX,foamY), 20, 3)
    pygame.draw.circle(screen, WHITE[FOAM_COLOUR], (foamX,foamY), 10)
    pygame.draw.circle(screen, CIRCLE_BACK, (foamX,foamY), 10, 3)

# Drawing background scenery
pygame.draw.rect(screen, GREY[0], (0, 0, 170, 270))# background for rock wall
pygame.draw.rect(screen, GREY[0], (420, 0, 600, 270))# background for rock wall
drawPond(BLUE[0], -50, 350)
drawPond(BLUE[1], 0, 400)
drawPond(BLUE[2], -50, 450)
drawPond(BLUE[3], 0, 500)
drawWaterfall(200)
drawWaterfall(260)
drawWaterfall(320)
drawWaterfall(380)
drawStoneGroup()
drawStoneGroup()
drawStoneGroup()
drawStoneGroup()
drawStoneGroup()
drawStoneGroup()
drawStoneGroup()
drawStoneGroup()
drawStoneGroup()
drawStoneGroup()
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325)) # x24
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
drawCirclesFoam(random.randrange(0, 25), random.randrange(250, 300)) # sides = x6 each
drawCirclesFoam(random.randrange(450, 475), random.randrange(250, 300)) 
drawCirclesFoam(random.randrange(25, 50), random.randrange(250, 300))
drawCirclesFoam(random.randrange(475, 500), random.randrange(250, 300))
drawCirclesFoam(random.randrange(50, 75), random.randrange(250, 300))
drawCirclesFoam(random.randrange(500, 525), random.randrange(250, 300))
drawCirclesFoam(random.randrange(75, 100), random.randrange(250, 300))
drawCirclesFoam(random.randrange(525, 550), random.randrange(250, 300))
drawCirclesFoam(random.randrange(100, 125), random.randrange(250, 300))
drawCirclesFoam(random.randrange(525, 575), random.randrange(250, 300))
drawCirclesFoam(random.randrange(125, 150), random.randrange(250, 300))
drawCirclesFoam(random.randrange(575, 600), random.randrange(250, 300))

# Drawing the basic character body **Linked to the same x and y variables for ease with adjustment
x = 415
y = 15
# dress
pygame.draw.polygon(screen, MAROON[0], ((x - 60, y + 130), (x + 70, y + 130), (x + 50, y + 240), (x + 130, y + 500), (x - 120, y + 500), (x - 40, y + 240)))
pygame.draw.polygon(screen, GREY[0], ((x - 28, y + 240), (x - 32, y + 240), (x - 100, y + 500), (x - 60, y + 500))) # 3 creases -> ->
pygame.draw.polygon(screen, GREY[0], ((x + 8, y + 240), (x + 2, y + 240), (x - 30, y + 500), (x + 30, y + 500)))
pygame.draw.polygon(screen, GREY[0], ((x + 38, y + 240), (x + 32, y + 240), (x + 70, y + 500), (x + 110, y + 500)))
pygame.draw.rect(screen, PURPLE, (x - 40, y + 240, 90, 10)) # belt
# left arm
pygame.draw.line(screen, MAROON[0], (x - 150, y + 210), (x - 55, y + 145), 35)
pygame.draw.line(screen, MAROON[0], (x - 150, y + 210), (x - 220, y + 170), 30)
# right arm
pygame.draw.line(screen, MAROON[0], (x + 60, y + 130), (x + 75, y + 245), 30)
pygame.draw.circle(screen, MAROON[0], (x + 75, y + 245), 15)
# scarf
pygame.draw.circle(screen, MAROON[2], (x, y + 65), 75)
pygame.draw.polygon(screen, MAROON[2], ((x - 60, y + 150), (x - 30, y + 220), (x + 35, y + 220), (x + 80, y + 130), (x + 55, y + 50)))
pygame.draw.line(screen, MAROON[1], (x - 40, y + 130), (x + 40, y + 100), 5)
pygame.draw.arc(screen, MAROON[1], pygame.Rect(x - 50, y + 100, 120, 50), 4, 0, 5)
pygame.draw.arc(screen, MAROON[1], pygame.Rect(x - 30, y + 115, 90, 70), 3, -1, 5)
pygame.draw.arc(screen, MAROON[1], pygame.Rect(x - 60, y, 140, 140), 3, 4, 5)

# Drawing the face
pygame.draw.polygon(screen, SKIN[0], ((x - 50, y + 50), (x, y + 10), (x + 50, y + 50), (x + 30, y + 100), (x, y + 120), (x - 30, y + 100)))
# eye on left
pygame.draw.arc(screen, DARK_BROWN, pygame.Rect(x - 40, y + 30, 30, 20), 1, -3, 3)
pygame.draw.ellipse(screen, DARK_BROWN, pygame.Rect(x - 42, y + 40, 30, 35))
pygame.draw.ellipse(screen, WHITE[0], pygame.Rect(x - 40, y + 45, 25, 30))
pygame.draw.ellipse(screen, SKIN[0], pygame.Rect(x - 40, y + 60, 30, 25))
pygame.draw.circle(screen, DARK_BROWN, (x - 28, y + 55), 10)
pygame.draw.arc(screen, DARK_BROWN, (x - 50, y + 40, 15, 10), -3, 0, 3)
pygame.draw.arc(screen, DARK_BROWN, (x - 60, y + 45, 20, 10), -3, 0, 3)
# eye on right
pygame.draw.arc(screen, DARK_BROWN, pygame.Rect(x + 10, y + 20, 30, 20), 0, 2, 3)
pygame.draw.ellipse(screen, DARK_BROWN, pygame.Rect(x + 13, y + 40, 30, 35))
pygame.draw.ellipse(screen, WHITE[0], pygame.Rect(x + 15, y + 45, 25, 30))
pygame.draw.ellipse(screen, SKIN[0], pygame.Rect(x + 10, y + 60, 30, 25))
pygame.draw.circle(screen, DARK_BROWN, (x + 27, y + 55), 10)
pygame.draw.arc(screen, DARK_BROWN, (x + 35, y + 40, 15, 10), -3, 0, 3)
pygame.draw.arc(screen, DARK_BROWN, (x + 40, y + 45, 20, 10), -3, 0, 3)
# glasses
pygame.draw.rect(screen, PURPLE, (x - 45, y + 40, 40, 30), 4)
pygame.draw.rect(screen, PURPLE, (x + 5, y + 40, 40, 30), 4)
pygame.draw.line(screen, PURPLE, (x - 5, y + 45), (x + 5, y + 45), 4)
# nose and mouth
pygame.draw.ellipse(screen, SKIN[1], pygame.Rect(x - 5, y + 75, 15, 5))
pygame.draw.polygon(screen, WHITE[0], ((x - 10, y + 95), (x, y + 103), (x + 10, y + 105), (x + 20, y + 90)))
pygame.draw.polygon(screen, MAROON[2], ((x - 10, y + 95), (x, y + 103), (x + 10, y + 105), (x + 20, y + 90)), 4)

# Drawing the painting frame
pygame.draw.rect(screen, DARK_BROWN, (x - 220, y + 130, 220, 240), 15)
pygame.draw.rect(screen, GREY[3], (x - 220, y + 130, 220, 240), 2)

# Drawing the hands
pygame.draw.line(screen, MAROON[0], (x + 75, y + 245), (x + 10, y + 215), 30) # part of right arm that needs to go on top
pygame.draw.rect(screen, SKIN[0], (x - 235, y + 155, 25, 25))
pygame.draw.rect(screen, SKIN[1], (x - 235, y + 155, 25, 25), 3)
pygame.draw.rect(screen, SKIN[0], (x - 10, y + 200, 25, 25))
pygame.draw.rect(screen, SKIN[1], (x - 10, y + 200, 25, 25), 3)
pygame.display.flip()
pygame.time.wait(10000)

# Creating an animation ending
def drawLeaf():
    LEAF_X = random.randrange(0, 600)
    LEAF_Y = random.randrange(-100, 300)
    LEAF_WIDTH = 15
    pygame.draw.line(screen, GREEN[1], (LEAF_X, LEAF_Y + 25), (LEAF_X, LEAF_Y + 330), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[1], (LEAF_X - 90, LEAF_Y + 180), (LEAF_X, LEAF_Y + 300), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[1], (LEAF_X - 70, LEAF_Y + 140), (LEAF_X, LEAF_Y + 250), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[1], (LEAF_X - 50, LEAF_Y + 100), (LEAF_X, LEAF_Y + 200), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[1], (LEAF_X - 30, LEAF_Y + 60), (LEAF_X, LEAF_Y + 150), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[1], (LEAF_X, LEAF_Y + 300), (LEAF_X + 90, LEAF_Y + 180), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[1], (LEAF_X, LEAF_Y + 250), (LEAF_X + 70, LEAF_Y + 140), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[1], (LEAF_X, LEAF_Y + 200), (LEAF_X + 50, LEAF_Y + 100), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[1], (LEAF_X, LEAF_Y + 150), (LEAF_X + 30, LEAF_Y + 60), LEAF_WIDTH)
    LEAF_WIDTH = 2
    pygame.draw.line(screen, GREEN[0], (LEAF_X, LEAF_Y + 25), (LEAF_X, LEAF_Y + 330), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[0], (LEAF_X - 90, LEAF_Y + 180), (LEAF_X, LEAF_Y + 300), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[0], (LEAF_X - 70, LEAF_Y + 140), (LEAF_X, LEAF_Y + 250), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[0], (LEAF_X - 50, LEAF_Y + 100), (LEAF_X, LEAF_Y + 200), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[0], (LEAF_X - 30, LEAF_Y + 60), (LEAF_X, LEAF_Y + 150), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[0], (LEAF_X, LEAF_Y + 300), (LEAF_X + 90, LEAF_Y + 180), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[0], (LEAF_X, LEAF_Y + 250), (LEAF_X + 70, LEAF_Y + 140), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[0], (LEAF_X, LEAF_Y + 200), (LEAF_X + 50, LEAF_Y + 100), LEAF_WIDTH)
    pygame.draw.line(screen, GREEN[0], (LEAF_X, LEAF_Y + 150), (LEAF_X + 30, LEAF_Y + 60), LEAF_WIDTH)
    
    pygame.display.flip()
    pygame.time.wait(200)
pygame.time.wait(200) # some extra waits so that the animation will gradually pick up speed
pygame.time.wait(200)
drawLeaf()
pygame.time.wait(200)
pygame.time.wait(200)
pygame.time.wait(200)
drawLeaf()
pygame.time.wait(200)
pygame.time.wait(200)
drawLeaf()
pygame.time.wait(200)
pygame.time.wait(200)
drawLeaf()
pygame.time.wait(200)
drawLeaf()
pygame.time.wait(200)
drawLeaf() # after this point, there are 35 drawLeaf() function calls
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
drawLeaf()
screen.fill(GREEN[1])

# Ending the game
letterX = 140
letterY = 145
pygame.draw.rect(screen, GREEN[0], (letterX, letterY, 20, 200))
pygame.draw.rect(screen, GREEN[0], (letterX, letterY, 100, 20))
pygame.draw.rect(screen, GREEN[0], (letterX, letterY + 90, 50, 20))
pygame.draw.rect(screen, GREEN[0], (letterX, letterY + 180, 100, 20))
pygame.draw.rect(screen, GREEN[0], (letterX + 120, letterY, 20, 200))
pygame.draw.rect(screen, GREEN[0], (letterX + 220, letterY, 20, 200))
pygame.draw.rect(screen, GREEN[0], (letterX + 270, letterY, 20, 200))
pygame.draw.line(screen, GREEN[0], (letterX + 130, letterY), (letterX + 230, letterY + 200), 20)
pygame.draw.arc(screen, GREEN[0], (letterX + 250, letterY, 100, 200), -2, 2, 20)

pygame.display.flip()
pygame.time.wait(2000)
pygame.quit()