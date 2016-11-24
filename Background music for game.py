#Background music for pygame
import pygame
from pygame.locals import *
pygame.intit()

#Creates a window
window = pygame.display.set_mode((640,640))

#Loads music file and start from the beginning of the song; the song is on an infinte loop.
pygame.mixer.music.load("Pacman.mp3")
pygame.mixer.music.play(-1,0.0)

#Creates a circle in the window to show the music file being played.
circle = pygame.draw.circle(window, (50,30,90),(90,30),16,5)

#This peice of code groups the window and circle together.
window.blit(window,cricle)

#This peice of code plays the song until the user has quit the window. 
while True:
    for even in pygame.event.get():
        if event.type--pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
