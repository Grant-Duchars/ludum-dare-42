import pygame
WHITE = (255, 255, 255)


class MakeSprite(pygame.sprite.Sprite):


    def __init__(self, filename, xpos, ypos):

        super().__init__()

        self.image = pygame.Surface([50, 50])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)


        pygame.draw.rect(self.image, WHITE, [xpos, ypos, 50, 50])


        self.image = pygame.image.load(filename).convert_alpha()


        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class Reputation:
    rep = 0

    def __init__(self, val):
        self.rep = val

    def AddRep(self, val):
        self.rep += val

    def CurrentRep(self):
        return self.rep
