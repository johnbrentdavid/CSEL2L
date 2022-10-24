import pygame
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
    def draw(self,win):
        self.move()
        if self.walkCount +1 >=54: #3 frames x 18 images animate it in only 3 images
            self.walkCount = 0
        if self.vel >0:#condition for movement of the enemy
            win.blit(self.walkLeft[self.walkCount//3],[self.x,self.y])#3 is the frames from the first one
            self.walkCount +=1
        
    def move(self):#
        if self.vel >0:#checks if moving
            if self.x > self.path[1] - self.width:#if not yet reach the farthest left
                self.x -= self.vel
            else:
                self.x =1280
                self.walkCount = 0
        
