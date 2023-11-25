import os
import sys
import pygame
import meta

pygame.init()
#pygame.mixer.init() #just putting this here for future music/sfx use

# window data
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d, %d' % (50, 50)

tileSize = meta.Game.TILESIZE
displaySize = meta.Game.DISPLAY_SIZE
display = pygame.display.set_mode(displaySize)
canvas = pygame.Surface(displaySize)

# fps
frames = meta.Game.FPS
fps = pygame.time.Clock()
logCount = 0
def fpsLog(): # write fps in console
    global logCount
    logCount += 1
    if logCount == 60:
        print(fps)
        logCount = 0

# world data
import load
loadLevel = load.World()
tileData = loadLevel.getLevelData()

# player data
from sprites import player
playerPos = (7, 14)
playerRect = (tileSize*playerPos[0], tileSize*playerPos[1], tileSize/2, tileSize)
plyr = player.Player(playerRect)

# --------------------------------------------
# play area
textData = pygame.font.SysFont('Consolas', 14)

def playArea():
    # temp map
    map = pygame.image.load('CloudGame.REMAKE/res/tileData.png')
    mapimg = pygame.transform.scale(map, (displaySize))
    canvas.blit(mapimg, (0, 0))

    # player info
    textDisplay = textData.render(
        ' coords:' +str((plyr.hitbox.x, plyr.hitbox.y))+ 
        ' velXYZ:' +str((plyr.velX, plyr.velY, plyr.velZ)), False, 'black')   
    canvas.blit(textDisplay, (10, 10))  

    # for tile in tileData:
    #     pygame.draw.rect(canvas, 'black', (tile.x, tile.y, tile.width, tile.height), 1)
 
# --------------------------------------------


while True:
    fps.tick(30)
    fpsLog()

    # visuals
    pygame.display.flip() 
    display.blit(canvas, (0, 0))

    # background
    canvas.fill("white") 

    # tests
    playArea()

    # entities
    plyr.update(canvas)

    # events
    for event in pygame.event.get():
        # program command keys
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()    
        if pygame.key.get_pressed()[pygame.K_F11]: pygame.display.toggle_fullscreen()
        
        # player
        if pygame.key.get_pressed()[pygame.K_SPACE] and not plyr.jump: plyr.spaceHold += 1
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_a: plyr.moveLeft = True
                case pygame.K_d: plyr.moveRight = True
                case pygame.K_w: plyr.moveUp = True
                case pygame.K_s: plyr.moveDown = True
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_a: plyr.moveLeft = False
                case pygame.K_d: plyr.moveRight = False
                case pygame.K_w: plyr.moveUp = False
                case pygame.K_s: plyr.moveDown = False
                case pygame.K_SPACE: plyr.jump = True