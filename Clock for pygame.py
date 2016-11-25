# Timer for pygame
import pygame
 
# Defining colours 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
pygame.init()
 
# Setting the dimensions 
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Timer for pygame")
 
# Loop until the user clicks the close button.
done = False
 
# Used to update the screen
clock = pygame.time.Clock()
 
font = pygame.font.Font(None, 25)
 
frame_count = 0
frame_rate = 60
start_time = 90
 
# Main program loop
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
 
# Set the screen background
    screen.fill(WHITE)
 
# Calculate total seconds
    total_seconds = frame_count // frame_rate

# Divide by 60 to get total minutes
    minutes = total_seconds // 60

# Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

# Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
 
# Blit to the screen
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 250])
 
    frame_count += 1
 
# Limit frames per second
    clock.tick(frame_rate)
 
# Updates screen
    pygame.display.flip()
 

pygame.quit()
