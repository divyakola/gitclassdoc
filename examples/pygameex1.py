import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 

while not done:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
   
    screen.fill(WHITE)
 
    
    pygame.display.flip()
 
    
    clock.tick(60)
 
pygame.quit()
﻿
