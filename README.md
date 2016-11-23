import pygame, sys, random
from pygame.locals import *
# Variables for intial position of pacman and later on movement
st_x =540
st_y = 540
FPS =5
#constants representing colours
BLACK=(0,0,0)
WHITE=(255,255,255)
red = (255,0,0) # demo pacman image till sprite is insterted
blue = (0,255,0)

randomx = random.randint(0, 3)

class Ghosts(pygame.sprite.Sprite):
    """Class to control the random movement of the ghosts in the game"""
    
    def __init__(self):
        self.x, self.y = 0,0
        self.movementx, self.movementy = 60,60

    def ghostmove(self):
        """ function to change randomly change the direction of the"""
        """ghosts in a random number of steps"""
        
        Stepstaken = random.randrange(5,11)
        Steps = 0
        
        if Steps <= Stepstaken:
            
            self.movementx = (-1,1)
            self.movementy = (-1,1)
            self.x += movementx
            self.y +=movementy
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
pygame.mixer.music.load("Pacman.mp3")#music playing
pygame.mixer.music.play(-1,0.0)
DISPLAYSURF=pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
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
        
    if move == True :
        st_x += st_x_change
    if move == False :
        st_y += st_y_change

    pygame.draw.rect(DISPLAYSURF , red , [st_x,st_y,60,60]) # pacman input on screen and actuall movement after above variables are valid
    
  
        #update the display
    pygame.display.update()
    time.tick(FPS) # fps editor
pygame.quit()
quit()
