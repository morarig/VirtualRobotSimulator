#Timer for pygame

import pygame

#Defining colours
Black = (0,0,0)
White = (255, 255, 255)

pygame.init()

#Set the dimensions for the window.
size = [700,500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Timer")

#Loop function, until user exits game.
Exit = False

#Used to update the screen
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)

#declaring some varibales used to update screen
frame_count = 0
frame_rate = 60
start_time = 90

#Main loop program

#This will notify and close the program if the user exits the game.
while not Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

#Sets the background screen for timer
screen.fill(White)

#Timer going up
total_seconds = frame_count // frame_rate

#Dividing by 60, so that we get total in minutes.
minutes = total_seconds % 60

#Using python's formatting to give a suitable output. 
output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

#Used to attach the screen/ blit.
text = font.render(output_string, True, Black)
screen.blit(text, [250, 250])

pygame.quit()
