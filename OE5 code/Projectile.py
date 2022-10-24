import pygame

#NEW CLASS FOR HANDLING PROJECTILES
class projectile(object):
    bul = pygame.image.load('images/bullet.png')
    def __init__(self,x,y,radius,color, facing):
        self.x = x
        self.y=y
        self.radius = radius
        self.color= color
        self.facing= facing
        self.vel = 8 *facing#speed of the projectile
    def draw(self,window):
        window.blit(self.bul,(self.x-10,self.y-10))