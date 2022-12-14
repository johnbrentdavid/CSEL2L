import pygame
import random
#NEW CLASS FOR HANDLING PROJECTILES
class projectile(object):
    bul = pygame.image.load('images/bullet.png')
    def __init__(self,x,y,radius,color, facing):
        self.x = x
        self.y=y
        self.radius = radius
        self.color= color
        self.facing= facing
        self.vel = 12 *facing#speed of the projectile
    def draw(self,window):
        window.blit(self.bul,(self.x-10,self.y-10))

class buff(object):#object for buff
    buff = pygame.image.load('images/buff.png')
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.init_y = -20
        self.fallSpeed = 3
        self.timer = 0
        self.pop = False

    def draw(self,window):
        if self.init_y <= self.y:
            window.blit(self.buff,(self.x-14,self.init_y -25))
            self.init_y += self.fallSpeed
        else: 
            if self.timer >=225:#should stay for 5 seconds after landing
                window.blit(self.buff,(self.x-14,self.init_y -25))
                self.pop = True
            else:
                window.blit(self.buff,(self.x-14,self.init_y -25))
                self.timer += 1



