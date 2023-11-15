from sprites import entity

tileSize = 32
displaySize = [40*32, 24*32]
speed = 32/5
gravity = 4.4

class Player(entity.Entity):
    def __init__(self, rect):
        super().__init__(rect)

    def move(self, left, right, up, down, jump, levelData):
        self.velX = 0
        self.velY = 0
        jumpForce = 0
        
        if left and self.hitbox.left > 0: self.velX -= speed
        if right and self.hitbox.right < displaySize[0]: self.velX += speed
        if up and self.hitbox.top > 0: self.velY -= speed
        if down and self.hitbox.bottom < displaySize[1]: self.velY += speed
        if jump: 
            jumpForce -= 0.5
            self.velY += jumpForce
            print(self.velY)

        self.collision(levelData)

        
    def collision(self, levelData):
        self.hitbox.x += self.velX
        for tile in levelData:
            if self.hitbox.colliderect(tile):
                if self.velX <= 0: self.hitbox.left = tile.right
                if self.velX >= 0: self.hitbox.right = tile.left 

        self.hitbox.y += self.velY + gravity
        for tile in levelData:
            if self.hitbox.colliderect(tile):    
                if self.velY <= 0: self.hitbox.top = tile.bottom
                if self.velY >= 0: self.hitbox.bottom = tile.top

    def draw(self, surface, showHitbox):
        return super().draw(surface, showHitbox)

    def animate(self):
        pass