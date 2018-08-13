import pygame
WHITE = (255, 255, 255)


'''
# Creates a Sprite

# Format:

# MakeSprite("filename.filextension", xPos, yPos)

# Example:

#     penis = MakeSprite("penis.png", 0, 0)

# The above code makes an object penis with the sprite from "penis.png"
# Remember you still have to stage your sprite
'''

class MakeSprite(pygame.sprite.Sprite):

    def __init__(self, filename, xpos, ypos):

        super().__init__()

        self.image = pygame.Surface((1920, 1080))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)


        pygame.draw.rect(self.image, WHITE, [xpos, ypos, 1920, 1080])


        self.image = pygame.image.load(filename).convert_alpha()
        pygame.transform.scale(self.image, (1920, 1080))

        self.rect = (self.image.get_rect())
        self.rect.x = xpos
        self.rect.y = ypos




'''
Global reputation system

    han = 0
    han = Reputation(7)

The above code creates the han object and assigns it a reputation of 7

    han.CurrentRep()

The above code will return the reputation of the han object

    han.AddRep(2)

The above code will add 2 rep to the han object
Use negative numbers to subtract rep
'''

class Reputation:

    rep = 0

    def __init__(self, val):
        self.rep = val

    def AddRep(self, val):
        self.rep += val

    def CurrentRep(self):
        return self.rep


'''
Compares position of mouse against boundaries
Returns True if mouse is within boundaries
Returns False if mouse is outside boundaries

Format:

    MouseCheck(Xmin, Xmax, Ymin, Ymax)

Example:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if MouseCheck(925, 1095, 100, 275) == True:
                print("In the zone, autozone!")
            else:
                print("Sorry buddy, no tires!")


The above code will print the text if the mouse is within
the boundaries X:925-1095 and Y:100-275
'''



