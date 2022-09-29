import pygame
pygame.init()

game_win = pygame.display.set_mode((500,500))
pygame.display.set_caption("OE3_David")

#set the row,col top-left
x = 200
y = 200
width = 50
height = 50

#2nd rectangle- top-right
bix = 250
biy =200
biwidth =50
biheight =50

#third rec bot-left
trix = 200
triy = 250
triwidth = 50
triheight = 50

#4th rec bot-right
quadx = 250
quady = 250
quadwidth = 50
quadheight = 50

#CONSTANT
speed = 5

#variables to set jump movement
isJump = False
jumpCount =10


run = True
while run:
    pygame.time.delay(100)#delay the game movement in ms

    for event in pygame.event.get():#loop through a list of any key or mouse event
        if event.type == pygame.QUIT:
            print("Thank You!")
            run = False #END THE GAME LOOP

    keys = pygame.key.get_pressed()#list of keys to use

    #CHECK which key is pressed
    if keys[pygame.K_LEFT] and x>speed:
        x-= speed
        quadx +=speed
    if keys[pygame.K_RIGHT] and x<500 - speed - width:
        x+= speed
        quadx-= speed
    if keys[pygame.K_UP]  and y>speed:
        y-= speed
        quady+=speed
    if keys[pygame.K_DOWN] and  y<500 - speed- height:
        y+= speed
        quady -=speed
    #keys for the bottom left square
    if keys[pygame.K_a] and trix>speed:#left
        bix += speed
        trix -= speed
    if keys[pygame.K_d] and trix< 500-speed-triwidth:#rght
        bix -= speed
        trix += speed
    if keys[pygame.K_s]and triy <500-speed-triheight:#down
        biy-= speed
        triy +=speed
    if keys[pygame.K_w] and triy>speed:#up
        biy += speed
        triy-= speed

        
    #JUMPING CONDITIONAL
    if not(isJump):#check the user not jumping
        if keys[pygame.K_SPACE]:
            isJump =True
    else:#happens if user is jumping
        if jumpCount >= -10:#this sets the action for the jump
            y-= (jumpCount*abs(jumpCount))*.5
            quady+= (jumpCount*abs(jumpCount))*.5
            triy+= (jumpCount*abs(jumpCount))*.5
            biy-= (jumpCount*abs(jumpCount))*.5
        
            jumpCount -= 1
        else:
            jumpCount =10
            isJump = False

    game_win.fill((255,255,255))#fill with black binubura nya yung previous pos na squares
    pygame.draw.rect(game_win, (0,120,212),(x,y,width,height))#top-left
    pygame.draw.rect(game_win, (45,92,127),(bix,biy,biwidth,biheight))#top-right rect

    pygame.draw.rect(game_win, (45,92,127),(trix,triy,triwidth,triheight))#bottom-left rect
    pygame.draw.rect(game_win, (0,120,212),(quadx,quady,quadwidth,quadheight))#bottom-right rect
    
    pygame.display.update()#enable to update the screen

pygame.quit()

#OE2 ADDITIONS - new shape with different key bind