import pygame


class Transition(pygame.sprite.Sprite):

    def __init__(self):
        self.image = pygame.image.load('black.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, i):
        pass
