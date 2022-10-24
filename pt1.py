import pygame

pygame.init()
pygame.mixer.init()
wx = 1280
wy = 576
win = pygame.display.set_mode((wx,wy))#set the size of the window
pygame.display.set_caption("My PT1 Sprite Game")#set the title
pygame.display.update()

#Variables to determine the sprite facing position
l = False #facing lefta
r = False #facing righta
a = False #pressing attack
walk_counter = 0 #char animator
hsoundCount = 0 #value of the hit sound counter
jsoundCount = 30 #jump sound counter
ssoundCount = 0 #step sound counter

#SET THE MOVEMENTS VARIABLES
#positions
x = 50
y=370
#dimensions for object collision
width = 200
height = 162

speed = 7
isJump = False
jumpCount = 11 #value of so called gravity for the game


#IMPORT THE SPRITES AND SOUNDS
walkRight = [pygame.image.load('images/right/r1.png'),pygame.image.load('images/right/r2.png'),pygame.image.load('images/right/r3.png'),pygame.image.load('images/right/r4.png'),pygame.image.load('images/right/r5.png'),pygame.image.load('images/right/r6.png'),pygame.image.load('images/right/r7.png'),pygame.image.load('images/right/r8.png'),pygame.image.load('images/right/r9.png'),pygame.image.load('images/right/r10.png'),pygame.image.load('images/right/r11.png'),pygame.image.load('images/right/r12.png'),pygame.image.load('images/right/r13.png'),pygame.image.load('images/right/r14.png'),pygame.image.load('images/right/r15.png'),pygame.image.load('images/right/r16.png'),pygame.image.load('images/right/r17.png'),pygame.image.load('images/right/r18.png')]
walkLeft = [pygame.image.load('images/left/l1.png'),pygame.image.load('images/left/l2.png'),pygame.image.load('images/left/l3.png'),pygame.image.load('images/left/l4.png'),pygame.image.load('images/left/l5.png'),pygame.image.load('images/left/l6.png'),pygame.image.load('images/left/l7.png'),pygame.image.load('images/left/l8.png'),pygame.image.load('images/left/l9.png'),pygame.image.load('images/left/l10.png'),pygame.image.load('images/left/l11.png'),pygame.image.load('images/left/l12.png'),pygame.image.load('images/left/l13.png'),pygame.image.load('images/left/l14.png'),pygame.image.load('images/left/l15.png'),pygame.image.load('images/left/l16.png'),pygame.image.load('images/left/l17.png'),pygame.image.load('images/left/l18.png')]
attackFront = [pygame.image.load('images/attacking/a1.png'),pygame.image.load('images/attacking/a2.png'),pygame.image.load('images/attacking/a3.png'),pygame.image.load('images/attacking/a4.png'),pygame.image.load('images/attacking/a5.png'),pygame.image.load('images/attacking/a6.png'),pygame.image.load('images/attacking/a7.png'),pygame.image.load('images/attacking/a8.png'),pygame.image.load('images/attacking/a9.png'),pygame.image.load('images/attacking/a10.png'),pygame.image.load('images/attacking/a11.png'),pygame.image.load('images/attacking/a12.png'),]
bg= pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')
#SOUNDS RESOURCE
pygame.mixer.music.load('sounds/bgm.mp3')
pygame.mixer.music.set_volume(.1)
pygame.mixer.music.play(-1)

step = pygame.mixer.Sound('sounds/step.mp3')
jump =  pygame.mixer.Sound('sounds/jump.wav')
hit = pygame.mixer.Sound('sounds/hit.wav')

jump.set_volume(.10)#.3 for headphones
step.set_volume(.3)#.3 for headphones

def redrawWindowGame():
    global walk_counter
    win.blit(bg, (0,0))#draw the bg at the position indicated
    if (walk_counter +1 >= 30):
        walk_counter = 0
    if l:
        win.blit(walkLeft[walk_counter//3],(x,y))
        walk_counter +=1
    elif r:
        win.blit(walkRight[walk_counter//3],(x,y))
        walk_counter +=1
    elif a:#a is for attack
        win.blit(attackFront[walk_counter//3],(x,y))
        walk_counter+=1
    else:
        win.blit(char, (x,y))
        walk_counter =0
    pygame.display.update()

clock = pygame.time.Clock()

#MAIN GAME LOOP
run = True
while run:
    clock.tick(45)#frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#conditional to stop the game if X is pressed
            run = False

    keys = pygame.key.get_pressed()
    mkeys = pygame.mouse.get_pressed()
#2nd condition sets the boundaries where u can only walk
    if (keys[pygame.K_d] and x< wx - speed - width ):
        if(ssoundCount ==0):
            step.play(0)
            ssoundCount = 30
        else:
            ssoundCount -=1
        x += speed
        l = False
        r = True
    elif (keys[pygame.K_a] and x> speed ):
        if(ssoundCount ==0):
            step.play(0)
            ssoundCount = 30
        else:
            ssoundCount -=1
        x-=speed
        l = True
        r = False
    elif (keys[pygame.K_s]and y < wy - speed- height+37 and not isJump): #not isJump is added as a condition to avoid getting out of bounds
        if(ssoundCount ==0):
            step.play(0)
            ssoundCount = 30
        else:
            ssoundCount -=1
        y+=speed
        l = False
        r = True
    elif (keys[pygame.K_w]and y > 370 and not isJump):#370 is the initial val of sprite
        if(ssoundCount ==0):
            step.play(0)
            ssoundCount = 30
        else:
            ssoundCount -=1
        y-=speed
        l = False
        r = True
#conditional for left-mouse click
    elif(mkeys[0] and not isJump):
        if (hsoundCount == 30):
            hit.play(0)
            hsoundCount = 0
        else:
            hsoundCount +=1
        l = False
        r = False
        a = True
#if the character is not moving
    else:
        l = False
        r = False
        walk_counter =0
        ssoundCount = 0
        hsoundCount = 0
#CONDITIONAL FOR JUMPING
    if not(isJump):
        if (keys[pygame.K_SPACE]):
            isJump = True
            right = False
            Left = False
            walk_counter =0 
    else:
        
        if(jumpCount >= -11):
            if(jumpCount == 11):#condition to check if code should play the sound
                if (jsoundCount ==30):
                    jump.play(0)
                    jsoundCount = 0
            y -= (jumpCount *abs(jumpCount)) *.5
            jumpCount -=1
        else:
            jsoundCount = 30
            jumpCount = 11 
            isJump = False
    redrawWindowGame()
    #end of the MAIN LOOP
pygame.quit()
#forgot the last line of code