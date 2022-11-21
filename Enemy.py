import pygame
import random
#NEW CLASS FOR ENEMY
class enemy(object):
    walkLeft = [pygame.image.load('images/enemy/l1.png'),pygame.image.load('images/enemy/l2.png'),pygame.image.load('images/enemy/l3.png'),pygame.image.load('images/enemy/l4.png'),pygame.image.load('images/enemy/l5.png'),pygame.image.load('images/enemy/l6.png'),pygame.image.load('images/enemy/l7.png'),pygame.image.load('images/enemy/l8.png'),pygame.image.load('images/enemy/l9.png'),pygame.image.load('images/enemy/l10.png'),pygame.image.load('images/enemy/l11.png'),pygame.image.load('images/enemy/l12.png'),pygame.image.load('images/enemy/l13.png'),pygame.image.load('images/enemy/l14.png'),pygame.image.load('images/enemy/l15.png'),pygame.image.load('images/enemy/l16.png'),pygame.image.load('images/enemy/l17.png'),pygame.image.load('images/enemy/l18.png')]
    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x,end]
        self.walkCount = 0
        self.vel = 3
        self.health = 2
    #values for the hitbox
        self.xSpace = 40
        self.ySpace = 20
        self.hitObject = (self.x +self.xSpace, self.y, self.width- self.xSpace*2, self.height)#rectangle THE LAST 2 PARAMETERS ARE CONSIDERED HITBOX 

    def draw(self,win):
        self.move()
        if self.walkCount +1 >=54: #3 frames x 18 images animate it in only 3 images
            self.walkCount = 0
        if self.vel >0:#condition for movement of the enemy
            win.blit(self.walkLeft[self.walkCount//3],[self.x,self.y])#3 is the frames from the first one
            self.walkCount +=1
        self.hitObject = (self.x +self.xSpace, self.y+self.ySpace, self.width- self.xSpace*2, self.height- self.ySpace*2-10)#added code for hitobject - rectangle
        
        pygame.draw.rect(win,(255,0,0),(self.hitObject[0]+20,self.hitObject[1] -20,80,10))
        pygame.draw.rect(win,(0,255,0),(self.hitObject[0]+20,self.hitObject[1] -20,self.health*8,10))
        #draw the rectangle hitbox
        #pygame.draw.rect(win,(255,0,0),self.hitObject,2)

    def move(self):#
        if self.vel >0:#checks if moving
            if self.x > self.path[1] - self.width:#if not yet reach the farthest left
                self.x -= self.vel
            else:#reach the leftmost part of the screen
                self.x =1280
                self.walkCount = 0
    
    def hit(self,score):
        if self.health > 1:
            self.health -= 1
            return False
        else:
            self.x = 1280
            self.y = random.randint(100,444)
            if score<10:#5 vel for this hp
                self.health =2
            elif score>=10 and score<20:#4 vel for this hp
                self.health = random.randint(2,4)
                self.vel= self.speed(self.health)
            elif score>=20 and score<30:#3 vel for this hp
                self.health = random.randint(2,6)
                self.vel= self.speed(self.health)
            elif score >= 30 and score<40:#2 vel for this hp
                self.health = random.randint(2,8)
                self.vel= self.speed(self.health)
            elif score >= 40:#1 vel for this hp
                self.health = random.randint(2,10)
                self.vel= self.speed(self.health)
            return True
    #dictates the balance speed for the hp
    def speed(self,health):
        if health ==3 or health ==4:
            return 4
        elif health ==5 or health ==6:
            return 3
        elif health ==7 or health ==8:
            return 2
        elif health ==9 or health ==10:
            return 1
        return 5