import pygame, sys
from pygame.locals import *
import random
#variables for pacmans initial position
st_x = 480
st_x1 = 60
st_x2 = 900
st_x3 =60
st_x4 = 900
st_y = 420
st_y1 = 60
st_y2 = 60
st_y3 = 780
st_y4 = 780
st_x_change = 0 # adder for movement after keypress ,variable
st_x1_change = 0
st_x2_change = 0
st_x3_change = 0
st_x4_change = 0
st_y_change = 0 # adder for movement after keypress ,variable
st_y1_change = 0
st_y2_change = 0
st_y3_change = 0
st_y4_change = 0
move = 0
move_1 = 0
move_2 = 0
move_3 = 0
move_4 = 0
FPS = 7.5
Up = 0
Down = 1
Left = 2
Right = 3

#constants representing colours
BLACK=(0,0,0)
WHITE=(255,255,255)
#constants representing the different resources
ROCK = 0
PATH = 1

#a dicitonary linking resources to colours
colours={
    PATH : WHITE,
    ROCK : BLACK,
    }

#a list representing our tilemap
tilemap= [
    [ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK],
    [ROCK, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ROCK, PATH, PATH, PATH, PATH, PATH, ROCK],
    [ROCK, PATH, ROCK, PATH, ROCK, ROCK, PATH, ROCK, ROCK, PATH, PATH, PATH, ROCK, ROCK, ROCK, PATH, ROCK],
    [ROCK, PATH, PATH, PATH, PATH, ROCK, PATH, PATH, PATH, PATH, PATH, PATH, ROCK, ROCK, ROCK, PATH, ROCK],
    [ROCK, ROCK, PATH, ROCK, PATH, PATH, ROCK, ROCK, PATH, PATH, PATH, PATH, PATH, PATH, ROCK, PATH, ROCK],
    [ROCK, PATH, PATH, ROCK, PATH, PATH, PATH, PATH, PATH, ROCK, ROCK, ROCK, PATH, PATH, ROCK, PATH, ROCK],
    [ROCK, ROCK, PATH, ROCK, ROCK, PATH, PATH, PATH, PATH, ROCK, PATH, PATH, PATH, PATH, PATH, PATH, ROCK],
    [ROCK, PATH, PATH, ROCK, ROCK, ROCK, ROCK, PATH, PATH, PATH, PATH, PATH, PATH, ROCK, ROCK, PATH, ROCK],
    [ROCK, PATH, PATH, ROCK, PATH, PATH, PATH, PATH, PATH, PATH, ROCK, ROCK, PATH, PATH, PATH, ROCK, ROCK],
    [ROCK, PATH, PATH, PATH, PATH, ROCK, ROCK, ROCK, PATH, PATH, PATH, PATH, PATH, ROCK, PATH, PATH, ROCK],
    [ROCK, ROCK, ROCK, PATH, PATH, PATH, PATH, PATH, PATH, ROCK, PATH, ROCK, PATH, ROCK, ROCK, PATH, ROCK],
    [ROCK, PATH, PATH, PATH, ROCK, ROCK, PATH, PATH, PATH, ROCK, PATH, PATH, PATH, PATH, ROCK, PATH, ROCK],
    [ROCK, ROCK, ROCK, PATH, PATH, ROCK, ROCK, PATH, PATH, PATH, ROCK, ROCK, PATH, PATH, ROCK, PATH, ROCK],
    [ROCK, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ROCK, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ROCK],
    [ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK]
    ]

#useful game dimensions
TILESIZE=60
MAPWIDTH=17
MAPHEIGHT=15

#set up the display
pygame.init()
DISPLAYSURF=pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
time = pygame.time.Clock()# For fps
pygame.display.set_caption("B-man 4")
player = pygame.image.load('pacman_sp(60x60).png')
orange = pygame.image.load('orange-ghost.png')
blue = pygame.image.load('lightblue-ghost.png')
red = pygame.image.load('red-ghost.png')
pink = pygame.image.load('pink-ghost.png')
while True :
    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type== QUIT :
            #end the game and close the window
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # movment code after key is pressed
            if event.key == pygame.K_RIGHT:
                st_x_change = 60
                move = True
            elif event.key == pygame.K_DOWN:
                st_y_change = 60
                move = False
            elif event.key == pygame.K_LEFT:
                st_x_change = -60
                move = True
            elif event.key == pygame.K_UP:
                st_y_change = -60
                move = False
    for row in range(0,MAPHEIGHT) :
         for column in range(0,MAPWIDTH):
        #draw the resource at the position in the tilemap, using the correct colour
            pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE, row*TILESIZE,TILESIZE,TILESIZE))
    if move == True:
        if st_x_change < 0 :
            x=int((st_x+st_x_change)/60)
            y=int((st_y)/60)
            if tilemap[y][x] is not ROCK :           
                st_x = st_x_change + st_x
        if st_x_change>0 :
            x=int((st_x+st_x_change)/60)
            y=int((st_y)/60)
            if tilemap[y][x] is not ROCK :           
                st_x = st_x_change + st_x
    if move == False :
        if st_y_change<0 :
            x=int(st_x/60)
            y=int((st_y+st_y_change)/60)
            if tilemap[y][x] is not ROCK :
                st_y = st_y + st_y_change
        if st_y_change>0:
            x=int(st_x/60)
            y=int((st_y + st_y_change)/60)
            if tilemap[y][x] is not ROCK:
                st_y = st_y_change + st_y
    direction = random.randint(0,4)
    direction1 = random.randint(0,4)
    direction2 = random.randint(0,4)
    direction3 = random.randint(0,4)

    
    if direction == 0:
        st_x1_change = 60
        move_1 = True
    elif direction == 1:
        st_y1_change = 60
        move_1 = False
    elif direction == 2:
        st_x1_change = -60
        move_1 = True
    elif direction == 3:
        st_y1_change = -60
        move_1 = False
    if move_1 == True:
        if st_x1_change < 0 :
            x1=int((st_x1+st_x1_change)/60)
            y1=int((st_y1)/60)
            if tilemap[y1][x1] is not ROCK :           
                st_x1 = st_x1_change + st_x1
        if st_x1_change>0 :
            x1=int((st_x1+st_x1_change)/60)
            y1=int((st_y1)/60)
            if tilemap[y1][x1] is not ROCK :           
                st_x1 = st_x1_change + st_x1
    if move_1 == False :
        if st_y1_change<0 :
            x1=int(st_x1/60)
            y1=int((st_y1+st_y1_change)/60)
            if tilemap[y1][x1] is not ROCK :
                st_y1 = st_y1 + st_y1_change
        if st_y1_change>0:
            x1=int(st_x1/60)
            y1=int((st_y1 + st_y1_change)/60)
            if tilemap[y1][x1] is not ROCK:
                st_y1 = st_y1_change + st_y1

                ######
    if direction1 == 0:
        st_x2_change = 60
        move_2 = True
    elif direction1 == 1:
        st_y2_change = 60
        move_2 = False
    elif direction1 == 2:
        st_x2_change = -60
        move_2 = True
    elif direction1 == 3:
        st_y2_change = -60
        move_2 = False
    if move_2 == True:
        if st_x2_change < 0 :
            x2=int((st_x2+st_x2_change)/60)
            y2=int((st_y2)/60)
            if tilemap[y2][x2] is not ROCK :           
                st_x2 = st_x2_change + st_x2
        if st_x2_change>0 :
            x2=int((st_x2+st_x2_change)/60)
            y2=int((st_y2)/60)
            if tilemap[y2][x2] is not ROCK :           
                st_x2 = st_x2_change + st_x2
    if move_2 == False :
        if st_y2_change<0 :
            x2=int(st_x2/60)
            y2=int((st_y2+st_y2_change)/60)
            if tilemap[y2][x2] is not ROCK :
                st_y2 = st_y2 + st_y2_change
        if st_y2_change>0:
            x2=int(st_x2/60)
            y2=int((st_y2 + st_y2_change)/60)
            if tilemap[y2][x2] is not ROCK:
                st_y2 = st_y2_change + st_y2
                ###
    if direction2 == 0:
        st_x3_change = 60
        move_3 = True
    elif direction2 == 1:
        st_y3_change = 60
        move_3 = False
    elif direction2 == 2:
        st_x3_change = -60
        move_3 = True
    elif direction2 == 3:
        st_y3_change = -60
        move_3 = False
    if move_3 == True:
        if st_x3_change < 0 :
            x3=int((st_x3+st_x3_change)/60)
            y3=int((st_y3)/60)
            if tilemap[y3][x3] is not ROCK :           
                st_x3 = st_x3_change + st_x3
        if st_x3_change>0 :
            x3=int((st_x3+st_x3_change)/60)
            y3=int((st_y3)/60)
            if tilemap[y3][x3] is not ROCK :           
                st_x3 = st_x3_change + st_x3
    if move_3 == False :
        if st_y3_change<0 :
            x3=int(st_x3/60)
            y3=int((st_y3+st_y3_change)/60)
            if tilemap[y3][x3] is not ROCK :
                st_y3 = st_y3 + st_y3_change
        if st_y3_change>0:
            x3=int(st_x3/60)
            y3=int((st_y3 + st_y3_change)/60)
            if tilemap[y3][x3] is not ROCK:
                st_y3 = st_y3_change + st_y3
                ##########
    if direction3 == 0:
        st_x4_change = 60
        move_4 = True
    elif direction3 == 1:
        st_y4_change = 60
        move_4 = False
    elif direction3 == 2:
        st_x4_change = -60
        move_4 = True
    elif direction3 == 3:
        st_y4_change = -60
        move_4 = False
    if move_4 == True:
        if st_x4_change < 0 :
            x4=int((st_x4+st_x4_change)/60)
            y4=int((st_y4)/60)
            if tilemap[y4][x4] is not ROCK :           
                st_x4 = st_x4_change + st_x4
        if st_x4_change>0 :
            x4=int((st_x4+st_x4_change)/60)
            y4=int((st_y4)/60)
            if tilemap[y4][x4] is not ROCK :           
                st_x4 = st_x4_change + st_x4
    if move_4 == False :
        if st_y4_change<0 :
            x4=int(st_x4/60)
            y4=int((st_y4+st_y4_change)/60)
            if tilemap[y4][x4] is not ROCK :
                st_y4 = st_y4 + st_y4_change
        if st_y4_change>0:
            x4=int(st_x4/60)
            y4=int((st_y4 + st_y4_change)/60)
            if tilemap[y4][x4] is not ROCK:
                st_y4 = st_y4_change + st_y4
    DISPLAYSURF.blit(player, (st_x, st_y,60,60)) # pacman input on screen and actuall movement after above variables are valid
    DISPLAYSURF.blit(orange, (st_x1, st_y1,60,60))
    DISPLAYSURF.blit(pink, (st_x2, st_y2,60,60)) 
    DISPLAYSURF.blit(blue, (st_x3, st_y3,60,60)) 
    DISPLAYSURF.blit(red, (st_x4, st_y4,60,60)) 

    #update the display
    time.tick(FPS)
    pygame.display.update()
    
