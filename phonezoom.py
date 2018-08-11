import pygame

from IansClasses import *
#from MouseCheck import MouseCheck
pygame.init()
running = True
WHITE = (255, 255, 255)

k_space = False

SCREENWIDTH=1920
SCREENHEIGHT=1080

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)

all_sprites_list = pygame.sprite.Group()

phone = MakeSprite("assets/Phone Zoom Screens/Phone Zoom.png",0,0)

all_sprites_list.add(phone)
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:

            print(MouseCheck(925, 1095, 100, 275))

#
#            if ((x >= 925) and (x <= 1095)) and ((y >= 100) and (y <= 275)):
#                print("x: " + str(x))
#                print("y: " + str(y))

    all_sprites_list.update()



    all_sprites_list.draw(screen)
    pygame.display.flip()

        #elif event.type == pygame.MOUSEBUTTONUP:
        #    pos = pygame.mouse.get_pos()

pygame.quit()
