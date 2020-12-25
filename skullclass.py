import pygame
import spritesheet
import random
from projectiles import Projectile
from direction import find_direction, random_direction


class SkullBadGuy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sheet = spritesheet.SpriteSheet("skullbadguy.png")
        self.image = self.sheet.get_image(0, 128, 64, 63)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(66, 706)
        self.rect.y = random.randint(50, 378)
        self.timer = 0
        self.counter = 0
        self.bone_counter = random.randint(0, 49)
        self.bone_timer = random.randint(50, 70)
        self.bone = 0
        self.playerX = 0
        self.playerY = 0
        self.health = 3
        self.bone_throw_direction = ""
        self.bone_list = []
        self.animation_timer = 0
        self.direction = random_direction()

    def collision(self, shots):
        for shot in shots:
            if shot.rect.colliderect(self.rect):
                self.health -= 1
                shots.remove(shot)
        if self.health == 0:
            if random.randint(1, 3) == 1:
                return False, True
            else:
                return False, False
        return True, False

    def animation(self):
        if self.direction == "right":
            self.image = self.sheet.get_image(self.counter * 64, 192, 64, 64)
        elif self.direction == "left":
            self.image = self.sheet.get_image(self.counter * 64, 64, 64, 64)
        elif self.direction == "up":
            self.image = self.sheet.get_image(self.counter * 64, 0, 64, 64)
        elif self.direction == "down":
            self.image = self.sheet.get_image(self.counter * 64, 128, 64, 64)

        if self.animation_timer % 2 == 0 and self.animation_timer != 0:
            self.counter += 1

        if self.animation_timer == 16:
            self.animation_timer = 0
            self.counter = 0

        self.animation_timer += 1

    def update(self, x, y, bones):
        self.playerX = x
        self.playerY = y
        self.bone_list = bones

        if self.timer == 30:
            self.direction = random_direction()
            self.timer = 0
        else:
            if self.direction == "right" and self.rect.x >= 710:
                self.direction = random_direction()
                self.timer = 0
            elif self.direction == "left" and self.rect.x <= 70:
                self.direction = random_direction()
                self.timer = 0
            elif self.direction == "up" and self.rect.y <= 55:
                self.direction = random_direction()
                self.timer = 0
            elif self.direction == "down" and self.rect.y >= 384:
                self.direction = random_direction()
                self.timer = 0
            else:
                if self.direction == "right":
                    self.animation()
                    self.rect.x += 3
                if self.direction == "left":
                    self.animation()
                    self.rect.x -= 3
                if self.direction == "up":
                    self.animation()
                    self.rect.y -= 3
                if self.direction == "down":
                    self.animation()
                    self.rect.y += 3
                self.timer += 1

    def bone_throw(self):
        if self.bone_counter == self.bone_timer:
            self.bone_throw_direction = find_direction((self.playerX, self.playerY), self.rect)
            self.bone_timer = random.randint(50, 70)
            self.bone = Projectile('bone.gif', self.bone_throw_direction, True, 32)
            if self.bone_throw_direction == "right":
                self.bone.goto((self.rect.x + 23), (self.rect.y + 25))
            if self.bone_throw_direction == "left":
                self.bone.goto((self.rect.x - 23), (self.rect.y + 25))
            if self.bone_throw_direction == "down":
                self.bone.goto((self.rect.x + 32), (self.rect.y - 25))
            if self.bone_throw_direction == "up":
                self.bone.goto(self.rect.x, (self.rect.y + 25))

            self.bone_counter = 0
            self.bone_list.append(self.bone)
        else:
            self.bone_counter += 1

        return self.bone_list
