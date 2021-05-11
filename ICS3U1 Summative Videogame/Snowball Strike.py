# Name: Yusra Hassan
# Date: Oct.28-Nov.9, 2020
# Class: ICS3U1-02
# Description: Enter letters to hit blocks defending a tower enough times before running out of blocks

# Start-Up
import pygame, random, math
pygame.init()
width = 600
height = 400
SIZE = (width, height)
screen = pygame.display.set_mode(SIZE)

# Variables
# Colour Key
bkgdClr = (143, 168, 196)
iceFillClr = (160, 210, 190)
iceLineClr = (170, 237, 210)
white = (227, 235, 218)
snow = (213, 235, 242)
skin = (138, 121, 94)
darkBrown = (79, 62, 36)
green = (109, 173, 130)
darkGreen = (86, 143, 104)
mauve = (173, 134, 123)

# Text
bigText = pygame.font.SysFont("Calibri", 45)
smallText = pygame.font.SysFont("Agency FB", 17)
medText = pygame.font.SysFont("Calibri", 25)

# Small snowball pile
snowballsClrs = []
snowballsPos = []
for snowball in range(15): # appends colours with same (r, b) values and different (g)
    snowballsClrs.append((180, random.randint(180, 220), 220))
    snowballsPos.append((random.randint(0, 70), random.randint(170, 220)))

# 35 Posibble words # Credit: https://www.words-to-use.com/words/winter/ for most words)
words = ["arctic", "barren", "blustery", "cozy", "crisp", "crystal", "dreary","enchanting", "extreme", "fog", "frost", "frigid", "glistening", "harsh", "holidays", "insolation", "icy", "joviality", "knitting", "leafless", "misty", "north", "numb", "opaline", "polar", "powdery", "quicksilver","recluse", "slippery", "snow", "toasty", "unending", "vast", "windy", "zero"]

# Snowflakes positions
snowflakesPos = []
for snowflake in range(10):
    snowflakesPos.append((random.randint(0, width), random.randint(0, height - 100), 100, 100))

# Key-related
VALID_ALPHA_KEYS = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z]
validNumKeys = [pygame.K_1, pygame.K_2, pygame.K_3]

# Game function
hitsToWin = 15
gameRunning = True
gameSceneRunning = False
scene = 1
mx, my = 0, 0

# A function to draw outlined shapes - works for just some basic ones
def outlineShape(scrn, shape, fillColour, lineColour, sizePosInfo, lineWidth):
    # determine shape type and draw a filled shape with an outline on top
    if shape == "rect":
        pygame.draw.rect(scrn, fillColour, sizePosInfo)
        pygame.draw.rect(scrn, lineColour, sizePosInfo, lineWidth)
    elif shape == "poly":
        pygame.draw.polygon(scrn, fillColour, sizePosInfo)
        pygame.draw.polygon(scrn, lineColour, sizePosInfo, lineWidth)
    elif shape == "elps":
        pygame.draw.ellipse(scrn, fillColour, sizePosInfo)
        pygame.draw.ellipse(scrn, lineColour, sizePosInfo, lineWidth)

def getMouseXY(): # function to find and return mousex and y
    mx, my = pygame.mouse.get_pos()
    return (mx, my)

# Function to create a button
def drawButton(scrn, btnX, btnY, text, textFormat, sceneChange, mx, my): 
    global iceFillClr, white, iceLineClr, scene # globalize necessary variables
    btnPos = pygame.Rect(btnX, btnY, 150, 50) # rect object for button
    
    if btnPos.collidepoint(mx, my): # if the mouse coordinates match up, change the text colour of the button
        pygame.draw.rect(scrn, iceFillClr, btnPos)
        scrn.blit(medText.render(text, 3, iceLineClr), (btnPos[0] + textFormat, btnPos[1] + 15, btnPos[2], btnPos[3]))
        if pygame.mouse.get_pressed()[0] == 1: # if the mouse is also pressed, change the scene number
            scene = sceneChange
    else: # if the mouse coordinates do not match up with a button, leave the text colour as white
        pygame.draw.rect(scrn, iceFillClr, btnPos)
        scrn.blit(medText.render(text, 3, white), (btnPos[0] + textFormat, btnPos[1] + 15, btnPos[2], btnPos[3]))

# Function to draw the menu
def menuScene(scrn, mx, my):
    # Initialize
    global scene, white, iceLineClr, bkgdClr, bigText, width, height
    scene = 1
    scrn.fill(bkgdClr)
    
    # Snowflake background
    for i in range(0, width, 80):
        for j in range(0, height, 80):
            screen.blit(bigText.render("*", 3, iceLineClr), (i + 5, j + 20, 5, 5))
    
    # Title
    scrn.blit(bigText.render("Snowball Strike", 3, white), (int(width / 3.5), int(height / 4), 10, 10))
    
    # Buttons
    drawButton(scrn, 220, 200, "How To Play", 15, 2, mx, my)
    drawButton(scrn, 220, 270, "Start!", 45, 3, mx, my)

# Function to draw "how to play" scene
def howToPlayScene(scrn, mx, my):
    # Initialize (variables, scene, background)
    global scene, bkgdClr, darkBrown, bigText, smallText, width, height
    scene = 2
    scrn.fill(bkgdClr)
    
    # Lines of text
    storyLineTxt = ["No tower is getting in your way. You won't be stopped by its strength... nor its icicle defense...", "nor its ability to avoid direct hits... right? Well, you've got a bunch of snowballs and blocks of snow,", "so might as well get started!"]
    instructionsTxt = ["Choose a number of rows of blocks to hit for the round by pressing a 1, 2 or 3 key. The number", "must be greater than or equal to the rows left displayed on the top right. To choose a snowball,", "press a letter key (one you haven't already pressed). Time it correctly to avoid being blocked", "by icicles. The chosen snowball will roll down the hill and crash into the icicles (a miss) or", "the blocks (hits calculated by the number of times the letter appeared in the blocks). The", "game ends when you reach " + str(hitsToWin) + " hits (a win) or when you've run out of blocks to hit (a loss)."]
    
    # Blit text to screen
    scrn.blit(bigText.render("How to Play", 3, darkBrown), (85, 30, 10, 10))
    
    for i in range(len(storyLineTxt)):
        scrn.blit(smallText.render(storyLineTxt[i], 3, darkBrown), (60, i * 25 + 100, 10, 10))
    
    scrn.blit(smallText.render("Instructions:", 3, darkBrown), (60, 200, 10, 10)) 
    for i in range(len(instructionsTxt)):
        scrn.blit(smallText.render(instructionsTxt[i], 3, darkBrown), (60, i * 25 + 225, 10, 10))
    
    # Draw a start button
    drawButton(scrn, 400, 30, "Start!", 45, 3, mx, my)

# Function to draw static parts of the game scene
def gameScene(scrn, iciclesY, armRise, flakePos, snowballX, snowballY, letter, numRows, blocked, mx, my):
    
    # Variables
    global scene, width, height, bkgdClr, iceFillClr, iceLineClr, white, snow, skin, darkBrown, green, darkGreen, mauve, snowballsClrs, snowballsPos, snowflakesPos, bigText, smallText, medText, words, validAlphaKeys, validNumKeys, countInfo, maxRows, hits
    
    iciclesX = 320
    characterX = 95
    characterY = 140
    towerPosSize = (400, 170, 130, 200)
    iceSquarePos = (400, 140)
    wordsPerRow = 3  
    
    # Initialize
    scene = 3
    scrn.fill(bkgdClr)    
    
    # Hills
    for hillsX in range(width):
        hillsY = int(80 * math.sin(hillsX / 120 + 400) + 180)
        pygame.draw.line(scrn, snow, (hillsX, 100 + hillsY), (hillsX, 400), 3)
     
    # Icicles
    # Coordinates
    iciclesPos1 = ((iciclesX, iciclesY), (iciclesX - 10, iciclesY - 30), (iciclesX, iciclesY - 80), (iciclesX + 5, iciclesY - 90), (iciclesX + 5, iciclesY - 100), (iciclesX + 10, iciclesY - 110), (iciclesX + 10, iciclesY))
    iciclesPos2 = ((iciclesX + 10, iciclesY), (iciclesX + 20, iciclesY - 50), (iciclesX + 25, iciclesY - 60), (iciclesX + 25, iciclesY - 80), (iciclesX + 35, iciclesY - 10), (iciclesX + 30, iciclesY))
    iciclesPos3 = ((iciclesX + 10, iciclesY), (iciclesX, iciclesY - 20), (iciclesX + 15, iciclesY - 70), (iciclesX + 25, iciclesY - 40), (iciclesX + 20, iciclesY))
    # Drawing
    outlineShape(scrn, "poly", iceFillClr, iceLineClr, iciclesPos1, 3) # 1 (left)
    outlineShape(scrn, "poly", iceFillClr, iceLineClr, iciclesPos2, 3) # 2 (right)
    outlineShape(scrn, "poly", iceFillClr, iceLineClr, iciclesPos3, 3) # 3 (middle)
     
    # Pile of snowballs behind character
    for i in range(len(snowballsClrs)):
        pygame.draw.circle(scrn, snowballsClrs[i], snowballsPos[i], 20)
     
    # The character (shirt, face, hat, pompom, sleeve, pants, shoes, eye)
    pygame.draw.rect(scrn, green, (characterX, characterY, 40, 50))
    pygame.draw.ellipse(scrn, skin, (90, 100, 50, 40))
    outlineShape(scrn, "poly", snowballsClrs[2], iceFillClr, ((characterX - 5, characterY - 30), (characterX + 5, characterY - 50), (characterX + 20, characterY - 60), (characterX + 35, characterY - 50), (characterX + 45, characterY - 30)), 4)
    pygame.draw.circle(scrn, iceFillClr, (110, 80), 10)
    pygame.draw.line(scrn, darkGreen, (110, 150), (110 + armRise, 190 - armRise), 15)
    pygame.draw.rect(scrn, mauve, (100, 190, 20, 30))
    pygame.draw.rect(scrn, mauve, (100, 210, 25, 10))
    pygame.draw.circle(scrn, darkBrown, (125, 120), 5)
     
    # The ice tower
    # base
    pygame.draw.rect(scrn, iceFillClr, towerPosSize)
    pygame.draw.rect(scrn, iceLineClr, towerPosSize, 5)
    # squares
    for i in range(3): # repeat the drawing of a column of squares 3 times
        for j in range(5): # draw the column of squares (5 squares / column)
            outlineShape(scrn, "rect", iceFillClr, iceLineClr, (i * 50 + iceSquarePos[0], j * 50 + iceSquarePos[1], 30, 30), 5)
            if j > 0 and i < 2: # draw the inner squares as only 4 * 2 (if statement only draws when conditions met)
                pygame.draw.rect(scrn, iceLineClr, (i * 50 + iceSquarePos[0] + 32, j * 50 + iceSquarePos[1] - 16, 15, 15), 5)

    # Draw the blocks of snow with words
    if numBlockRows != 0 and snowballLetter != "":
        blocksChosen = words[:(numRows * wordsPerRow)] # Chooses the first (number asked-for) words from the shuffled list
        
        for i in range(numRows): # repeats the rows (wordsPerRow) times upwards to make a grid of blocks
            row = blocksChosen[wordsPerRow * i : wordsPerRow * i + wordsPerRow] # holds list values in sets of (wordsPerRow) to be blitted with proper formatting later on
            
            for j in range(wordsPerRow): # draws a row of (wordsPerRow) blocks
                snowblockPos = (j * 68 + 370, 350 - i * 33, 65, 30)
                outlineShape(scrn, "rect", snowballsClrs[1], white, snowblockPos, 3) # block shape
                screen.blit(smallText.render(row[j].center(14), 3, skin), snowblockPos)
    
    # Count the number of times the letter appeared in the words
    if countInfo and snowballLetter != "": # Conditions: Snowball has a letter, it isn't blocked by the icicles and countInfo is true
        # Update the number of rows left the user has
        maxRows -= numBlockRows
        
        # Update the user's number of hits
        if not blocked:
            for word in blocksChosen: # takes each word form the words displayed for the round
                if snowballLetter in word: # if the letter chosen is in the word add hits
                    hits += word.count(snowballLetter)
        
        # Stop updating until the next time all conditions are met 
        countInfo = False    
    
    # Blit hits and rows left to the screen
    screen.blit(medText.render(str(maxRows) + " ROWS TO HIT", 3, mauve), (400, 50, 10, 10))
    screen.blit(medText.render(str(hits) + " / " + str(hitsToWin) + " HITS", 3, mauve), (400, 80, 10, 10))    
    
    # Main snowball
    pygame.draw.circle(scrn, snowballsClrs[0], (snowballX, snowballY), 30)
    screen.blit(bigText.render(letter, 3, white), pygame.Rect(snowballX - 10, snowballY - 20, 30, 30))    
     
    # Snowy background
    for i in range(10): # 10 snowflakes each iteration of the game loop
        scrn.blit(bigText.render("*", 3, white), flakePos[i])
        
while gameRunning:
    for evnt in pygame.event.get(): # Close pygame if the user presses the X
        if evnt.type == pygame.QUIT:
            gameRunning = False
    
    if scene == 3: # if scene is 3, reset the variables for a new game
        # Main snowball
        snowballLetter = ""
        snowballXPos = 150
        snowballYPos = 190
        
        # Hits, blocks, crashes
        blocksChosen = []
        maxRows = 15
        numBlockRows = 0
        lettersUsed = []
        runningCount = 0
        hits = 0
        crash = False
        countInfo = True
        miss = False
        
        # Game function
        gameSceneRunning = True
        iceMustRise = True
        icicleYPos = 400
        armPos = 0     
    
    # Get mouse coordinates
    mx = getMouseXY()[0]
    my = getMouseXY()[1]
    
    # Change scene based on number
    if scene == 1:
        menuScene(screen, mx, my)
    elif scene == 2:
        howToPlayScene(screen, mx, my)
    while scene == 3 and gameSceneRunning:
        for evnt in pygame.event.get(): # Closes pygame if the user presses the X
            if evnt.type == pygame.QUIT:
                gameSceneRunning = False # Must exit the inner loop before the outer
                gameRunning = False

            # If a number of rows of blocks is not determined, the number is the first valid one pressed
            if evnt.type == pygame.KEYDOWN and numBlockRows == 0:
                key = pygame.key.get_pressed()
                for i in validNumKeys: # loop through all valid number keys
                    if key[i] and maxRows - int(pygame.key.name(i)) >= 0: # if a valid number is pressed and it is less than the current maxRows
                        numBlockRows = int(pygame.key.name(i))
                    
            # if a row number is determined and a snowball-assigned letter is needed, assign the first valid one pressed
            if evnt.type == pygame.KEYDOWN and numBlockRows != 0 and snowballLetter == "":
                key = pygame.key.get_pressed()
                for i in VALID_ALPHA_KEYS: # loop through all valid letter keys
                    if key[i] == True and pygame.key.name(i) not in lettersUsed: # if a valid letter is pressed and it has not yet been pressed
                        snowballLetter = pygame.key.name(i)
                        lettersUsed.append(snowballLetter)
                        countInfo = True
        
        # Draw the static elements
        gameScene(screen, icicleYPos, armPos, snowflakesPos, snowballXPos, snowballYPos, snowballLetter, numBlockRows, miss, mx, my)
        
        # If the snowball reaches a y of 350, crash
        if snowballYPos == 350:
            crash = True
        
        # Reset variables after a crash
        if crash:
            snowballLetter = ""
            snowballXPos = 150
            snowballYPos = 190
            armPos = 0 # arm of the character goes back down
            numBlockRows = 0
            random.shuffle(words)
            crash = False       
        
        # If letter and block info entered, the snowball should roll with the hill and the person's arm should go up
        if snowballLetter != "" and numBlockRows != 0 and snowballYPos < 350:
            armPos = 45
            snowballXPos += 5
            snowballYPos = int(80 * math.sin(snowballXPos / 120 + 400) + 280)        
                
        # Check if an icicle rise is needed
        if icicleYPos > height + 100:
            iceMustRise = False
        if icicleYPos < height:
            iceMustRise = True
            
        # Change the y-value of the icicles
        if iceMustRise:
            icicleYPos += 2
        else:
            icicleYPos -= 6
            
        # Change the snowflake position every few seconds
        if runningCount % 7 == 0: # Every time the running count is a multiple of 10, snowflake positions are changed
            snowflakesPos = []
            # Append 10 random snowflake positions each time. Positions can range from any x, but must have a y-value > 350 because snowflakes that low aren't very visible
            for snowflake in range(10):
                snowflakesPos.append((random.randint(0, width), random.randint(0, height - 100), 100, 100))       
        
        # Check for win or loss
        if hits >= hitsToWin or maxRows == 0:
            gameSceneRunning = False # Stop playing the game
            screen.fill(white) # New background
            
            # Display status based on win or loss
            if hits >= hitsToWin: 
                screen.blit(bigText.render("YOU WON!", 3, mauve), (width // 3, 130, 10, 10))    
            elif maxRows == 0:
                screen.blit(bigText.render("You lost :(", 3, mauve), (width // 3, 130, 10, 10))
                
            # Wait a little    
            pygame.display.flip()
            pygame.time.wait(1000) 
            
            # End status
            screen.blit(medText.render(str(hits) + " hits from " + str(hitsToWin) + " and " + str(maxRows) + " rows left", 3, mauve), (150, 210, 10, 10))
            
            # Wait a little and change to menu scene
            pygame.display.flip()
            pygame.time.wait(2000)
            scene = 1
        else:
            # Counter
            runningCount += 1
            
            # Display and wait
            pygame.display.flip()
            pygame.time.wait(60)        
    
    # Repeat full game loop
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
