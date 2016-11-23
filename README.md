import pygame, sys
from pygame.locals import *
# Variables for intial position of pacman and later on movement
st_x = 280
st_y = 220

#constants representing colours
BLACK=(0,0,0)
WHITE=(255,255,255)
red = (255,0,0) # demo pacman image till sprite is insterted

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
time = pygame.time.Clock() # FPS counter variable
move = 0 # boolean so one movement is funtional at a time
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
    pygame.draw.rect(DISPLAYSURF , red , [st_x,st_y,20,20]) # pacman input on screen and actuall movement after above variables are valid
    if move == True :
        st_x += st_x_change
    if move == False :
        st_y += st_y_change
        
        #update the display
    pygame.display.update()
    time.tick(7.5) # fps editor
pygame.quit()
quit()
