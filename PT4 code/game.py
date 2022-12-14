#PT3 - OBJECT COLLISIONS
import pygame
from Player import player #from for file name the import can be the class name
from Projectile import projectile
from Projectile import buff
from Enemy import enemy
import random

pygame.init()
pygame.mixer.init()
wx = 1280
wy = 576
win = pygame.display.set_mode((wx,wy))#set the size of the window
pygame.display.set_caption("Farm Invaders")#set the title
pygame.display.update()

#IMPORT THE SPRITES AND SOUNDS
bg= pygame.image.load('images/bg3.jpg').convert_alpha()
lifeCtr = pygame.image.load('images/heart.png').convert_alpha()

#SOUNDS RESOURCE
pygame.mixer.music.load('sounds/bgm.wav')
pygame.mixer.music.set_volume(.1)
pygame.mixer.music.play(-1)

step = pygame.mixer.Sound('sounds/step.mp3')
jump =  pygame.mixer.Sound('sounds/jump.wav')
hit = pygame.mixer.Sound('sounds/hit.wav')
ddamage = pygame.mixer.Sound('sounds/ddamage.wav')
gover = pygame.mixer.Sound('sounds/gover.wav')

jump.set_volume(.10)#.1 for headphones
step.set_volume(.3)#.3 for headphones
ddamage.set_volume(.05)
gover.set_volume(.05)
score = 0
bulctr = 0 #counts the amount of bullets that should be present on the game window
lives = 3
damage = 1
buff_timer =0
once = True
mdpx=500 #monster dead position
mdpy = 250 
mdp1x= 500 #monster1 dead position
mdp1y = 250  

#INSTANTIATION OF THE CLASSES
play = player()#instance of player class
monster = enemy(1280,410,200,162,0)
monster1 = enemy(1280,110,200,162,0)
bullets = []
buffs = []

def redrawWindowGame():
    win.blit(bg, (0,0))#draw the bg at the position indicated
    for buff in buffs:
        buff.draw(win)
    play.draw(win)
    monster.draw(win,mdpx,mdpy)
    monster1.draw(win,mdp1x,mdp1y)
    life_x = 80
    life_y = 10
    for i in range (0,lives):
        win.blit(lifeCtr,(life_x,life_y))
        life_x+=50
    text = font.render('Score : '+str(score),1,(255,255,255))
    text2 = font.render('Lives: ',1,(255,255,255))
    win.blit(text,(1150,40))
    win.blit(text2,(5,20))
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

def drawEndGame():
    win.blit(bg, (0,0))
    play.drawDied(win)
    monster.draw(win,mdpx,mdpy)
    monster1.draw(win,mdpx,mdpy)
    creds = fontTitle.render('Game Over!',1,(255,0,0))
    fnlScore = fontTitle.render('Your total kills : '+str(score),1,(255,0,0))
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
        if(random.randint(0,1000)==9):
            buffs.append(buff(random.randint(0+play.width,wx-play.width),random.randint(0+play.height,wy-play.height)))
        bulctr =0
    elif score>=10 and score<20:
        if(random.randint(0,800)==9):
            buffs.append(buff(random.randint(0+play.width,wx-play.width),random.randint(0+play.height,wy-play.height)))
        bulctr =1
    elif score>=20 and score<30:
        if(random.randint(0,600)==9):
            buffs.append(buff(random.randint(0+play.width,wx-play.width),random.randint(0+play.height,wy-play.height)))
        bulctr =2
    elif score >= 30 and score<40:
        if(random.randint(0,400)==9):
            buffs.append(buff(random.randint(0+play.width,wx-play.width),random.randint(0+play.height,wy-play.height)))
        bulctr =3
    elif score >= 40:#This is the buff for 40+ score line randomly drops a double damage buff on the window that a player can pick up
        if(random.randint(0,200)==9):
            buffs.append(buff(random.randint(0+play.width,wx-play.width),random.randint(0+play.height,wy-play.height)))
    if buff_timer >=450:#10 seconds
        damage =1
        buff_timer = 0
        ddamage.stop()
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
    
    #check for bullet and monster collision
    for bullet in bullets:
        if bullet.x+10 >= monster.hitObject[0] and bullet.x+10 <= monster.hitObject[0] + monster.hitObject[2]:
            if bullet.y+10 >= monster.hitObject[1] and bullet.y+10 <= monster.hitObject[1] + monster.hitObject[3]:
                bullets.pop(bullets.index(bullet))
                if monster.hit(score,damage):
                    score+=1
                    mdpx = monster.deadx 
                    mdpy = monster.deady
                    monster.dead= True
                if monster.health <=0:#removes the scoring bug double checks the health of the enemy
                    score+=1
                    mdpx = monster.x 
                    mdpy = monster.y
                    monster.dead = True
                    monster.repos(score)
        if bullet.x+10 >= monster1.hitObject[0] and bullet.x+10 <= monster1.hitObject[0] + monster1.hitObject[2]:
            if bullet.y+10 >= monster1.hitObject[1] and bullet.y+10 <= monster1.hitObject[1] + monster1.hitObject[3]:
                bullets.pop(bullets.index(bullet))
                if monster1.hit(score,damage):
                    score+=1
                    mdp1x = monster1.deadx 
                    mdp1y = monster1.deady
                    monster1.dead= True
                if monster1.health <=0:
                    score+=1
                    mdp1x = monster1.x 
                    mdp1y = monster1.y
                    monster1.dead = True
                    monster1.repos(score)
        if bullet.x < wx and bullet.x > 0:#checks if the bullet is still on the window
            bullet.x += bullet.vel
        else:#if the bullet is not the remove it from the array
            bullets.pop(bullets.index(bullet))

    #checks for player and buff collision
    for buf in buffs:
        if buf.x+14 >= play.hitObject[0] and buf.x+14 <= play.hitObject[0] + play.hitObject[2]:
            if buf.init_y+25 >= play.hitObject[1] and buf.init_y+25 <= play.hitObject[1] + play.hitObject[3]:
                damage = 2
                buff_timer = 0
                ddamage.stop()
                ddamage.play(0)
                buffs.pop(buffs.index(buf))
        if buf.pop:#checks if the bullet expires
            buffs.pop(buffs.index(buf))
    buff_timer += 1
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
        elif (keys[pygame.K_w]and play.y > 10 and not play.isJump):#370 is the initial val of sprite
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
        #CHECKS for character collisions between enemy and player
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
        if play.hitObject[0] >= monster1.hitObject[0] and play.hitObject[0] <= monster1.hitObject[0]+monster1.hitObject[2]:#check the left of the player
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
            lives =0

    if lives <= 0:
        drawEndGame()
        pygame.mixer.music.set_volume(0)
        if once:
            ddamage.stop()
            gover.play(-1)
            once = False
    else:
        redrawWindowGame()
        
    #end of the MAIN LOOP

pygame.quit()
