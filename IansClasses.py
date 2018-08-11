import pygame
WHITE = (255, 255, 255)


class MakeSprite(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, filename, xpos, ypos):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([50, 50])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, WHITE, [xpos, ypos, 50, 50])

        # Instead we could load a proper pciture of a car...
        self.image = pygame.image.load(filename).convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
