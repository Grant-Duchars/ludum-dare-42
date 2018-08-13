import pygame, time
from IansClasses import *
from PhoneCall import *
#from MouseCheck import MouseCheck
pygame.init()
running = True
WHITE = (255, 255, 255)



SCREENWIDTH=1920
SCREENHEIGHT=1080

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)

all_sprites_list = pygame.sprite.Group()

def_phone = MakeSprite("assets/Phone Zoom Screens/Phone Zoom.png",0,0)
phone_1 = MakeSprite("assets/Phone Zoom Screens/Phone Zoom1.png",0,0)
phone_2 = MakeSprite("assets/Phone Zoom Screens/Phone Zoom2.png",0,0)
phone_3 = MakeSprite("assets/Phone Zoom Screens/Phone Zoom3.png",0,0)
phone_4 = MakeSprite("assets/Phone Zoom Screens/Phone Zoom4.png",0,0)
phone_5 = MakeSprite("assets/Phone Zoom Screens/Phone Zoom5.png",0,0)
phone_6 = MakeSprite("assets/Phone Zoom Screens/Phone Zoom6.png",0,0)
phone_7 = MakeSprite("assets/Phone Zoom Screens/Phone Zoom7.png",0,0)
phone_8 = MakeSprite("assets/Phone Zoom Screens/Phone Zoom8.png",0,0)
phone_9 = MakeSprite("assets/Phone Zoom Screens/Phone Zoom9.png",0,0)
phone_star = MakeSprite("assets/Phone Zoom Screens/Phone ZoomStar.png",0,0)
phone_0 = MakeSprite("assets/Phone Zoom Screens/Phone Zoom0.png",0,0)
phone_pound = MakeSprite("assets/Phone Zoom Screens/Phone ZoomPound.png",0,0)


callnum = ""
last_num = ""
butnum = def_phone
buttonpressed = False
currentcall = ""

all_sprites_list.add(def_phone)

def Dial():
    global last_num
    global butnum
    global buttonpressed
    if MouseCheck(925, 1095, 100, 275) == True:
        butnum = phone_1
        buttonpressed = True
        last_num = "1"

    elif MouseCheck(1170, 1340, 100, 275) == True:
        butnum = phone_2
        buttonpressed = True
        last_num = "2"

    elif MouseCheck(1415, 1585, 100, 275) == True:
        butnum = phone_3
        buttonpressed = True
        last_num = "3"

    elif MouseCheck(925, 1095, 345, 515) == True:
        butnum = phone_4
        buttonpressed = True
        last_num = "4"

    elif MouseCheck(1170, 1340, 345, 515) == True:
        butnum = phone_5
        buttonpressed = True
        last_num = "5"

    elif MouseCheck(1415, 1585, 345, 515) == True:
        butnum = phone_6
        buttonpressed = True
        last_num = "6"

    elif MouseCheck(925, 1095, 580, 750) == True:
        butnum = phone_7
        buttonpressed = True
        last_num = "7"

    elif MouseCheck(1170, 1340, 580, 750) == True:
        butnum = phone_8
        buttonpressed = True
        last_num = "8"

    elif MouseCheck(1415, 1585, 580, 750) == True:
        butnum = phone_9
        buttonpressed = True
        last_num = "9"

    elif MouseCheck(925, 1095, 815, 985) == True:
        butnum = phone_star
        buttonpressed = True
        last_num = "*"

    elif MouseCheck(1170, 1340, 815, 985) == True:
        butnum = phone_0
        buttonpressed = True
        last_num = "0"

    elif MouseCheck(1415, 1585, 815, 985) == True:
        butnum = phone_pound
        buttonpressed = True
        last_num = "#"

    if buttonpressed == True:

        all_sprites_list.add(butnum)
        all_sprites_list.remove(def_phone)

contacts = {
"6084758252":"army",
"3079842748":"mob",
"2175477508":"police",
"6621278932":"looters",
"3156546988":"power",
"6072352348":"landlord"
}

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            Dial()
            callnum += last_num

        if event.type == pygame.MOUSEBUTTONUP:
            if len(callnum) <= 10:

                buttonpressed = False
                all_sprites_list.add(def_phone)
                all_sprites_list.remove(butnum)
                print(callnum)
                print(currentcall)


            if len(callnum) == 10:
                buttonpressed = False
                if callnum in contacts:
                    currentcall = contacts[callnum]
                    print(callnum)
                    print(currentcall)

            elif len(callnum) > 10:
                callnum = ""
                last_num = ""
                butnum = def_phone
                buttonpressed = False
                print(callnum)
                print(currentcall)

        if currentcall != "":
            import PhoneCall
            running = False
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()


pygame.quit()
