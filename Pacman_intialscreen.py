import pygame
pygame.init()
size = width, height = 1024, 768 
black = 0, 0, 0
screen = pygame.display.set_mode(size)

start_screen = pygame.image.load("pacman_beta.png")#imports image 
screenrect = start_screen.get_rect() #variable for inputing screen
screen.blit(start_screen , screenrect)#prinitng in window
pygame.display.flip()# see in screen 

