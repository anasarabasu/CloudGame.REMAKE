from PIL import Image
import pygame
import meta

tileSize = meta.Game.TILESIZE

class World:
    def __init__(self):
        self.tileData = []
        with Image.open('CloudGame.REMAKE/res/tileData.png') as file:
            self.mapWidth, self.mapHeight = file.size
            file.convert('RGB') 
            for y in range(self.mapHeight):
                for x in range(self.mapWidth):
                    RGBA = list(file.getpixel((x, y)))
                    if RGBA[0] == 0: # ground
                        # self.tileData.append((x, y))
                        self.tileData.append(pygame.Rect(tileSize*x, tileSize*y, tileSize, tileSize))
        

    def getLevelData(self):
        return self.tileData

