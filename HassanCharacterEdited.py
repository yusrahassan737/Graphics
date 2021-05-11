# Name: Yusra Hassan
# Date: Edited: Dec.6-7, 2020 (First Written: September 23-29, 2020)
# Class: None - Personal Project
# Description: Draws a cool character with a waterfall bacground using graphic arts
# Purpose: Editing an old class project for efficiency/clarity of code

#***Will probably need to fix commenting

# Setting up
import random, pygame
pygame.init()
SIZE = (600, 500)
screen = pygame.display.set_mode(SIZE)

# Colour Key
SKIN = [(207, 150, 70), (186, 127, 60)]
blue = [(149, 222, 206),(70, 176, 144), (23, 103, 138), (14, 19, 117)]
white = [(242, 227, 216), (216, 220, 227), (206, 237, 214)]
grey = [(95, 107, 97), (219, 208, 182), (184, 183, 169), (135, 153, 149), (63, 68, 77)]
MAROON = [(179, 139, 109), (173, 81, 68), (120, 50, 40)]
green = [(21, 92, 76), (34, 133, 110)]
DARK_BROWN = (48, 44, 32)
PURPLE = (74, 55, 74)

# Other
running = True
stonesInfo = []
for i in range(50):
    stonesInfo.append((random.randint(1, 4), random.randint(0, 160), random.randint(10, 230), random.randint(10, 230), random.randint(20, 40)))
pondXPos = 0
leavesPos = []
for i in range(150):
    leavesPos.append((random.randint(0, SIZE[0]), random.randint(0, SIZE[1])))
lightText = pygame.font.SysFont("Corbel", 30)

# Defining scenery pattern functions
def drawPond(pondX, pondY): # creates one row
    global screen, blue, white, pondXPos
    
    for h in range(4):
        if h % 2 == 0: # creates zigzag pattern with the xPos
            for i in range(8):
                pygame.draw.circle(screen, blue[h], (100 * i + pondX - 50, pondY + h * 50), 50)
            for i in (1, 2, 4):
                pygame.draw.line(screen, white[1], (0, pondY - (10 * i) + (h * 50)), (600, pondY - (10 * i) + (h * 50)), 3)            
        else:
            for i in range(8):
                pygame.draw.circle(screen, blue[h], (100 * i + pondX, pondY + (h * 50)), 50)
            for i in (1, 2, 4):
                pygame.draw.line(screen, white[1], (0, pondY - (10 * i) + (h * 50)), (600, pondY - (10 * i) + (h * 50)), 3)
    
    if pondXPos < 50:
        pondXPos += 5
    else:
        pondXPos = -50

def drawWaterfall(waterX): # creates one column
    global screen
    FALL_SIZE = 30
    
    for i in range(4):
        pygame.draw.line(screen, blue[random.randint(0, 2)], (waterX + (i * 60), 0), (waterX + (i * 60), 270), 4) # vertical line
        for j in range(10):
            pygame.draw.line(screen, blue[random.randint(0, 2)], (waterX + (i * 60), j * FALL_SIZE), (waterX + 30 + (i * 60), (j - 1) * FALL_SIZE), 4)
            pygame.draw.line(screen, blue[random.randint(0, 2)], (waterX + (i * 60), j * FALL_SIZE), (waterX - 30 + (i * 60), (j - 1) * FALL_SIZE), 4)

def drawStone(greyShade, stoneX, stoneY1, stoneY2, stoneSize): # creates one stone
    global screen, grey
    pygame.draw.circle(screen, grey[greyShade], (stoneX, stoneY1), stoneSize)
    pygame.draw.circle(screen, grey[greyShade], (stoneX + 440, stoneY2), stoneSize)

def drawCirclesFoam(foamX, foamY): # creates one circle
    global screen
    FOAM_COLOUR = random.randrange(0, 3)
    CIRCLE_BACK = (250, 246, 200)
    for i in range(3, 0, -1):
        pygame.draw.circle(screen, white[FOAM_COLOUR], (foamX,foamY), i * 10)
        pygame.draw.circle(screen, CIRCLE_BACK, (foamX,foamY), i * 10, 3)

def drawCharacter(x, y):

    # dress
    pygame.draw.polygon(screen, MAROON[0], ((x - 60, y + 130), (x + 70, y + 130), (x + 50, y + 240), (x + 130, y + 500), (x - 120, y + 500), (x - 40, y + 240)))
    pygame.draw.polygon(screen, grey[0], ((x - 28, y + 240), (x - 32, y + 240), (x - 100, y + 500), (x - 60, y + 500))) # 3 creases -> ->
    pygame.draw.polygon(screen, grey[0], ((x + 8, y + 240), (x + 2, y + 240), (x - 30, y + 500), (x + 30, y + 500)))
    pygame.draw.polygon(screen, grey[0], ((x + 38, y + 240), (x + 32, y + 240), (x + 70, y + 500), (x + 110, y + 500)))
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
    pygame.draw.ellipse(screen, white[0], pygame.Rect(x - 40, y + 45, 25, 30))
    pygame.draw.ellipse(screen, SKIN[0], pygame.Rect(x - 40, y + 60, 30, 25))
    pygame.draw.circle(screen, DARK_BROWN, (x - 28, y + 55), 10)
    pygame.draw.arc(screen, DARK_BROWN, (x - 50, y + 40, 15, 10), -3, 0, 3)
    pygame.draw.arc(screen, DARK_BROWN, (x - 60, y + 45, 20, 10), -3, 0, 3)
    # eye on right
    pygame.draw.arc(screen, DARK_BROWN, pygame.Rect(x + 10, y + 20, 30, 20), 0, 2, 3)
    pygame.draw.ellipse(screen, DARK_BROWN, pygame.Rect(x + 13, y + 40, 30, 35))
    pygame.draw.ellipse(screen, white[0], pygame.Rect(x + 15, y + 45, 25, 30))
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
    pygame.draw.polygon(screen, white[0], ((x - 10, y + 95), (x, y + 103), (x + 10, y + 105), (x + 20, y + 90)))
    pygame.draw.polygon(screen, MAROON[2], ((x - 10, y + 95), (x, y + 103), (x + 10, y + 105), (x + 20, y + 90)), 4)
    
    # Drawing the painting frame
    pygame.draw.rect(screen, DARK_BROWN, (x - 220, y + 130, 220, 240), 15)
    pygame.draw.rect(screen, grey[3], (x - 220, y + 130, 220, 240), 2)
    
    # Drawing the hands
    pygame.draw.line(screen, MAROON[0], (x + 75, y + 245), (x + 10, y + 215), 30) # part of right arm that needs to go on top
    pygame.draw.rect(screen, SKIN[0], (x - 235, y + 155, 25, 25))
    pygame.draw.rect(screen, SKIN[1], (x - 235, y + 155, 25, 25), 3)
    pygame.draw.rect(screen, SKIN[0], (x - 10, y + 200, 25, 25))
    pygame.draw.rect(screen, SKIN[1], (x - 10, y + 200, 25, 25), 3)

def drawLeaf(leafX, leafY): # Draws a leaf
    global screen, green
    leafLineW = (15, 2)
    for i in range(2):
        pygame.draw.line(screen, green[i], (leafX, leafY - 155), (leafX, leafY + 155), leafLineW[i])
        for j in range(4):
            pygame.draw.line(screen, green[i], (leafX - (90 - 20 * j), leafY + (5 - j * 40)), (leafX, leafY + (125 - j * 50)), leafLineW[i])
            pygame.draw.line(screen, green[i], (leafX, leafY + (125 - j * 50)), (leafX + (90 - 20 * j), leafY + (5 - j * 40)), leafLineW[i])

# Drawing background scenery
while running:
    for evnt in pygame.event.get(): # Close pygame if the user presses the X
        if evnt.type == pygame.QUIT:
            running = False
    screen.fill(white[1])
    
    # waterfall
    drawWaterfall(200)
    
    # rock walls
    pygame.draw.rect(screen, grey[0], (0, 0, 170, 270)) # background for left rock wall
    pygame.draw.rect(screen, grey[0], (420, 0, 600, 270)) # background for right rock wall
    for i in stonesInfo:
        drawStone(i[0], i[1], i[2], i[3], i[4])
    
    # pond
    drawPond(pondXPos, 350)
    
    # Water foam
    for i in range(24):
        drawCirclesFoam(random.randrange(150, 420), random.randrange(230, 325))
        if i % 4 == 0:
            drawCirclesFoam(random.randrange(25 * i, 25 * (i + 1)), random.randrange(250, 300))
            drawCirclesFoam(random.randrange(450 + i * 25, 475 + (i * 25 + 1)), random.randrange(250, 300)) 
    
    # leaves covering
    for i in range(len(leavesPos)):
        drawLeaf(leavesPos[i][0], leavesPos[i][1])
    if len(leavesPos) > 0 and pygame.mouse.get_pressed()[0] == 1:
        leavesPos.pop()
    if len(leavesPos) > 130:
        screen.blit(lightText.render("Click to remove the leaves and reveal the image", 1, white[0]), (20, 50, 100, 100))
    elif len(leavesPos) == 0 and pygame.mouse.get_pressed()[0] != 1: # don't draw the character if the mouse is pressed
        drawCharacter(415, 15) # draw the character after leaves uncovered
        
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()