import pygame
from data import spritesheet


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sheet = spritesheet.SpriteSheet("data/Magesprite.png")
        self.image = self.sheet.get_image(0, 128, 64, 63)
        self.live_image = pygame.image.load('data/lives.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 240
        self.counter = 0
        self.health = 5
        self.timer = 0
        self.cooldown = 0

    def collision(self, sprite):
        return self.rect.colliderect(sprite)

    def enemy_collision(self, enemy):
        if self.rect.colliderect(enemy):
            if self.cooldown == 0:
                self.health -= 1
                self.cooldown = 20

    def bone_collision(self, bone, bones):
        if self.rect.colliderect(bone):
            bones.remove(bone)
            self.health -= 1

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y
        if not self.cooldown == 0:
            self.cooldown -= 1
        if self.health <= 0:
            return False
        return True

    def lives(self, lives):
        return self.live_image, ((28*lives + 30), 20, 26, 26)

    def animation(self, direction, moved):
        if not moved:
            self.counter = 0

        if direction == "right":
            self.image = self.sheet.get_image(self.counter * 64, 192, 64, 63)
        elif direction == "left":
            self.image = self.sheet.get_image(self.counter * 64, 64, 64, 64)
        elif direction == "up":
            self.image = self.sheet.get_image(self.counter * 64, 0, 64, 64)
        elif direction == "down":
            self.image = self.sheet.get_image(self.counter * 64, 128, 64, 64)

        if self.timer % 2 == 0 and self.timer != 0:
            self.counter += 1

        if self.timer == 18:
            self.timer = 0
            self.counter = 0

        self.timer += 1
