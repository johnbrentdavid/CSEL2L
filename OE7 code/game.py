#OE6 - OBJECT COLLISIONS
import pygame
from Player import player #from for file name the import can be the class name
from Projectile import projectile
from Enemy import enemy

pygame.init()
pygame.mixer.init()
wx = 1280
wy = 576
win = pygame.display.set_mode((wx,wy))#set the size of the window
pygame.display.set_caption("PT2 Game version")#set the title
pygame.display.update()

#IMPORT THE SPRITES AND SOUNDS
bg= pygame.image.load('images/bg2.jpg')
lifeCtr = pygame.image.load('images/heart.png')

#SOUNDS RESOURCE
pygame.mixer.music.load('sounds/bgm.mp3')
pygame.mixer.music.set_volume(.1)
pygame.mixer.music.play(-1)

step = pygame.mixer.Sound('sounds/step.mp3')
jump =  pygame.mixer.Sound('sounds/jump.wav')
hit = pygame.mixer.Sound('sounds/hit.wav')

jump.set_volume(.10)#.1 for headphones
step.set_volume(.3)#.3 for headphones

score = 0
bulctr = 0 #counts the amount of bullets that should be present on the game window
lives = 3

#INSTANTIATION OF THE CLASSES
play = player()#instance of player class
monster = enemy(1280,410,200,162,0)
monster1 = enemy(1280,110,200,162,0)
bullets = []

def redrawWindowGame():
    play.walk_counter
    win.blit(bg, (0,0))#draw the bg at the position indicated
    play.draw(win)
    monster.draw(win)
    monster1.draw(win)
    life_x = 80
    life_y = 10
    for i in range (0,lives):
        win.blit(lifeCtr,(life_x,life_y))
        life_x+=50
    text = font.render('Score : '+str(score),1,(255,255,255))
    text2 = font.render('Lives: ',1,(255,255,255))
    win.blit(text,(1150,10))
    win.blit(text2,(5,20))
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

def drawEndGame():
    win.blit(bg, (0,0))
    play.drawDied(win)
    monster.draw(win)
    monster1.draw(win)
    creds = fontTitle.render('Game Over!',1,(0,0,0))
    fnlScore = fontTitle.render('Your total kills : '+str(score),1,(0,0,0))
    win.blit(creds,(550,260))
    win.blit(fnlScore,(475,310))
    pygame.display.update()

clock = pygame.time.Clock()
run = True
font = pygame.font.Font('fontstyles/SummerPixel22Regular-jE0W7.ttf',25)
fontTitle = pygame.font.Font('fontstyles/SummerPixel22Regular-jE0W7.ttf',40)
#MAIN GAME LOOP
while run:
    clock.tick(45)#frame rate

    #Game Balancing
    if score<10:
        bulctr =0
    elif score>=10 and score<20:
        bulctr =1
    elif score>=20 and score<30:
        bulctr =2
    elif score >= 30 and score<40:
        bulctr =3
    elif score >= 40:
        bulctr =4

    #Game Player Lives counter
    if(monster.x >= -199 and monster.x <= -150):
        lives -=1
        monster.x =1280
    if monster1.x >= -199 and monster1.x <= -150:
        lives-=1
        monster1.x= 1280
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#conditional to stop the game if X is pressed
            run = False
    #add projectile class in main loop
    for bullet in bullets:
        if bullet.x+10 >= monster.hitObject[0] and bullet.x+10 <= monster.hitObject[0] + monster.hitObject[2]:
            if bullet.y+10 >= monster.hitObject[1] and bullet.y+10 <= monster.hitObject[1] + monster.hitObject[3]:
                bullets.pop(bullets.index(bullet))
                if monster.hit(score):
                    score+=1
        elif bullet.x+10 >= monster1.hitObject[0] and bullet.x+10 <= monster1.hitObject[0] + monster1.hitObject[2]:
            if bullet.y+10 >= monster1.hitObject[1] and bullet.y+10 <= monster1.hitObject[1] + monster1.hitObject[3]:
                bullets.pop(bullets.index(bullet))
                if(monster1.hit(score)):
                    score+=1
        if bullet.x < wx and bullet.x > 0:#checks if the bullet is still on the window
            bullet.x += bullet.vel
        else:#if the bullet is not the remove it from the array
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    mkeys = pygame.mouse.get_pressed()

#2nd condition sets the boundaries where u can only walk
    if lives >0:
        if(mkeys[0] and not play.isJump and len(bullets) <=bulctr):
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
        elif (keys[pygame.K_w]and play.y > 100 and not play.isJump):#370 is the initial val of sprite
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
        #CHECKS for character collisions between enemy and playerd
        if play.hitObject[0] >= monster.hitObject[0] and play.hitObject[0] <= monster.hitObject[0]+monster.hitObject[2]:#check the left of the player
            if play.hitObject[1] >= monster.hitObject[1] and play.hitObject[1] <= monster.hitObject[1]+monster.hitObject[3]:
                monster.x = 1280
                play.health -= 1
            elif play.hitObject[1]+play.hitObject[3] >= monster.hitObject[1] and play.hitObject[1]+play.hitObject[3] <= monster.hitObject[1]+monster.hitObject[3]:
                monster.x = 1280
        elif play.hitObject[0]+play.hitObject[2] >= monster.hitObject[0] and play.hitObject[0]+play.hitObject[2] <= monster.hitObject[0]+monster.hitObject[2]:
            if play.hitObject[1] >= monster.hitObject[1] and play.hitObject[1] <= monster.hitObject[1]+monster.hitObject[3]:
                monster.x = 1280
                play.health -= 1
            elif play.hitObject[1]+play.hitObject[3] >= monster.hitObject[1] and play.hitObject[1]+play.hitObject[3] <= monster.hitObject[1]+monster.hitObject[3]:
                monster.x = 1280
                play.health -= 1
        elif play.hitObject[0] >= monster1.hitObject[0] and play.hitObject[0] <= monster1.hitObject[0]+monster1.hitObject[2]:#check the left of the player
            if play.hitObject[1] >= monster1.hitObject[1] and play.hitObject[1] <= monster1.hitObject[1]+monster1.hitObject[3]:
                monster1.x = 1280
                play.health -= 1
            elif play.hitObject[1]+play.hitObject[3] >= monster1.hitObject[1] and play.hitObject[1]+play.hitObject[3] <= monster1.hitObject[1]+monster1.hitObject[3]:
                monster1.x = 1280
                play.health -= 1
        elif play.hitObject[0]+play.hitObject[2] >= monster1.hitObject[0] and play.hitObject[0]+play.hitObject[2] <= monster1.hitObject[0]+monster1.hitObject[2]:
            if play.hitObject[1] >= monster1.hitObject[1] and play.hitObject[1] <= monster1.hitObject[1]+monster1.hitObject[3]:
                monster1.x = 1280
                play.health -= 1
            elif play.hitObject[1]+play.hitObject[3] >= monster1.hitObject[1] and play.hitObject[1]+play.hitObject[3] <= monster1.hitObject[1]+monster1.hitObject[3]:
                monster1.x = 1280
                play.health -= 1
        
        if play.health == 0:
            play.health =10
            lives -= 1

    if lives <= 0:
        drawEndGame()
    else:
        redrawWindowGame()
    #end of the MAIN LOOP
pygame.quit()
