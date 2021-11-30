import pygame, sys
from pygame.locals import *
import time
from random import randint


#-Variables-------------#
#Colours
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARKBLUE = (0,0,55)
DARKGREEN =(0,100,0)
LIGHTBLUE = (68,85,90)
LIGHTRED = (210,111,111)

#Font paths
optimusFont = 'Assets/Fonts/optimus.ttf'
generationFont = 'Assets/Fonts/generation.ttf'
    
def round(screen, clock, roundNumber, write, Brick, Paddle, Ball, Powerup, Bullet, Enemy, lives, score):    
    roundStart = True
    running = True
    #Functions
    def drawScreen():
        #This is the base stuff, that pretty much doesn't change. Things like the highscore counter, background, some of the text, etc. These are all just drawn at the beginning of the round by calling this function. Not much else to say. 
        highscoreCounter = write("HIGHSCORE", RED, 20, generationFont)
        highscoreTXT = write(str(highscore), WHITE, 20, generationFont)
        scoreCounter = write("SCORE", RED, 20, generationFont)
        scoreTXT = write(str(score), WHITE, 20, generationFont)
        roundTXT = write("ROUND " + str(roundNumber), WHITE, 20, optimusFont)
        
        
        
        pygame.draw.rect(screen, roundColors[(roundNumber - 1)%4], [0,150,600,800])
        screen.blit(leftEdge, (0,150))
        screen.blit(rightEdge, (578,150))
        screen.blit(topEdge[edgeNo], (22,150))
        screen.blit(logo, (0,0))
        screen.blit(scoreCounter, (logo.get_rect().w, 0))
        screen.blit(scoreTXT, (logo.get_rect().w, scoreCounter.get_rect().h))
        screen.blit(highscoreCounter, (logo.get_rect().w, scoreCounter.get_rect().h + scoreTXT.get_rect().h))
        screen.blit(highscoreTXT, (logo.get_rect().w, scoreCounter.get_rect().h + scoreTXT.get_rect().h + highscoreCounter.get_rect().h))
        screen.blit(roundTXT, (logo.get_rect().w, 80))
      
    def generateRound(brickColors, spriteList, allBricks, goldBricks):
        
        #Reads the text file, and generates a list, with each index holding a row of the text file.
        with open("Assets/textfiles/round_" + str(roundNumber) + ".txt") as f:
            content = f.readlines()
        brickList = [x.strip() for x in content]
        
        #Outer loop repeats for as many lines as there are in the file
        for i in range(len(brickList) - 1):
            #Inner loop repeats for 13 - the number of characters per line. 
            for x in range(13):
                #If the character is - it shows there should be no brick in this space, and continues to the next loop iteration. 
                if brickList[i+1][x] == '-':
                    continue
                #Taking the number from the character thats being read, it checks how it corresponds with the colours, and then creates a new brick object with the relevant color.
                brick = Brick(brickColors[int(brickList[i + 1][x])])
                #Sets up the x and y co-ords based on the row and column. 
                brick.rect.x = 22 + (x * 43)
                brick.rect.y = (int(brickList[0]) + i * 21 + 150)
                spriteList.add(brick)
                #If gold, adds it to its own list, as gold bricks are invincible.
                if brick.color == 'gold':
                    goldBricks.add(brick)
                else:
                    allBricks.add(brick)
                    
    #Displays number of lives in the bottom left.
    def printLives(lives):
        for i in range(lives):
            life = pygame.image.load("Assets/Paddle/paddle_life.png").convert_alpha()
            screen.blit(life, (22 + i * 43, 783))
    
    #I mess with this function when i when want to test a particular powerup, usually change the odds or spawn rate. 
    def randomSpawn(spriteList, PowerupList, brick):
        #the % chance of a powerup spawn.
         if (randint(2,10)) == 7:
             powerup = Powerup(validPowerups[randint(0,len(validPowerups)-1)])  
             #powerup = Powerup("laser")
             #However, only 10% for a life powerup or if you have max lives (5)
             if (powerup == 'life' and (randint(1,2)) == 2) or lives >= 5:
                 return
             #adds to lists, etc,etc
             spriteList.add(powerup)
             PowerupList.add(powerup)
             powerup.rect.x = brick.rect.x
             powerup.rect.y = brick.rect.y
    
    def reset():
        #this is for the end of the round - kills off any remaining sprites, so the next round can be cleanly generated.  
        for mainball in ball_list:
            mainball.kill()
        for enemy in enemylist:
            enemy.kill()
        playerpaddle.kill()
    
    #Explosion animation for when an enemy is damaged. 
    def explosion(x,y, loopControl, index):
        loopControl += 1
        if loopControl%2 == 0:
            index += 1
            if index == 10:
                index = 0
                loopControl = 0
                return loopControl, index, False
        screen.blit(explosions[index], (x,y))
        return loopControl, index, True
    
    #Variables 
    
     
    edgeNo = 0
    powLoopControl = 0
    enemyloopcontrol = 0
    powerupActive = False
    laserCollision = False
    #these next ones are just holders = technically the variables dont exist when i call them so i need a filler. Yes, there are a lot of variables but they're mostly just to check if something is active.
    savedVel = 4
    caughtRN = False
    diff = 0
    isCatch = False
    isSpawning = False
    bullets = []
    ball_list = []
    bulletCD = False
    bulletShot = 0
    isExploding = False
    explosionIndex = 0
    explosionLoop = 0
    doorloopcontrol = 0
    enemySpawning = False
    enemylist = []
    enemies = ["cone","pyramid","molecule","cube"]
    #----
    file1 = open("Assets/textfiles/highscore.txt","r+")
    highscore = file1.read()
    file1.close()
    roundColors = [DARKBLUE, DARKGREEN, LIGHTBLUE, LIGHTRED]
    brickColors = ["blue", "cyan", "gold", "green", "orange", "pink", "red", "silver","white", "yellow"]
    validPowerups = ["expand","slow","life","catch","laser","duplicate"]
    
    #Image creation
    explosions = []
    for i in range(10):
        explosions.append(pygame.image.load("Assets/explosions/enemy_explosion_{}.png".format(str(i+1))).convert_alpha())
        
    
    
    logo = pygame.image.load("Assets/MainMenu/logo.png").convert()
    leftEdge = pygame.image.load("Assets/Edges/edge_left.png").convert()
    rightEdge = pygame.image.load("Assets/Edges/edge_right.png").convert()
    topEdge = []
    topEdge.append(pygame.image.load("Assets/Edges/edge_top.png").convert())
    for i in range(7):
        topEdge.append(pygame.image.load("Assets/Edges/door_top_left_" + str(i+1) + ".png").convert())
    for i in range(7):
        topEdge.append(pygame.image.load("Assets/Edges/door_top_right_" + str(i+1) + ".png").convert())
    
    #These are the classes stuff, need to make some groups to hold them lmao
    all_sprites_list = pygame.sprite.Group()
    all_bricks = pygame.sprite.Group()
    goldBricks = pygame.sprite.Group()
    powerupList = pygame.sprite.Group()
    
    #Round generation time. 
    generateRound(brickColors, all_sprites_list, all_bricks, goldBricks)
    playerpaddle = Paddle()
    playerpaddle.rect.x = 250
    playerpaddle.rect.y = 760
    all_sprites_list.add(playerpaddle)
    mainball = Ball()
    mainball.rect.x = 270
    mainball.rect.y = 750
    ball_list.append(mainball)
    all_sprites_list.add(mainball)
    
    #Game logic goes here chief.
    while running:
        
    
        
        #--------------MAIN EVENT LOOP-------------# 
        for event in pygame.event.get():
            if event.type == QUIT:
                running == False
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    running = False
                    sys.exit()
                
                if event.key == pygame.K_SPACE:
                    if powerupActive == True:
                        #If you press space, AND the catch powerup is active AND the ball is caught, the ball is sent off at the angle and speed it would've been sent off at if catch wasn't active. 
                        if caughtRN == True:
                            mainball.velocity[0] = savedVel
                            mainball.velocity[1] = -6
                            caughtRN = False
                        elif playerpaddle.powerup == 'laser' and bulletCD == False:
                            #If laser is active, and you press space, and the bullet isn't on cooldown, it creates a pair of new bullet objects, and adds them to the list.
                                bullet = Bullet('left', playerpaddle)
                                bullets.append(bullet)
                                all_sprites_list.add(bullet)
                                bullet = Bullet('right', playerpaddle)
                                bullets.append(bullet)
                                all_sprites_list.add(bullet)
                                bulletShot = time.time()
                                bulletCD = True
                    if isSpawning == True:
                        mainball.velocity[0] = 0
                        mainball.velocity[1] = -5
                        isSpawning = False
        
        #Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerpaddle.moveLeft(6)
        if keys[pygame.K_RIGHT]:
            playerpaddle.moveRight(6)
        
        #Drawing code rq
        #draws the main round screen - only the boundaries, logo and screen.
        screen.fill(BLACK)
        drawScreen()
        if roundStart == True:
            playerpaddle.animate("spawn", all_sprites_list, clock, screen, roundColors[(roundNumber - 1)%4], topEdge[edgeNo], leftEdge, rightEdge, lives, printLives)
            roundStart = False
            playerpaddle.rect.x = 270
            playerpaddle.rect.y = 760
            mainball.rect.x = 300
            mainball.rect.y = 750
            mainball.velocity[0] = 3
            mainball.velocity[1] = 5
            roundStartTime = time.time()
        printLives(lives)
        #Game logic time bbbb
        # --- Game logic should go here
        all_sprites_list.update()
        mainball.stuck(playerpaddle, diff, caughtRN)
        
        
        
        #----------------COLLISIONS--------------------#
        
        #Collision code for the ball and the paddle using paddleBounce
        for mainball in ball_list:
            if pygame.sprite.collide_mask(mainball, playerpaddle):
                mainball.rect.y = 750
                if playerpaddle.powerup == 'catch':
                    savedVel, isCatch, caughtRN, diff = mainball.paddleBounce(playerpaddle, True)
                else:
                    mainball.paddleBounce(playerpaddle, isCatch)
        
        #assuming there are gold bricks, handles collisionss with them
        if len(goldBricks) > 0:
            for mainball in ball_list:
                gold_brick_collisions = pygame.sprite.spritecollide(mainball, goldBricks, False)
                for brick in gold_brick_collisions:
                    #added these lines to try stop it getting stuck inside the gold bricks. if it does get stuck there, it moves it outside of the brick. 
                    if (mainball.rect.y + (mainball.rect.h)/2)> brick.rect.y and (mainball.rect.y  +  (mainball.rect.h)/2) < brick.rect.y + (brick.rect.h)/2:
                        mainball.rect.y = brick.rect.y - mainball.rect.h
                    elif mainball.rect.y > brick.rect.y + (brick.rect.h)/2 and mainball.rect.y < brick.rect.y + brick.rect.h:
                        mainball.rect.y = brick.rect.y + brick.rect.h 
                    #See ball.py
                    mainball.bounce(brick)    
        
        #handles picking up powerups by checking if any collide with the paddle. If they do, it runs the collectpowerup function.
        if len(powerupList) > 0:
            powerupCollisions = pygame.sprite.spritecollide(playerpaddle, powerupList, False)
            for powerup in powerupCollisions:
                if powerup.powerup == 'life':
                    lives += 1
                    powerup.kill()
                else:
                    powerup.kill()
                    startTime = playerpaddle.collectPowerup(powerup.powerup, all_sprites_list, clock, screen, mainball, roundColors[(roundNumber - 1)%4], topEdge[edgeNo], leftEdge, rightEdge, lives, printLives)
                    #If its catch, changes this variable. Do i need it? Probably not, but it would take more work to remove.
                    if playerpaddle.powerup == 'catch':
                        isCatch = True
                        while len(ball_list) > 1:
                            ball_list[1].kill()
                            ball_list.pop(1)  
                    else:
                        isCatch = False
                    
                    #If the duplicate powerup is active, then two more balls are created and appended. 
                    if playerpaddle.powerup == 'duplicate':
                        for i in range(2):
                            mainball = Ball()
                            mainball.rect.x = playerpaddle.rect.x + (playerpaddle.rect.w)/2
                            mainball.rect.y = 750
                            if i == 1:
                                mainball.velocity[0] = -4
                            else:
                                mainball.velocity[0] = 4
                            mainball.velocity[1] = -6
                            ball_list.append(mainball)
                            all_sprites_list.add(mainball)
                            
                    #Once the powerup has been collected, it must be killed, and poewrupActive must be true.   
                    #powerup.kill()
                    powerupActive = True
            #hell, might as well throw some other code in here too.  This animates the powerup as it falls, assuming any are on screen. 
            for powerup in powerupList:
                powLoopControl = powerup.animate(powLoopControl)
                if powerup.rect.y > 800:
                    powerup.kill()
        
        #This is ball and brick collisions. This runs for every ball that exists on screen - all of which are held in ball list, and checks collisions for them all. 
        for mainball in ball_list:
            #This handles the brick collisions. If the brick collides. ball bounce. 
            brick_collision_list = pygame.sprite.spritecollide(mainball,all_bricks,False)
            for brick in brick_collision_list:
                while len(brick_collision_list) > 1:
                    #This is to avoid a glitch I had, where when 2 blocks are hit simultaneously, the 2 velocity flips cancel each other, and the ball simply doesnt bounce. So it only allows 1 brick to be registed as being collided into as one. 
                    brick_collision_list.pop(1)
                #bounce bounce
                mainball.bounce(brick)
                score = brick.brickHit(score)
                if brick.hits == 0:
                    randomSpawn(all_sprites_list, powerupList, brick) 
                if len(all_bricks)==0:
                    reset()
                    return False, score, highscore, lives
            

        #This is for the good old laser brick collisions
        for bullet in bullets:
            collisionlist = pygame.sprite.spritecollide(bullet, all_bricks, False)
            for brick in collisionlist:
                while len(collisionlist) > 1:
                    collisionlist.pop(1)
                score = brick.brickHit(score)
                bullets = bullet.collision(bullets)
            
        #ok now enemy collision check - this is basically checking if the enemies are colliding with anything - if they are, then it either kills them or blocks them from moving. 
        #Enemy list holds the enemy objects.
        for enemy in enemylist:
            #Checks if its colliding with the paddle or ball - if so kills it, plays the explosion effect, and if its the ball, makes it change direction. 
            if pygame.sprite.collide_mask(enemy, playerpaddle):
                x = enemy.rect.x
                y = enemy.rect.y
                enemy.kill()
                enemylist.pop(enemylist.index(enemy))
                isExploding = True
            for mainball in ball_list:
                if pygame.sprite.collide_mask(enemy, mainball):
                    mainball.velocity[1] = -mainball.velocity[1]
                    x = enemy.rect.x
                    y = enemy.rect.y
                    enemy.kill()
                    enemylist.pop(enemylist.index(enemy))
                    isExploding = True
            enemycollisions = pygame.sprite.spritecollide(enemy, all_bricks, False)
            for brick in enemycollisions:
                #If the enemy is colliding with the side of the brick.
                if enemy.rect.y > brick.rect.y and enemy.rect.y < brick.rect.y + brick.rect.h: 
                    enemy.velocity[0] = -enemy.velocity[0]
                #Else it just prevents it from moving further down. 
                else:
                    enemy.rect.y = brick.rect.y - enemy.rect.h      
            if len(goldBricks) > 0:
                goldBricksEnemyCollisons = pygame.sprite.spritecollide(enemy, goldBricks, False)
                for brick in goldBricksEnemyCollisons:
                     if enemy.rect.y > brick.rect.y and enemy.rect.y < brick.rect.y + brick.rect.h: 
                        enemy.velocity[0] = -enemy.velocity[0]
                     else:
                        enemy.rect.y = brick.rect.y - enemy.rect.h   
        
        #quick check to see if the game is finished. 
        if len(all_bricks) == 0:
            reset()
            return False, score, highscore, lives
            
            
        #Check if the ball is bouncing against any of the 4 walls:
        for mainball in ball_list:
            if mainball.rect.x>=568:
                mainball.rect.x = 568
                mainball.velocity[0] = -mainball.velocity[0]
            if mainball.rect.x<=22:
                mainball.rect.x = 22
                mainball.velocity[0] = -mainball.velocity[0]
            if mainball.rect.y <= 172:
                mainball.rect.y = 172
                mainball.velocity[1] = -mainball.velocity[1] 
            elif mainball.rect.y >= 790:
                mainball.kill()
                ball_list.pop(ball_list.index(mainball))
        #hell, lets do the same for the enemies
        for enemy in enemylist:
            if enemy.rect.x >= (578 - enemy.rect.w):
                enemy.rect.x = (578 - enemy.rect.w)
                enemy.velocity[0] = -enemy.velocity[0] 
            if enemy.rect.x <=22:
                enemy.rect.x = 22
                enemy.velocity[0] = -enemy.velocity[0]
            if enemy.rect.y > 800:
                enemy.kill()
                enemylist.pop(enemylist.index(enemy))
        
        #Checks to see if all balls are dead - if they are creates a new ball item. 
        if len(ball_list) <= 0:
            lives -= 1
            if lives == 0:
                playerpaddle.animate('death', all_sprites_list, clock, screen, roundColors[(roundNumber-1)%4], topEdge[edgeNo], leftEdge, rightEdge, lives, printLives)
                reset()
                return True, score, highscore, lives
            mainball = Ball()
            all_sprites_list.add(mainball)
            ball_list.append(mainball)
            mainball.rect.x = 300
            mainball.rect.y = 750
            mainball.velocity[0] = 0
            mainball.velocity[1] = 0
            isSpawning = True
        
        #Checks if you have a powerup active.
        if powerupActive:
            timePassed = time.time() - startTime
            #if powerup timer is over, it resets the effects.
            if timePassed > 20:
                if playerpaddle.powerup == 'catch':
                     mainball.velocity[0] = 4
                     mainball.velocity[1] = -6
                #kills all the balls bar one. 
                if playerpaddle.powerup == 'duplicate':
                    while len(ball_list) > 1:
                        ball_list[1].kill()
                        ball_list.pop(1)  
                
                #resets the necessary variables, and clears any paddle effecs.  
                playerpaddle.reset()
                caughtRN = False
                isCatch = False
                powerupActive = False
                bullets = []
            #Shooting cooldown on the bullet.
            if playerpaddle.powerup == 'laser':
                if time.time() - bulletShot > 0.4:
                    bulletCD = False

        #Assuming there are enemies on screen, it animates them. 
        if len(enemylist) > 0:
            for enemy in enemylist:
                enemyloopcontrol = enemy.animate(enemyloopcontrol)
        
        
        
        #checks to see if bullets are out of range
        for bullet in bullets:
            if bullet.rect.y < 172:
                bullet.kill()
        #now we check if we need to spawn any enemies, and then spawns them. Edgeno and endno are the start and end indexes for the images. 
        if (time.time() - roundStartTime) >= 25:
            if randint(1,2) == 1:
                enemy = Enemy(enemies[(roundNumber - 1)%4], 'right')
                edgeNo = 8
                endNo = 15
            else:
                enemy = Enemy(enemies[(roundNumber-1)%4],'left')
                edgeNo = 1
                endNo = 8
            enemySpawning = True
            enemylist.append(enemy)
            all_sprites_list.add(enemy)
            roundStartTime = time.time()

        #If the enemy is dead, plays explosion graphic. 
        if isExploding == True:
            explosionLoop, explosionIndex, isExploding = explosion(x,y,explosionLoop,explosionIndex)
        
        #If an enemy is spawning, it opens the relative door on the top edge.
        if enemySpawning:
            
           doorloopcontrol += 1
           if doorloopcontrol%6 == 0:
               edgeNo += 1
               if edgeNo == endNo:
                   edgeNo = 0
               if edgeNo == 0:
                enemySpawning = False
               
        #now we quickly check the animation lads.
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)