from PIL import Image
import pygame

tileSize = 32

class World:
    def __init__(self):

        self.R = []
        # self.G = []
        # self.B = []
        with Image.open('CloudGame.REMAKE/res/world.png') as file:
            mapWidth, mapHeight = file.size
            file.convert('RGB') 

            for x in range(mapWidth):
                for y in range(mapHeight):
                    RGBA = list(file.getpixel((x, y)))
                    if RGBA[0] == 0: 
                        self.R.append(pygame.Rect(tileSize*x, tileSize*y, tileSize, tileSize))  

    def getLevelData(self):
        return self.R


