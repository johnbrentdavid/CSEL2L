import pygame

pygame.init()
pygame.mixer.init()
wx = 1280
wy = 576
win = pygame.display.set_mode((wx,wy))#set the size of the window
pygame.display.set_caption("My PT1 Sprite Game")#set the title
pygame.display.update()

#IMPORT THE SPRITES AND SOUNDS
walkRight = [pygame.image.load('images/right/r1.png'),pygame.image.load('images/right/r2.png'),pygame.image.load('images/right/r3.png'),pygame.image.load('images/right/r4.png'),pygame.image.load('images/right/r5.png'),pygame.image.load('images/right/r6.png'),pygame.image.load('images/right/r7.png'),pygame.image.load('images/right/r8.png'),pygame.image.load('images/right/r9.png'),pygame.image.load('images/right/r10.png'),pygame.image.load('images/right/r11.png'),pygame.image.load('images/right/r12.png'),pygame.image.load('images/right/r13.png'),pygame.image.load('images/right/r14.png'),pygame.image.load('images/right/r15.png'),pygame.image.load('images/right/r16.png'),pygame.image.load('images/right/r17.png'),pygame.image.load('images/right/r18.png')]
walkLeft = [pygame.image.load('images/left/l1.png'),pygame.image.load('images/left/l2.png'),pygame.image.load('images/left/l3.png'),pygame.image.load('images/left/l4.png'),pygame.image.load('images/left/l5.png'),pygame.image.load('images/left/l6.png'),pygame.image.load('images/left/l7.png'),pygame.image.load('images/left/l8.png'),pygame.image.load('images/left/l9.png'),pygame.image.load('images/left/l10.png'),pygame.image.load('images/left/l11.png'),pygame.image.load('images/left/l12.png'),pygame.image.load('images/left/l13.png'),pygame.image.load('images/left/l14.png'),pygame.image.load('images/left/l15.png'),pygame.image.load('images/left/l16.png'),pygame.image.load('images/left/l17.png'),pygame.image.load('images/left/l18.png')]
attackFront= [pygame.image.load('images/attacking/a1.png'),pygame.image.load('images/attacking/a2.png'),pygame.image.load('images/attacking/a3.png'),pygame.image.load('images/attacking/a4.png'),pygame.image.load('images/attacking/a5.png'),pygame.image.load('images/attacking/a6.png'),pygame.image.load('images/attacking/a7.png'),pygame.image.load('images/attacking/a8.png'),pygame.image.load('images/attacking/a9.png'),pygame.image.load('images/attacking/a10.png'),pygame.image.load('images/attacking/a11.png'),pygame.image.load('images/attacking/a12.png'),]
bg= pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')
bul = pygame.image.load('images/bullet.png')
#SOUNDS RESOURCE
pygame.mixer.music.load('sounds/bgm.mp3')
pygame.mixer.music.set_volume(.1)
pygame.mixer.music.play(-1)

step = pygame.mixer.Sound('sounds/step.mp3')
jump =  pygame.mixer.Sound('sounds/jump.wav')
hit = pygame.mixer.Sound('sounds/hit.wav')

jump.set_volume(.10)#.1 for headphones
step.set_volume(.3)#.3 for headphones

#NEW CLASS FOR HANDLING PLAYER OBJECTS
class player(object):
    def __init__(self,x,y,width,height):
        #SET THE MOVEMENTS VARIABLES
        #positions
        self.x = 50
        self.y=370
        #dimensions for object collision
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
        self.hsoundCount = 0 #value of the hit sound counter
        self.jsoundCount = 30 #jump sound counter
        self.ssoundCount = 0 #step sound counter
    def draw(self,win):
        if (self.walk_counter +1 >= 30):
            self.walk_counter = 0
        if self.l:
            win.blit(walkLeft[self.walk_counter//3],(self.x,self.y))
            self.walk_counter +=1
        elif self.r:
            win.blit(walkRight[self.walk_counter//3],(self.x,self.y))
            self.walk_counter +=1
        elif self.a:#a is for attack
            win.blit(attackFront[self.walk_counter//3],(self.x,self.y))
            self.walk_counter+=1
        else:
            win.blit(char, (self.x,self.y))
            self.walk_counter =0

#NEW CLASS FOR HANDLING PROJECTILES
class projectile(object):
    def __init__(self,x,y,radius,color, facing):
        self.x = x
        self.y=y
        self.radius = radius
        self.color= color
        self.facing= facing
        self.vel = 8 *facing#speed of the projectile
    def draw(self,window):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
        window.blit(bul,(self.x-10,self.y-10))


play = player(200,410,60,60)#instance of player class
bullets = []

def redrawWindowGame():
    play.walk_counter
    win.blit(bg, (0,0))#draw the bg at the position indicated
    play.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

clock = pygame.time.Clock()
play = player(200,410,60,60)#instance of player class
run = True
#MAIN GAME LOOP
while run:
    clock.tick(45)#frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#conditional to stop the game if X is pressed
            run = False
    #add projectile class in main loop
    for bullet in bullets:
        if bullet.x < wx and bullet.x > 0:#checks if the bullet is still on the window
            bullet.x += bullet.vel
        else:#if the bullet is not the remove it from the array
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    mkeys = pygame.mouse.get_pressed()
#2nd condition sets the boundaries where u can only walk
    if (keys[pygame.K_d] and play.x< wx - play.speed - play.width ):
        if(play.ssoundCount ==0):
            step.play(0)
            play.ssoundCount = 30
        else:
            play.ssoundCount -=1
        play.x += play.speed
        play.l = False
        play.r = True
    elif (keys[pygame.K_a] and play.x> play.speed ):
        if(play.ssoundCount ==0):
            step.play(0)
            play.ssoundCount = 30
        else:
            play.ssoundCount -=1
        play.x-=play.speed
        play.l = True
        play.r = False
    elif (keys[pygame.K_s]and play.y < wy - play.speed- play.height+37 and not play.isJump): #not isJump is added as a condition to avoid getting out of bounds
        if(play.ssoundCount ==0):
            step.play(0)
            play.ssoundCount = 30
        else:
            play.ssoundCount -=1
        play.y+=play.speed
        play.l = False
        play.r = True
    elif (keys[pygame.K_w]and play.y > 370 and not play.isJump):#370 is the initial val of sprite
        if(play.ssoundCount ==0):
            step.play(0)
            play.ssoundCount = 30
        else:
            play.ssoundCount -=1
        play.y-=play.speed
        play.l = False
        play.r = True
#conditional for left-mouse click
    elif(mkeys[0] and not play.isJump):
        if (play.hsoundCount == 30):
            bullets.append(projectile((play.x + play.width//2),round(play.y+play.height//2),6,(0,0,0),facing))
            hit.play(0)
            play.hsoundCount = 0
        else:
            play.hsoundCount +=1
        play.l = False
        play.r = False
        play.a = True
        facing = 1
        

#if the character is not moving
    else:
        play.l = False
        play.r = False
        play.walk_counter =0
        play.ssoundCount = 0
        play.hsoundCount = 0
#CONDITIONAL FOR JUMPING
    if not(play.isJump):
        if (keys[pygame.K_SPACE]):
            play.isJump = True
            play.right = False
            play.Left = False
            play.walk_counter =0 
    else:
        
        if(play.jumpCount >= -11):
            if(play.jumpCount == 11):#condition to check if code should play the sound
                if (play.jsoundCount ==30):
                    jump.play(0)
                    play.jsoundCount = 0
            play.y -= (play.jumpCount *abs(play.jumpCount)) *.5
            play.jumpCount -=1
        else:
            play.jsoundCount = 30
            play.jumpCount = 11 
            play.isJump = False
    redrawWindowGame()
    #end of the MAIN LOOP
pygame.quit()
#forgot the last line of code