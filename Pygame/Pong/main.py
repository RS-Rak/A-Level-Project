import pygame, sys, time, random

from pygame.constants import QUIT
from paddle import Paddle
from ball import Ball
from menus import Menus, write



pygame.init() #Initalises pygame
pygame.font.init() #initalises fonts

#music
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Pygame/Pong/Sounds/MAINTHEME.mp3')
pygame.mixer.music.play(-1) #-1 means loops for ever, 0 means play just once)
pygame.mixer.music.set_volume(0.5)

#Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0, 255, 0)

#Initialises the scores
ScoreA = 0
ScoreB = 0
#Open a new window
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#Player paddle
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200 

#AI Paddle
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

#Ball
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195


#---------------PLAYER 2 OR AI------------------#

# values for AI difficulty
const1 = 0
const2 = 50

#Shows if player 2 is human controlled or AI
AI = True

#--------------------SOUND ---------------------------#

#The sound effect for when it bounces. 
bounceSound = pygame.mixer.Sound("Pygame/Pong/Sounds/pongBounce.wav")

#The sound effect for when it scores
scoreSound = pygame.mixer.Sound("Pygame/Pong/Sounds/score.wav")


#draws every sprite in thiss group on the screen
all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

#SHOWS IF MAIN MENU IS UP OR NOT
onMenu = True

#SHOWS IF MUSIC IS PAUSED
paused = False

playing = True

#The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------------------MAIN PROGRAM LOOP -------------------------------------
while playing:
    #--------------MAIN EVENT LOOP-------------# 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing == False
        elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    playing = False
    
        
    
    #Game logic goes here wee



    done = True
    #Main menu
    while onMenu == True:
        Menus.main_menu(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                    AI = True
                    onMenu = False
                elif event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                    AI = False
                    onMenu = False
                elif event.key == pygame.K_x:
                    playing = False
                    onMenu = False
                    break
                
     
    
    all_sprites_list.update()

    #Arrow keys are being saved for when P2 is here. 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.move_up(5)
    if keys[pygame.K_s]:
        paddleA.move_down(5)
    if AI == False:
        if keys[pygame.K_UP]:
            paddleB.move_up(5)
        elif keys[pygame.K_DOWN]:
            paddleB.move_down(5)

    
    #Check if the ball is bouncing against any of the 4 walls: if so plays a bounce sound/score sound, and then moves it
    if ball.rect.x>=690:
       
       #calls the score function from the ball class, go check that out its pretty neat 
       ScoreA = ball.score(ScoreA, scoreSound, paddleA, paddleB)
       time.sleep(1)

    if ball.rect.x<=0:
       
       #SAME AS BEFORE
       ScoreB = ball.score(ScoreB, scoreSound, paddleA, paddleB)
       time.sleep(1)

    def bounce(bounceSound):
        ball.velocity[1] = -ball.velocity[1]
        bounceSound.play()

    if ball.rect.y>490 or ball.rect.y < 0:
        bounce(bounceSound)
      
    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce(bounceSound)
 
    #Checks to see if anyone has won:
    if ScoreA >= 3 or ScoreB >= 3:
        running = True
        while running:

            if ScoreA > ScoreB:

                #-------------DISPLAYS VICTORY SCREEN------------------#

                screen.fill(BLACK)
                text, textWidth, textHeight = write("Player 1", GREEN, 80)
                screen.blit(text, (((700 - textWidth)/2),((500-textHeight)/2 - 50)))

                text, textWidth, textHeight = write("Wins", GREEN, 80)
                screen.blit(text, (((700 - textWidth)/2),((500)/2)))


                text, textWidth, textHeight = write("PRESS ANY BUTTON TO RETURN TO MENU", WHITE, 20)
                screen.blit(text, (((700 - textWidth)/2),(500 - textHeight)))
                pygame.display.flip()

            elif ScoreB > ScoreA:

                screen.fill(BLACK)

                #---------------IF ITS COMPUTER, A DIFFERENT MESSAGE WILL SHOW WHEN THEY WIN.------------#
                if AI == False:
                    text, textWidth, textHeight = write("Player 2", RED, 80)
                    screen.blit(text, (((700 - textWidth)/2),((500-textHeight)/2 - 50)))

                    text, textWidth, textHeight = write("Wins", RED, 80)
                    screen.blit(text, (((700 - textWidth)/2),((500)/2)))
                else:
                    text, textWidth, textHeight = write("Computer", RED, 80)
                    screen.blit(text, (((700 - textWidth)/2),((500-textHeight)/2 - 50)))

                    text, textWidth, textHeight = write("Wins", RED, 80)
                    screen.blit(text, (((700 - textWidth)/2),((500/2))))

                text, textWidth, textHeight = write("PRESS ANY BUTTON TO RETURN TO MENU", WHITE, 20)
                screen.blit(text, (((700 - textWidth)/2),(500 - textHeight)))
                pygame.display.flip()
            ScoreA = 0
            ScoreB = 0
            
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    running = False
                    onMenu = True
                
                

    #AI control. Greater the diff between const1 and 2, easier it is 

    if AI == True:   
        if paddleB.rect.y + random.randint(const1, const2) < (ball.rect.y + 10):
            #ideas for diff = change const values, change offset from ball val?
            if random.randint(1,4) == 4:
                pass
            paddleB.move_down(5)
        elif paddleB.rect.y  + random.randint(const1, const2) > (ball.rect.y + 10):
            paddleB.move_up(5)



    #DRAWING CODE
    screen.fill(BLACK)
    
    #Draw the net
    pygame.draw.line(screen, WHITE, [349,0],[349,500],5)

    all_sprites_list.draw(screen)
    
   # Display scores:
    font = pygame.font.Font("Pygame/Pong/Fonts/ARCADECLASSIC.TTF", 74)
    text = font.render(str(ScoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(ScoreB), 1, WHITE)
    screen.blit(text, (420,10))
 
    pygame.display.flip()

    clock.tick(60)

#TO ADD
#MUSIC
#MAIN MENU
#PLAYER 2 AND/OR AI
#VICTORY/LOSS CONDITIONS
#Accel for the pong paddles?


pygame.quit()
sys.exit()