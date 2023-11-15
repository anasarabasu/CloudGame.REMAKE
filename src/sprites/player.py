from sprites import entity

tileSize = 32
displaySize = [40*32, 24*32]
speed = 32/5
gravity = 4.4

class Player(entity.Entity):
    def __init__(self, rect):
        super().__init__(rect)

    def move(self, left, right, up, down, jump, levelData):
        self.moveX = 0
        self.moveY = 0
        
        if left and self.hitbox.left > 0: self.moveX -= speed
        if right and self.hitbox.right < displaySize[0]: self.moveX += speed
        if up and self.hitbox.top > 0: self.moveY -= speed
        if down and self.hitbox.bottom < displaySize[1]: self.moveY += speed

        jumpForce = 32
        if jump: 
            self.hitbox.y -= jumpForce
            jumpForce -= gravity

        self.collision(levelData)

        
    def collision(self, levelData):
        self.hitbox.x += self.moveX
        for tile in levelData:
            if self.hitbox.colliderect(tile):
                if self.moveX <= 0: self.hitbox.left = tile.right
                if self.moveX >= 0: self.hitbox.right = tile.left 

        self.hitbox.y += self.moveY + gravity
        for tile in levelData:
            if self.hitbox.colliderect(tile):    
                if self.moveY <= 0: self.hitbox.top = tile.bottom
                if self.moveY >= 0: self.hitbox.bottom = tile.top

    # def draw(self, surface, showHitbox):
    #     if showHitbox: pygame.draw.rect(surface, "red", self.hitbox, 1)

        #draw playerimage

    def animate(self):
        pass