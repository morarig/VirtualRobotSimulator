import pygame, sys
from pygame.locals import *
import random
# Variables for intial position of pacman and later on movement
st_x = 220
st_y = 220
st_x1 = 120
st_y1 = 120

FPS = 5
#constants representing colours
BLACK=(0,0,0)
WHITE=(255,255,255)
red = (255,0,0) # demo pacman image till sprite is insterted
green = (0,255,0)
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
    [ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK],
    [ROCK, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ROCK],
    [ROCK, PATH, ROCK, PATH, ROCK, ROCK, PATH, ROCK, PATH, ROCK, PATH, ROCK, PATH, ROCK],
    [ROCK, PATH, PATH, PATH, PATH, ROCK, PATH, PATH, PATH, ROCK, PATH, ROCK, PATH, ROCK],
    [ROCK, PATH, PATH, ROCK, PATH, ROCK, ROCK, ROCK, PATH, PATH, PATH, PATH, PATH, ROCK],
    [ROCK, PATH, PATH, ROCK, PATH, PATH, PATH, PATH, ROCK, ROCK, ROCK, ROCK, PATH, ROCK],
    [ROCK, PATH, PATH, ROCK, ROCK, ROCK, PATH, PATH, ROCK, PATH, PATH, PATH, PATH, ROCK],
    [ROCK, PATH, PATH, PATH, ROCK, ROCK, ROCK, PATH, PATH, PATH, ROCK, PATH, ROCK, ROCK],
    [ROCK, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ROCK],
    [ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK, ROCK],


    ]

#useful game dimensions
TILESIZE=40
MAPWIDTH=14
MAPHEIGHT=10

#set up the display
pygame.init()
DISPLAYSURF=pygame.display.set_mode((560,400))
pygame.display.update()
st_x_change = 0 # adder for movement after input , variables
st_y_change = 0
st_x1_change = 0
st_y1_change = 0
time = pygame.time.Clock() # FPS counter variable
move = 0 # boolean so one movement is funtional at a time
move_1 = 0
while True :
    for row in range(0,MAPHEIGHT) :
         for column in range(0,MAPWIDTH):
        #draw the resource at the position in the tilemap, using the correct colour
            pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE, row*TILESIZE,TILESIZE,TILESIZE))
     #get all the user events
    for event in pygame.event.get():
        print(event) 
        #if the user wants to quit
        if event.type== QUIT :
            #end the game and close the window
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # movment code after key is pressed
            if event.key == pygame.K_RIGHT:
                st_x_change = 20
                move = True
            elif event.key == pygame.K_DOWN:
                    st_y_change = 20
                    move = False
            elif event.key == pygame.K_LEFT:
                st_x_change = -20
                move = True
            elif event.key == pygame.K_UP:
                st_y_change = -20
                move = False

    if move == True :
        st_x += st_x_change
    if move == False :
        st_y += st_y_change
        
    pygame.draw.rect(DISPLAYSURF , red , [st_x,st_y,20,20]) # pacman input on screen and actuall movement after above variables are valid


    Up = 0
    Down = 1
    Left = 2
    Right = 3
    direction = random.randint(0,4)
    
    if direction == 0:
        st_x1_change = 20
        move_1 = True
    elif direction == 1:
        st_y1_change = 20
        move_1 = False
    elif direction == 2:
        st_x1_change = -20
        move_1 = True
    elif direction == 3:
        st_y1_change = -20
        move_1 = False
    if move == True:
        st_x1 += st_x1_change
    if move == False:
        st_y1 += st_y1_change
    
      

    pygame.draw.rect(DISPLAYSURF, green, [st_x1,st_y1,20,20])
       
        #update the display
    pygame.display.update()
    time.tick(7.5) # fps editor
pygame.quit()
quit()
