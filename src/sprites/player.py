from sprites import entity
import meta

tileSize = meta.Game.TILESIZE
displaySize = meta.Game.DISPLAY_SIZE

speed = 0.25
speedLimit = 5

longJump = 18 
shortJump = longJump/2 

class Player(entity.Entity):
    def __init__(self, rect):
        super().__init__(rect)
        self.showHitbox = True

        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.jump = False

        self.spaceHold = 0
        self.airTime = longJump

        self.velX = 0 # walk LR
        self.velY = 0 # walk LR
        self.velZ = 0 # walk UD

    def update(self, surface):
        super().update(surface)
        self.moveXZ()
        self.moveY()


    def moveXZ(self):
        # screen edge
        if self.hitbox.left < 0: self.hitbox.left = 0
        if self.hitbox.right > displaySize[0]: self.hitbox.right = displaySize[0]

        # move lrup with slippy effect
        if self.moveLeft and not self.moveRight and self.hitbox.left > 0: 
            self.velX -= speed
            if self.velX < -speedLimit: self.velX = -speedLimit
        elif self.velX < 0:
            self.velX += speed
            if self.velX >= 0: self.velX = 0

        if self.moveRight and not self.moveLeft and self.hitbox.right < displaySize[0]: 
            self.velX += speed
            if self.velX > speedLimit: self.velX = speedLimit
        elif self.velX > 0:
            self.velX -= speed
            if self.velX <= 0: self.velX = 0

        if self.moveUp and not self.moveDown and self.hitbox.top > 0: 
            self.velZ -= speed
            if self.velZ < -speedLimit/2: self.velZ = -speedLimit/2
        elif self.velZ < 0:
            self.velZ += speed/2
            if self.velZ >= 0: self.velZ = 0

        if self.moveDown and not self.moveUp and self.hitbox.bottom < displaySize[1]: 
            self.velZ += speed
            if self.velZ > speedLimit/2: self.velZ = speedLimit/2
        elif self.velZ > 0:
            self.velZ -= speed/2
            if self.velZ <= 0: self.velZ = 0

        # if readying for jump stop With slippy effect
        if not self.jump and self.spaceHold > 0:
            if self.velX < 0:
                self.velX += speed*2
                if self.velX >= 0: self.velX = 0

            if self.velX > 0:
                self.velX -= speed*2
                if self.velX <= 0: self.velX = 0

            if self.velZ < 0:
                self.velZ += speed*2
                if self.velZ >= 0: self.velZ = 0
            if self.velZ > 0:
                self.velZ -= speed*2
                if self.velZ <= 0: self.velZ = 0

        # change xy values by xy velocity
        self.hitbox.x += self.velX
        self.hitbox.y += self.velZ

    def moveY(self):
        if self.spaceHold == 0: self.jump = False

        if self.jump and self.spaceHold > 0:
            if self.spaceHold <= 8: # i can link the amount of hold to the animation
                if self.airTime == longJump: self.airTime = shortJump
                if self.airTime >= -shortJump:
                    self.velY = self.airTime
                    self.airTime -= 1
                else:
                    self.airTime = longJump
                    self.velY = 0
                    self.spaceHold = 0
                    self.jump = False
            else:
                if self.airTime >= -longJump:
                    self.velY = self.airTime
                    self.airTime -= 1
                else:
                    self.airTime = longJump
                    self.velY = 0
                    self.spaceHold = 0
                    self.jump = False
        

        self.hitbox.y -= self.velY
    
    def collision(self, levelData):
        for tile in levelData:
            if tile.collidepoint(self.hitbox.bottomright) or tile.collidepoint(self.hitbox.bottomleft):
                self.gravity = 0
                if self.onAir:
                    self.onAir = False

    def animate(self):
        return super().animate()
