import pygame
from Player import player
from Projectile import projectile
from Enemy import enemy

pygame.init()
pygame.mixer.init()
wx = 1280
wy = 576
win = pygame.display.set_mode((wx,wy))#set the size of the window
pygame.display.set_caption("OE5 version Game")#set the title
pygame.display.update()

#IMPORT THE SPRITES AND SOUNDS
bg= pygame.image.load('images/bg.jpg')

#SOUNDS RESOURCE
pygame.mixer.music.load('sounds/bgm.mp3')
pygame.mixer.music.set_volume(.1)
pygame.mixer.music.play(-1)

step = pygame.mixer.Sound('sounds/step.mp3')
jump =  pygame.mixer.Sound('sounds/jump.wav')
hit = pygame.mixer.Sound('sounds/hit.wav')

jump.set_volume(.10)#.1 for headphones
step.set_volume(.3)#.3 for headphones

#INSTANTIATION OF THE CLASSES
play = player()#instance of player class
monster = enemy(1280,410,200,162,0)
bullets = []

def redrawWindowGame():
    play.walk_counter
    win.blit(bg, (0,0))#draw the bg at the position indicated
    play.draw(win)
    monster.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

clock = pygame.time.Clock()
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
    if(mkeys[0] and not play.isJump and len(bullets) <=1):
        if (play.hsoundCount == 33):
            bullets.append(projectile((play.x + play.width//2),round(play.y+play.height//2),6,(0,0,0),facing))
            hit.play(0)
            play.hsoundCount = 0
            play.a = False
        else:
            play.hsoundCount +=1
        play.l = False
        play.r = False
        play.a = True
        facing = 1
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
    elif (keys[pygame.K_d] and play.x< wx - play.speed - play.width ):
        if(play.ssoundCount ==0):
            step.play(0)
            play.ssoundCount = 30
        else:
            play.ssoundCount -=1
        play.x += play.speed
        play.l = False
        play.r = True
#if the character is not moving
    else:
        play.l = False
        play.r = False
        play.a = False
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