import pygame
class player(object):
    walkRight = [pygame.image.load('images/right/r1.png'),pygame.image.load('images/right/r2.png'),pygame.image.load('images/right/r3.png'),pygame.image.load('images/right/r4.png'),pygame.image.load('images/right/r5.png'),pygame.image.load('images/right/r6.png'),pygame.image.load('images/right/r7.png'),pygame.image.load('images/right/r8.png'),pygame.image.load('images/right/r9.png'),pygame.image.load('images/right/r10.png'),pygame.image.load('images/right/r11.png'),pygame.image.load('images/right/r12.png'),pygame.image.load('images/right/r13.png'),pygame.image.load('images/right/r14.png'),pygame.image.load('images/right/r15.png'),pygame.image.load('images/right/r16.png'),pygame.image.load('images/right/r17.png'),pygame.image.load('images/right/r18.png')]
    walkLeft = [pygame.image.load('images/left/l1.png'),pygame.image.load('images/left/l2.png'),pygame.image.load('images/left/l3.png'),pygame.image.load('images/left/l4.png'),pygame.image.load('images/left/l5.png'),pygame.image.load('images/left/l6.png'),pygame.image.load('images/left/l7.png'),pygame.image.load('images/left/l8.png'),pygame.image.load('images/left/l9.png'),pygame.image.load('images/left/l10.png'),pygame.image.load('images/left/l11.png'),pygame.image.load('images/left/l12.png'),pygame.image.load('images/left/l13.png'),pygame.image.load('images/left/l14.png'),pygame.image.load('images/left/l15.png'),pygame.image.load('images/left/l16.png'),pygame.image.load('images/left/l17.png'),pygame.image.load('images/left/l18.png')]
    attackFront= [pygame.image.load('images/attacking/a1.png'),pygame.image.load('images/attacking/a2.png'),pygame.image.load('images/attacking/a3.png'),pygame.image.load('images/attacking/a4.png'),pygame.image.load('images/attacking/a5.png'),pygame.image.load('images/attacking/a6.png'),pygame.image.load('images/attacking/a7.png'),pygame.image.load('images/attacking/a8.png'),pygame.image.load('images/attacking/a9.png'),pygame.image.load('images/attacking/a10.png'),pygame.image.load('images/attacking/a11.png'),pygame.image.load('images/attacking/a12.png')]
    deadAnim = [pygame.image.load('images/dead/die1.png'),pygame.image.load('images/dead/die2.png'),pygame.image.load('images/dead/die3.png'),pygame.image.load('images/dead/die4.png'),pygame.image.load('images/dead/die5.png'),pygame.image.load('images/dead/die6.png'),pygame.image.load('images/dead/die7.png'),pygame.image.load('images/dead/die8.png'),pygame.image.load('images/dead/die9.png'),pygame.image.load('images/dead/die10.png'),pygame.image.load('images/dead/die11.png'),pygame.image.load('images/dead/die12.png')]
    char = pygame.image.load('images/standing.png')
    def __init__(self):
        #SET THE MOVEMENTS VARIABLES
        #positions
        self.x = 50
        self.y=370
        #dimensions for object collision the so called hitbox
        self.width = 200
        self.height = 162
        self.speed = 7
        self.isJump = False
        self.jumpCount = 11 #value of so called gravity for the game
        #Variables to determine the sprite facing position
        self.l = False #facing left
        self.r = False #facing right
        self.a = False #pressing attack
        self.walk_counter = 0 #char animator
        self.attack_counter = 0
        self.dead_counter = 0
        self.hsoundCount = 0 #value of the hit sound counter
        self.jsoundCount = 30 #jump sound counter
        self.ssoundCount = 0 #step sound counter
    #values for the hitbox
        self.xSpace = 40
        self.ySpace = 20
        self.hitObject = (self.x +self.xSpace, self.y+self.ySpace, self.width- self.xSpace*2, self.height- self.ySpace*2-10)#rectangle THE LAST 2 PARAMETERS ARE CONSIDERED HITBOX 
        self.health = 10
    def draw(self,win):
        if (self.walk_counter +1 >= 54):
            self.walk_counter = 0
        if (self.attack_counter +1 >= 36):
            self.attack_counter = 0

        if self.l:
            win.blit(self.walkLeft[self.walk_counter//3],(self.x,self.y))
            self.walk_counter +=1
        elif self.r:
            win.blit(self.walkRight[self.walk_counter//3],(self.x,self.y))
            self.walk_counter +=1
        elif self.a:#a is for attack
            win.blit(self.attackFront[self.attack_counter//3],(self.x,self.y))
            self.attack_counter+=1
            if self.attack_counter +1 >= 36:
                self.a = False
        else:
            win.blit(self.char, (self.x,self.y))
            self.walk_counter =0
            self.attack_counter= 0
        pygame.draw.rect(win,(255,0,0),(self.hitObject[0]+20,self.hitObject[1] -20,80,10))
        pygame.draw.rect(win,(0,255,0),(self.hitObject[0]+20,self.hitObject[1] -20,self.health*8,10))

        self.hitObject = (self.x +self.xSpace, self.y+self.ySpace, self.width- self.xSpace*2, self.height- self.ySpace*2-10)#added code for hitobject - rectangle
        #draw the rectangle hitbox
        #pygame.draw.rect(win,(255,0,0),self.hitObject,2)
    def drawDied(self,win):
        if self.dead_counter +1 >=36:
            win.blit(self.deadAnim[11],(self.x,self.y))
        else:
            win.blit(self.deadAnim[self.dead_counter//3],(self.x,self.y))
            self.dead_counter += 1
        

