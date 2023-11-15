import sys
import pygame

pygame.init()
#pygame.mixer.init() #just putting this here for future music/sfx use

# fps
fps = pygame.time.Clock()
logCount = 0
def fpsLog():
    global logCount
    logCount += 1
    if logCount == 60:
        print(fps)
        logCount = 0

# window data
tileSize = 32
displaySize = [40*32, 24*32]
display = pygame.display.set_mode(displaySize)
canvas = pygame.Surface(displaySize)

# --------------------------------------------
# play area


# --------------------------------------------

# world data
import load
loadLevel = load.World()
levelData = loadLevel.getLevelData()

# player data
from sprites import player
playerRect = (20, 20, tileSize, tileSize)
playerChar = player.Player(playerRect)
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
jump = False

def playerUpdate():
    playerChar.draw(canvas, True)
    playerChar.move(moveLeft, moveRight, moveUp, moveDown, jump, levelData)

while True:
    fps.tick(60)
    fpsLog()

    # visuals
    pygame.display.flip() 
    display.blit(canvas, (0, 0))

    # background
    canvas.fill("white")  

    # --------------------------------------------
    # play area
    for tile in levelData:
        pygame.draw.rect(canvas, 'black', (tile.x, tile.y, tile.width, tile.height), 2)

    # --------------------------------------------

    # entities
    playerUpdate()

    # events
    for event in pygame.event.get():
        # program command keys
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()    
        if pygame.key.get_pressed()[pygame.K_F11]: pygame.display.toggle_fullscreen()
        
        # player
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_a: moveLeft = True
                case pygame.K_d: moveRight = True
                case pygame.K_w: moveUp = True
                case pygame.K_s: moveDown = True
                case pygame.K_SPACE: jump = True
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_a: moveLeft = False
                case pygame.K_d: moveRight = False
                case pygame.K_w: moveUp = False
                case pygame.K_s: moveDown = False
                case pygame.K_SPACE: jump = False

