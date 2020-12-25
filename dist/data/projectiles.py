import pygame
from data import spritesheet


class Projectile(pygame.sprite.Sprite):

    def __init__(self, image, direction, animation=0, size=0):
        super().__init__()
        if animation:
            self.sheet = spritesheet.SpriteSheet(image)
            self.image = self.sheet.get_image(0, 0, size, size)
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.image.load(image).convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
        self.direction = direction
        self.counter = 0
        self.size = size

    def goto(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def animation(self, frames):
        self.image = self.sheet.get_image(self.counter * self.size, 0, self.size, self.size)
        self.counter += 1
        if self.counter == frames:
            self.counter = 0

    def update(self, speed):
        if (70 <= self.rect.x <= 775) and (55 <= self.rect.y <= 450):
            if self.direction == "right":
                self.rect.x += speed
            elif self.direction == "left":
                self.rect.x -= speed
            elif self.direction == "up":
                self.rect.y += speed
            elif self.direction == "down":
                self.rect.y -= speed
            return True
        return False
