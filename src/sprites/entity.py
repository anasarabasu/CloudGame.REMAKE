import pygame

class Entity:
    def __init__(self, rect):
        self.hitbox = pygame.Rect(rect)

    def draw(self, surface, showHitbox):
        if showHitbox: pygame.draw.rect(surface, "red", self.hitbox, 1)

    def animate(self):
        pass