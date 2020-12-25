import pygame


class Portal(pygame.sprite.Sprite):

    def __init__(self, wall):
        self.wall = wall
        if wall == "up":
            self.image = pygame.image.load("secretportal1.png").convert_alpha()
        if wall == "down":
            self.image = pygame.image.load("secretportal3.png").convert_alpha()
        if wall == "right":
            self.image = pygame.image.load("secretportal4.png").convert_alpha()
        if wall == "left":
            self.image = pygame.image.load("secretportal2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))

    def goto(self,wall):

        if wall == 1:
            self.rect.x = 330
            self.rect.y = -25
        if wall == 2:
            self.rect.x = -25
            self.rect.y = 190
        if wall == 3:
            self.rect.x = 350
            self.rect.y = 440
        if wall == 4:
            self.rect.x = 755
            self.rect.y = 175

    def update(self):
        return True
