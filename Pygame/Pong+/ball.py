import pygame
from random import randint
import time

BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):


        def __init__(self, color, width, height):
            super().__init__()


            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)
            self.image.set_colorkey(BLACK)


            pygame.draw.rect(self.image, color, [0,0, width, height])

            self.velocity = [randint(3,8),randint(-4,8)]

            self.rect = self.image.get_rect()

        def update(self):
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]
        
        def bounce(self,bounceSound):
            self.velocity[0] = -self.velocity[0] * 1.005
            self.velocity[1] = randint(-8,8) * 1.005
            bounceSound.play()
        
        def score(self, score, scoreSound, paddleA, paddleB):
            score += 1
            
            #plays score sound
            scoreSound.play()

            #resets ball pos
            self.rect.x = 345
            self.rect.y = 195
                        
            #resets paddle pos
            paddleA.rect.x = 20
            paddleA.rect.y = 200

            paddleB.rect.x = 670
            paddleB.rect.y = 200

            #Resets the ball speed
            self.velocity = [randint(3,8),randint(-4,8)]

            #changes ball direction
            self.velocity[0] = -(0.75)* self.velocity[0]
            self.velocity[1] = -(0.75) *self.velocity[1]
                
            #when ball has  been reset pauses
            return score    