import pygame
import sys

pygame.init()
#pygame.mixer.init() #just putting this here for future music/sfx use

fps = pygame.time.Clock()

winSize = [1280, 720]
display = pygame.display.set_mode(winSize)
canvas = pygame.Surface(winSize)

loc = [0, 0]
box = pygame.Rect(0, 0, 14, 14)
speed = 14

moveRight = False
moveLeft = False
MoveUp = False
MoveDown = False

def move(moveRight):
    if event.type == pygame.KEYDOWN:
        match event.key:
            case pygame.K_d:
                moveRight = True
            case pygame.K_a:
                loc[0] -= speed
            case pygame.K_w:
                loc[1] -= speed
            case pygame.K_s:
                loc[1] += speed
    if event.type == pygame.KEYUP:
        match event.key:
            case pygame.K_d:
                moveRight = False
            case pygame.K_a:
                loc[0] = 0
            case pygame.K_w:
                loc[1] = 0
            case pygame.K_s:
                loc[1] = 0

    if moveRight == True:
        loc[0] += speed
    elif moveRight == False:
        loc[0] = 0


while True:
    fps.tick(60)

    pygame.display.flip() # update visuals
    display.blit(canvas, (0, 0))
    canvas.fill("white")

    pygame.draw.rect(canvas, "red", box)
    box.x += loc[0]
    box.y += loc[1]

    for event in pygame.event.get():
        # close program
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()    
        
        # 
        move(moveRight)

