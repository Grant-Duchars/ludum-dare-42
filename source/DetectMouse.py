import pygame
class Detect_Mouse:

    def MouseCheck(self, xmin, xmax, ymin, ymax):
        x, y = pygame.mouse.get_pos()
        if ((x >= xmin) and (x <= xmax)) and ((y >= ymin) and (y <= ymax)):
            return True
        else:
            return False