import pygame


class Entity:
    def __init__(self, rect):
        self.hitbox = pygame.Rect(rect)
        self.showHitbox = False

    def update(self, surface):
        self.draw(surface)

    def draw(self, surface):
        if self.showHitbox: pygame.draw.rect(surface, "red", self.hitbox)

    def animate(self):
        pass