import pygame
pygame.init()

game_win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

#set the row,col
x = 50
y = 50
width = 40
height = 40

#2nd rectangle
bix = 400
biy =50
biwidth =40
biheight =40

#third rec
trix = 50
triy = 400
triwidth = 40
triheight = 40

#4th rec
quadx = 400
quady = 400
quadwidth = 40
quadheight = 40

#CONSTANT
speed = 5


run = True
while run:
    pygame.time.delay(100)#delay the game movement in ms

    for event in pygame.event.get():#loop through a list of any key or mouse event
        if event.type == pygame.QUIT:
            print("Thank You!")
            run = False #END THE GAME LOOP
    keys = pygame.key.get_pressed()#list of keys to use
    #CHECK which key is pressed
    if keys[pygame.K_LEFT]:
        x-= speed
        quadx +=speed
    if keys[pygame.K_RIGHT]:
        x+= speed
        quadx-= speed
    if keys[pygame.K_UP]:
        y-= speed
        quady+=speed
    if keys[pygame.K_DOWN]:
        y+= speed
        quady -=speed
    #keys for the bottom left square
    if keys[pygame.K_a]:#left
        bix += speed
        trix -= speed
    if keys[pygame.K_d]:#rght
        bix -= speed
        trix += speed
    if keys[pygame.K_s]:#down
        biy-= speed
        triy +=speed
    if keys[pygame.K_w]:#up
        biy += speed
        triy-= speed
    

    game_win.fill((255,255,255))#fill with black binubura nya yung previous pos na squares
    pygame.draw.rect(game_win, (255,0,0),(x,y,width,height))#window surface drawing a square,
    pygame.draw.rect(game_win, (37,77,144),(bix,biy,biwidth,biheight))#top-right rect

    pygame.draw.rect(game_win, (37,77,144),(trix,triy,triwidth,triheight))#bottom-left rect
    pygame.draw.rect(game_win, (255,0,0),(quadx,quady,quadwidth,quadheight))#bottom-right rect
    
    pygame.display.update()#enable to update the screen

pygame.quit()

#OE2 ADDITIONS - new shape with different key bind