import pygame, sys 
from pygame.locals import *
import random
#variables for pacmans initial position
pygame.init()
FPS = 7.5#fps counter
screen = None
pygame.mixer.music.load("Pacman.mp3")
pygame.mixer.music.play(-1,0.0)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
frame_count = 0
frame_rate = FPS
start_time = 90
st_x = 480 # pacman initial cordinates in x axis
st_x1 = 60# orange initial cordinates in x axis
st_x2 = 900# pink initial cordinates in x axis
st_x3 =60# blue initial cordinates in x axis
st_x4 = 900# red initial cordinates in x axis
st_y = 420# pacman initial cordinates in y axis
st_y1 = 60# orange initial cordinates in y axis
st_y2 = 60# pink initial cordinates in y axis
st_y3 = 780# blue initial cordinates in y axis
st_y4 = 780#red initial cordinates in y axis
st_x_change = 0 # adder for movement in x axis after keypress ,variable for pacman
st_x1_change = 0# adder for movement in x axis after keypress ,variable for orange
st_x2_change = 0# adder for movement in x axis after keypress ,variable for pink
st_x3_change = 0# adder for movement in x axis after keypress ,variable forblue
st_x4_change = 0# adder for movement in x axis after keypress ,variable for red
st_y_change = 0 # adder for movement in y axis after keypress ,variable for pacman
st_y1_change = 0## adder for movement in y axis after keypress ,variable for orange
st_y2_change = 0# adder for movement in y axis after keypress ,variable for pink
st_y3_change = 0# adder for movement in y axis after keypress ,variable for blue
st_y4_change = 0# adder for movement in y axis after keypress ,variable for red
move = 0 # boolean so only movement can be perfomed in one axis at a time for pacman
move_1 = 0# boolean so only movement can be perfomed in one axis at a time for orange
move_2 = 0# boolean so only movement can be perfomed in one axis at a time for pink
move_3 = 0# boolean so only movement can be perfomed in one axis at a time for blue
move_4 = 0# boolean so only movement can be perfomed in one axis at a time for red
#Four variables for all 4 ghost movements and direction of movement
Up = 0
Down = 1
Left = 2
Right = 3
#####
gamemode = False#Boolean for which gamemode is active
lose = False #Losing boolean 
ap = True#boolean to within the map to spawn an apple
ch = True#boolean to within the map to spawn an cherry
st = True#boolean to within the map to spawn an strawberry
stext = "Strawberries :"#string for score of strawberries
atext = "Apples :"#string for score of apples
ctext = "Cherries :"#string for score of cherries
wintext = "Congratulations Pacman has been fed !! "#winning string for "feed pacman"mode
leavetext = "Press Esc to go back to initial screen and reset the game "#leaving game straing while playing 
winleavetext = "Press Esc to go back to initial screen"#additional straing for winning "feed pacman" mode
cuaghttext = "Sorry you lost.Press Esc to go back"
finalwintext = False#boolean activating "feed pacman"mode
text = pygame.font.SysFont(None,25)
wtext= pygame.font.SysFont(None,60)
spoint= 0#score counter for strawberries
apoint = 0#score counter for apples
cpoint = 0#score counter for cherries
#constants representing colours
BLACK=(0,0,0)
WHITE=(255,255,255)
yellow=(255,255,0)
wierdblue=(150,150,250)
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
####
#image loading of apropriate picture under 
player = pygame.image.load('pacman_sp(60x60).png')
orange = pygame.image.load('orange-ghost.png')
blue = pygame.image.load('lightblue-ghost.png')
red = pygame.image.load('red-ghost.png')
pink = pygame.image.load('pink-ghost.png')
apple = pygame.image.load("Apple.png")
cherry = pygame.image.load("cherry.png")
strawberry = pygame.image.load("strawberry.png")
start_screen = pygame.image.load("pacman_beta.png")
settings = pygame.image.load("settings.png")
while True :
    while screen == None:#While loop for initial screen
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(start_screen,(0,0,MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen = True
                if event.key == pygame.K_SPACE:
                    screen = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit
    while screen == False:#while loop for settings screen
        DISPLAYSURF.blit(settings,(0,0,MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screen = None
                if event.key == pygame.K_5:
                    FPS = 5
                if event.key == pygame.K_7:
                    FPS = 7.5
                if event.key == pygame.K_0:
                    FPS = 10
                if event.key == pygame.K_SPACE:
                    gamemode = True
                if event.key == pygame.K_RETURN:
                    gamemode = False
    while screen == True:#while loop for game
        lose = False
        finalwintext = False
        total_seconds = frame_count // frame_rate
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
        texttimer = font.render(output_string, True, yellow)
        frame_count += 1


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
                if event.key == pygame.K_ESCAPE:#going bck to initial screen and resetting game but keeping same mode
                    screen = None
                    st_x = 480 # 
                    st_x1 = 60
                    st_x2 = 900
                    st_x3 =60
                    st_x4 = 900
                    st_y = 420
                    st_y1 = 60
                    st_y2 = 60
                    st_y3 = 780
                    st_y4 = 780
                    st_x_change = 0 
                    st_x1_change = 0
                    st_x2_change = 0
                    st_x3_change = 0
                    st_x4_change = 0
                    st_y_change = 0
                    st_y1_change = 0
                    st_y2_change = 0
                    st_y3_change = 0
                    st_y4_change = 0
                    move = 0
                    move_1 = 0
                    move_2 = 0
                    move_3 = 0
                    move_4 = 0
                    spoint= 0
                    apoint = 0
                    cpoint = 0
        for row in range(0,MAPHEIGHT) :
             for column in range(0,MAPWIDTH):
            #draw the resource at the position in the tilemap, using the correct colour
                pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE, row*TILESIZE,TILESIZE,TILESIZE))
        while ap==True:#spawning apples whie boolean true
            rapx = random.randrange(1,MAPWIDTH-1)
            rapy = random.randrange(1,MAPHEIGHT-1)
            apx = int(rapx*TILESIZE)
            apy = int(rapy*TILESIZE)
            if tilemap[rapy][rapx] is PATH :
                ap = False
        while ch==True:#same for cherries
            rchx = random.randrange(1,MAPWIDTH-1)
            rchy = random.randrange(1,MAPHEIGHT-1)
            chx = int(rchx*TILESIZE)
            chy = int(rchy*TILESIZE)
            if tilemap[rchy][rchx] is PATH :
                ch = False
        while st==True:#and for strawberries
            rstx = random.randrange(1,MAPWIDTH-1)
            rsty = random.randrange(1,MAPHEIGHT-1)
            stx = int(rstx*TILESIZE)
            sty = int(rsty*TILESIZE)
            if tilemap[rsty][rstx] is PATH :
                st = False
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
            ###
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
            #####
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
            #####
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
            #######
        if spoint >=10 and apoint >=10 and cpoint>= 10 and gamemode == True:#"feed pacman mode" txt once winning and requirements to win also going back to initial screen option and reseting game
            winningtext = wtext.render(wintext,True,wierdblue)
            winningtext_2=wtext.render(winleavetext,True,wierdblue)
            st_x_change = 0 
            st_y_change = 0
            st_x1_change = 0
            st_x2_change = 0
            st_x3_change = 0
            st_x4_change = 0
            st_y1_change = 0
            st_y2_change = 0
            st_y3_change = 0
            st_y4_change = 0
            finalwintext = True
        if st_x == st_x1 and st_y ==st_y1: ## If statements for losing
            losetext = wtext.render(cuaghttext,True,wierdblue)
            st_x_change = 0 
            st_y_change = 0
            st_x1_change = 0
            st_x2_change = 0
            st_x3_change = 0
            st_x4_change = 0
            st_y1_change = 0
            st_y2_change = 0
            st_y3_change = 0
            st_y4_change = 0
            lose = True
        if st_x == st_x2 and st_y ==st_y2:
            losetext = wtext.render(cuaghttext,True,wierdblue)
            st_x_change = 0 
            st_y_change = 0
            st_x1_change = 0
            st_x2_change = 0
            st_x3_change = 0
            st_x4_change = 0
            st_y1_change = 0
            st_y2_change = 0
            st_y3_change = 0
            st_y4_change = 0
            lose = True
        if st_x == st_x3 and st_y ==st_y3:
            losetext = wtext.render(cuaghttext,True,wierdblue)
            st_x_change = 0 
            st_y_change = 0
            st_x1_change = 0
            st_x2_change = 0
            st_x3_change = 0
            st_x4_change = 0
            st_y1_change = 0
            st_y2_change = 0
            st_y3_change = 0
            st_y4_change = 0
            lose = True
        if st_x == st_x4 and st_y ==st_y4:
            losetext = wtext.render(cuaghttext,True,wierdblue)
            st_x_change = 0 
            st_y_change = 0
            st_x1_change = 0
            st_x2_change = 0
            st_x3_change = 0
            st_x4_change = 0
            st_y1_change = 0
            st_y2_change = 0
            st_y3_change = 0
            st_y4_change = 0
            lose = True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screen = None
                    #######
        if move == True:# calculating next movement of character or ghost under and collison check with walls
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
            #######
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
        if st_x == stx and st_y == sty:#if pacman in same position with a berry a point is given and it respawns in a new random position 
            st = True
            spoint = spoint +1
        if st_x == chx and st_y == chy :
            ch = True
            cpoint = cpoint + 1
        if st_x == apx and st_y == apy :
            ap = True
            apoint = apoint +1
        DISPLAYSURF.blit(texttimer,[450,0])
        esctext = text.render(leavetext,True,yellow)#draws text depending situation (cross check variables)
        DISPLAYSURF.blit(esctext,(0,840))
        cherrytext = text.render(ctext,True,yellow)
        DISPLAYSURF.blit(cherrytext,(0,0))
        cheerypoint= text.render(str(cpoint),True,yellow)
        DISPLAYSURF.blit(cheerypoint,(90,0))
        appletext = text.render(atext,True,yellow)
        DISPLAYSURF.blit(appletext,(120,0))
        applepoint= text.render(str(apoint),True,yellow)
        DISPLAYSURF.blit(applepoint,(200,0))
        strawberrytext = text.render(stext,True,yellow)
        DISPLAYSURF.blit(strawberrytext,(240,0))
        strawberrypoint= text.render(str(spoint),True,yellow)
        DISPLAYSURF.blit(strawberrypoint,(370,0))#
        DISPLAYSURF.blit(strawberry, (stx,sty,TILESIZE,TILESIZE))#berries drawning with apropriate position
        DISPLAYSURF.blit(cherry, (chx,chy,TILESIZE,TILESIZE))
        DISPLAYSURF.blit(apple, (apx,apy,TILESIZE,TILESIZE))
        DISPLAYSURF.blit(player, (st_x, st_y,60,60)) # pacman input on screen and actuall movement after above variables are valid
        DISPLAYSURF.blit(orange, (st_x1, st_y1,TILESIZE,TILESIZE))#drawning ghosts 
        DISPLAYSURF.blit(pink, (st_x2, st_y2,TILESIZE,TILESIZE)) 
        DISPLAYSURF.blit(blue, (st_x3, st_y3,TILESIZE,TILESIZE)) 
        DISPLAYSURF.blit(red, (st_x4, st_y4,TILESIZE,TILESIZE))
        if finalwintext == True :# prints strings for "feed pacman mode"
            DISPLAYSURF.blit(winningtext,(60,420))
            DISPLAYSURF.blit(winningtext_2,(60,460))
        if lose == True :
            DISPLAYSURF.blit(losetext,(60,420))

            


        #update the display
        time.tick(FPS)
        pygame.display.update()
