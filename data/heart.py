import pygame


class Heart(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('lives.png')
        self.rect = self.image.get_rect()

    def goto(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def collision(self, player):
        if self.rect.colliderect(player):
            return True
        return False
