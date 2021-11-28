import pygame, sys
from pygame.locals import *

#-Variables-------------#
#Colours
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
running =  True

#Font paths
optimusFont = 'Assets/Fonts/optimus.ttf'
generationFont = 'Assets/Fonts/generation.ttf'


#This was the first function I wrote, so its a LOT messier than the others. I apologise in advance. 
def mainMenu(screen, mainClock, write):
    #and now for the powerup animations

    #Animates the powerups
    def powerupAnimation(list, frames, path):
        for i in range((frames - 1)):
            list.append(pygame.image.load(path + str(i+1) + '.png').convert())
        return list
    
    #Just a word counter for later. Finds the gaps, and sees how many there are. 
    def countWords(text, n):
        start = text.find(' ')
        while start >= 0 and n > 1:
            start = text.find(' ', start+len(' '))
            n -= 1
        return start    
    
    #Prints the description of each powerup using the count words function to properly word wrap the text. Still took some fiddling to see how many words I could fit on one line.   
    def printDesc(names, desc, powerup, row, col, size):
        index = countWords(desc, 3)
        nameTXT = write(names, WHITE, size + 4, optimusFont)
        descTXT1 = write(desc[:index], WHITE, size, optimusFont)
        if len(desc) > index:
            desctTXT2 = write(desc[index + 1:], WHITE, size, optimusFont)
        else:
            desctTXT2 = ''
    
        screen.blit(nameTXT, (row + powerup.get_rect().w, col))
        screen.blit(descTXT1, (row, col + powerup.get_rect().h))

        if len(desc) > 3:
            screen.blit(desctTXT2, (row, col + powerup.get_rect().h + descTXT1.get_rect().h))
    
     #i should comment this but i wont
    def getCenter(text):
        xcenter = (600 - text.get_rect().w)/2
        return xcenter
    
    
    
    
    #
    #Paths for the powerups.
    catchPath = "Assets/MainMenu/powerup_catch_"
    dupePath = "Assets/MainMenu/powerup_duplicate_"
    expandPath = "Assets/MainMenu/powerup_expand_"
    laserPath = "Assets/MainMenu/powerup_laser_"
    lifePath = 'Assets/MainMenu/powerup_life_'
    slowPath = 'Assets/MainMenu/powerup_slow_'
    
    #Sets up a list of images for the powerup - I could've done this with one class. It would've been so much neater. I might redo it later. 
    cAni = powerupAnimation([],8, catchPath)
    dAni = powerupAnimation([], 8, dupePath)
    eAni = powerupAnimation([], 8, expandPath)
    lAni = powerupAnimation([], 8, laserPath)
    liAni = powerupAnimation([], 8, lifePath)
    sAni = powerupAnimation([],8, slowPath)
    logo = pygame.image.load("Assets/MainMenu/logo.png").convert()
    
  
    #powerup names + descriptions go here 
    PowerupNames = [
    "CATCH",
    "DUPLICATE",               
    "EXPAND",
    "LASER",
    "EXTRA LIFE",
    "SLOW",     
                    ]
    PowerupDesc = [
        "CATCHES THE ENERGY BALL",
        "DUPLICATES THE ENERGY BALL",
        "EXPANDS THE VAUS ",
        "ENABLES THE VAUS TO FIRE A LASER",
        "GAIN AN ADDITIONAL VAUS",
        "SLOW DOWN THE ENERGY BALL",
    ]
    
    
    #gets the highscore
    file1 = open("Assets/textfiles/highscore.txt","r+")
    highscore = file1.read()
    file1.close()
    
    x = 0
    #the index for the flashing start text = basically it alternates between the yellow and white version to create a flashing effect. 
    startNo = 0
    #see the readme for an explanation on loop control. 
    loopControl = 12
    #holds the flashing start text image
    startList = []
    loopControl2 = 20
    
    while True:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                return
        screen.fill(BLACK)
        #blits logo to screen
        screen.blit(logo, (getCenter(logo),0))
        
        #using write function to create blittable images for all the text
        scoreCounter = write("HIGHSCORE", RED, 28, generationFont)
        highscoreTXT = write(str(highscore), WHITE, 36, generationFont)
        powerupTXT = write("POWERUPS", WHITE, 36, optimusFont)
        startTXT1 = write("SPACEBAR TO START", WHITE, 48, optimusFont)
        startTXT2 = write("SPACEBAR TO START", YELLOW, 48, optimusFont)
        startList.append(startTXT1)
        startList.append(startTXT2)
        
        #blits everything tot he screen jesus 
        screen.blit(scoreCounter, (getCenter(scoreCounter),logo.get_rect().h + 20))
        screen.blit(highscoreTXT, (getCenter(highscoreTXT),logo.get_rect().h + scoreCounter.get_rect().h + 20))
        screen.blit(powerupTXT, (getCenter(powerupTXT),logo.get_rect().h + 100))
        screen.blit(startList[startNo], (getCenter(startTXT1), 550))
        
        #Blits the powerups to the screen
        animationList = [cAni[x], dAni[x], eAni[x], lAni[x], liAni[x], sAni[x]] 
        rowList = [25,25,225,225,425,425]
        colList = [300,400,300,400,300,400]
        
        for i in range(6):
            screen.blit(animationList[i], (rowList[i], colList[i]))
        #Now we blit the description to the screen
        for i in range(6):
            printDesc(PowerupNames[i], PowerupDesc[i], animationList[i],rowList[i], colList[i], 14)
        
        #More loop control stuff - basically updates every 5 frames for 12 frames per second. W    
        if loopControl%5 == 0:
           x = x + 1
        elif loopControl == 5:
            loopControl = 0
        
        loopControl += 1
        
        if x == 7:
            x = 0
        
        #This is the loop control for the flashing text - it only updates ever 10 frames for 6 frames per second. 
        if loopControl2%10 == 0:
            startNo +=1
        if startNo == 2:
            startNo = 0
        loopControl2 += 1
        if loopControl2 == 10:
            loopControl2 = 0    
        
        #Updates display 
        pygame.display.flip()
        mainClock.tick(60)
  

def endMenu(screen, clock, write, score, highscore):
    #Runs the end menu - creates 4 images, one each for score/highscore counter, and another one each for the actual values. 
    highscoreCounter = write("HIGHSCORE", RED, 36, generationFont)
    highscoreTXT = write(str(highscore), WHITE, 36, generationFont)
    scoreCounter = write("SCORE", RED, 36, generationFont)
    scoreTXT = write(str(score), WHITE, 36, generationFont)
    
    #mini game loop i guess
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
               return
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return
        
        #displays score and high score.       
        screen.fill(BLACK) 
        screen.blit(highscoreCounter,(0,0))
        screen.blit(highscoreTXT, (0, highscoreCounter.get_rect().h))
        screen.blit(scoreCounter, (0, highscoreCounter.get_rect().h + highscoreTXT.get_rect().h))
        screen.blit(scoreTXT, (0, highscoreCounter.get_rect().h + highscoreTXT.get_rect().h + scoreCounter.get_rect().h))
        pygame.display.flip()
        clock.tick(60)
  