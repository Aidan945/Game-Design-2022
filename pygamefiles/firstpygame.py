# Aidan Zarski
# learning to draw circles, images, and stuff
# 6/9/2022
from cmath import rect
import os, pygame, time
os.system("cls")
pygame.init()


WIDTH = 700 # amount of pixels
HEIGHT = 700

# creat a display
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My first game") # title of the window

# create a square
square = (200,200,50,50)

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill("red")
    # rect, surface, color, dimensions/location
    pygame.draw.rect(screen, "blue", square)
    # circle
    pygame.draw.circle(screen, "black",(350,400),60)
    pygame.display.update()






