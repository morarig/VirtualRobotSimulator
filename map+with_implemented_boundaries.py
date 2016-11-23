import pygame, sys
from pygame.locals import *
#variables for pacmans initial position
st_x = 480
st_y = 420
FPS = 7.5

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
move = 0
pygame.display.set_caption("B-man 4")
player = pygame.image.load('pacman_sp(60x60).png')
st_x_change = 0 # adder for movement after keypress ,variable
st_y_change = 0 # adder for movement after keypress ,variable
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
    DISPLAYSURF.blit(player, (st_x, st_y,60,60)) # pacman input on screen and actuall movement after above variables are valid

    #update the display
    time.tick(FPS)
    pygame.display.update()
    
