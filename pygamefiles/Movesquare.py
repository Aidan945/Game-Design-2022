# Aidan Zarski
# learning to draw circles, images, and stuff
# 6/9/2022
from cmath import rect
from importlib.util import spec_from_loader
import os, pygame, time, random, math
os.system("cls")
pygame.init()


WIDTH = 700 # amount of pixels
HEIGHT = 700
speed=1

# creat a display
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My first game") # title of the window

# images
bg = pygame.image.load("pygamefiles/images/bgSmaller.jpg")
char = pygame.image.load("pygamefiles/images/PixelArtTutorial.png")


# create a square
hb=50
wb=50
xb=100
yb=300
square = pygame.Rect(xb,yb,wb,hb)

#char variables
charx = 200
chary = 50


def squaremove():
    if keys[pygame.K_a] and square.x > speed:
        square.x -=speed
    if keys[pygame.K_d] and square.x < (WIDTH-(wb+speed)):
        square.x +=speed
    if keys[pygame.K_w] and square.y>speed:
        square.y-=speed
    if keys[pygame.K_s] and square.y < HEIGHT-(hb+speed):
        square.y+=speed

#create circle variables
cx=350
cy=350
radios=30
ibox = radios*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy - (ibox/2)
insSquare = pygame.Rect(xig,yig,ibox,ibox)



run=True
while run:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys=pygame.key.get_pressed() #provide a list of all keys

    
    # rect, surface, color, dimensions/location
    if square.colliderect(insSquare):
        print("BOOM")
        cx = random.randint(radios, WIDTH-radios)
        cy = random.randint(radios, HEIGHT-radios)
        insSquare.x = cx-(ibox/2)
        insSquare.y = cy - (ibox/2)
    if keys[pygame.K_a] and square.x > speed:
        square.x -=speed
    if keys[pygame.K_d] and square.x < (WIDTH-(wb+speed)):
        square.x +=speed
    if keys[pygame.K_w] and square.y>speed:
        square.y-=speed
    if keys[pygame.K_s] and square.y < HEIGHT-(hb+speed):
        square.y+=speed    
        
    pygame.draw.rect(screen, "pink", square)
    # circle
    if keys[pygame.K_RIGHT] and cx < WIDTH - radios:
        cx +=speed
        insSquare.x +=speed
    if keys[pygame.K_LEFT] and cx > radios :
        cx -=speed
        insSquare.x-=speed
    if keys[pygame.K_UP] and cy > radios:
        cy-=speed
        insSquare.y-=speed
    if keys[pygame.K_DOWN] and cy < HEIGHT-radios:
        cy+=speed
        insSquare.y+=speed

    pygame.draw.rect(screen, "green", insSquare)
    pygame.draw.circle(screen, "blue",(cx,cy),radios)

    screen.blit(char, (charx,chary))
    
    pygame.display.update()
    pygame.time.delay(2)






