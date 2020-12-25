import pygame


class Score(object):
    def __init__(self, screen):
        self.screen = screen
        self.file = open("highscore.txt", "r")
        self.font = pygame.font.Font('freesansbold.ttf', 25)
        self.highscore = int(self.file.read())
        self.score = 0
        self.highscore_text = self.font.render(('Score ' + str(self.highscore)), True, (255, 255, 255))
        self.highscore_rect = self.highscore_text.get_rect()
        self.background = pygame.image.load('gameover.jpg')
        self.text = self.font.render(('Score ' + str(self.score)), True, (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (400, 20)

    def points(self, event):
        if event == "skeleton death":
            self.score += 10
            self.text = self.font.render(('Score ' + str(self.score)), True, (255, 255, 255))
        elif event == "ogre death":
            self.score += 12
            self.text = self.font.render(('Score ' + str(self.score)), True, (255, 255, 255))
        elif event == "room clear":
            self.score += 30
            self.text = self.font.render(('Score ' + str(self.score)), True, (255, 255, 255))

    def blit(self):
        if self.score > self.highscore:
            self.file = open("highscore.txt", "w")
            self.file.write(str(self.score))
            self.highscore = self.score
        self.screen.blit(self.text, self.rect)

    def end_blit(self):
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.text = self.font.render(('Score ' + str(self.score)), True, (255, 255, 255))
        self.rect.center = (580, 80)
        self.highscore_text = self.font.render(('Highscore ' + str(self.highscore)), True, (255, 255, 255))
        self.highscore_rect.center = (500, 200)
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.highscore_text, self.highscore_rect)
        self.screen.blit(self.text, self.rect)
