import pygame
import spritesheet
import random
from direction import random_direction, find_direction


class OgreBadGuy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sheet = spritesheet.SpriteSheet("ogrebadguy.png")
        self.image = self.sheet.get_image(0, 128, 64, 63)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(66, 706)
        self.rect.y = random.randint(50, 378)
        self.counter = 0
        self.timer = 0
        self.health = 4
        self.playerX = 0
        self.playerY = 0
        self.animation_timer = 0
        self.dashing = 0
        self.direction = random_direction()
        self.dash_direction = ""
        self.dash_counter = random.randint(0, 49)
        self.dash_timer = random.randint(40, 70)

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

    def animation(self, dashing):
        if not dashing:
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

        else:
            if self.direction == "right":
                self.image = self.sheet.get_image(self.counter * 64, 192, 64, 64)
            elif self.direction == "left":
                self.image = self.sheet.get_image(self.counter * 64, 64, 64, 64)
            elif self.direction == "up":
                self.image = self.sheet.get_image(self.counter * 64, 0, 64, 64)
            elif self.direction == "down":
                self.image = self.sheet.get_image(self.counter * 64, 128, 64, 64)

            self.counter += 1

            if self.counter == 9:
                self.counter = 0

    def update(self, x, y):
        self.playerX = x
        self.playerY = y

        if self.dashing == 0:
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
                        self.animation(False)
                        self.rect.x += 3
                    if self.direction == "left":
                        self.animation(False)
                        self.rect.x -= 3
                    if self.direction == "up":
                        self.animation(False)
                        self.rect.y -= 3
                    if self.direction == "down":
                        self.animation(False)
                        self.rect.y += 3
                    self.timer += 1
        else:
            if (70 <= self.rect.x <= 710) and (55 <= self.rect.y <= 384):
                if self.dash_direction == "right":
                    self.animation(True)
                    self.rect.x += 12
                if self.dash_direction == "left":
                    self.animation(True)
                    self.rect.x -= 12
                if self.dash_direction == "up":
                    self.animation(True)
                    self.rect.y -= 12
                if self.dash_direction == "down":
                    self.animation(True)
                    self.rect.y += 12
                self.dash_counter -= 1
            else:
                self.dashing = 0
                self.counter = 0
                if self.dash_direction == "right":
                    self.direction = "left"
                elif self.dash_direction == "left":
                    self.direction = "right"
                elif self.dash_direction == "up":
                    self.direction = "down"
                elif self.dash_direction == "down":
                    self.direction = "up"

    def dash(self):
        if self.dash_counter == self.dash_timer:
            self.dash_direction = find_direction((self.playerX, self.playerY), self.rect)
            if self.dash_direction == "up":
                self.dash_direction = "down"
            elif self.dash_direction == "down":
                self.dash_direction = "up"
            self.direction = self.dash_direction
            self.dash_timer = random.randint(30, 70)
            self.dashing = 40
            self.dash_counter = 0
        else:
            self.dash_counter += 1
