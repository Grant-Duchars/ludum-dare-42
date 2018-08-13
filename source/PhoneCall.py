import pygame, time
from IansClasses import *
from phonezoom import currentcall

class CreateText:
    def __init__(self, TEXT_START_X=137, TEXT_START_Y=838):
        self.TEXT_START_X = TEXT_START_X
        self.TEXT_START_Y = TEXT_START_Y
        self.textstart = [TEXT_START_X, TEXT_START_Y]
        self.text = None
        self.color = (0, 0, 0)

        all_sprites_list.remove(phone)
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        screen.fill(WHITE)


        callbground = pygame.image.load("assets/Phone Zoom.png")
        screen.blit(callbground, (0,0))

        callwindow = pygame.image.load("assets/Text box.png")
        screen.blit(callwindow, (24, 733))
        pygame.display.flip()

        self.font = pygame.font.Font("assets/Phone Font.ttf", 50)
        self.lines = []
        self.xoffsets = []
        self.yoffsets = []

    def AddText(self, ulines, xoffs=0, yoffs=0):
        self.lines.append(ulines)
        self.xoffsets.append(xoffs)
        self.yoffsets.append(yoffs)

    def DrawRegionSelect(self, object):
        self.AddText(object.ps[6][0], 1000)
        self.AddText(object.ps[6][1], 1250)
        self.AddText(object.ps[6][2], 1500)
        self.AddText(object.ps[6][3], 1000, 64)
        self.AddText(object.ps[6][4], 1250, 64)
        self.AddText(object.ps[6][5], 1500, 64)

    def SetColor(self, r=0, g=0, b=0):
        self.color = (r, g, b)

    def ClearDisplayText(self):
        self.lines = []
        self.xoffsets = []
        self.yoffsets = []


    def ShowDisplayText(self):
        for line , xoffset, yoffset in zip(self.lines, self.xoffsets, self.yoffsets):
            self.text = self.font.render(line, True, self.color)
            screen.blit(self.text, [self.TEXT_START_X+xoffset,self.TEXT_START_Y+yoffset])
            pygame.display.flip()






class PhoneCall:

    def __init__(self,person):
        self.callscreen = None
        if person == "army":
            self.index = 0
        elif person == "mob":
            self.index = 1
        elif person == "police":
            self.index = 2
        elif person == "looters":
            self.index = 3
        elif person == "power":
            self.index = 4
        elif person == "landlord":
            self.index = 5
        self.choice = None

    def PhoneScript():
    self.opener = open("assets/Phone Scripts.txt", "r")
    self.temp = self.opener.read()
    self.temp2 = self.temp.split("*")
    self.phone_scripts = [[],[],[],[],[],[],[]]
    self.phone_scripts[0].append("Army")
    self.phone_scripts[1].append("Mob")
    self.phone_scripts[2].append("Police")
    self.phone_scripts[3].append("Looters")
    self.phone_scripts[4].append("Power")
    self.phone_scripts[5].append("Landlord")
    self.phone_scripts[6].extend(("Region 1", "Region 2",
    "Region 3", "Region 4", "Region 5", "Region 6"))
    for i in range(len(self.temp2)):
        self.temp = self.temp2[i].split("\"")
        for x in range(len(self.temp)):
            if x % 2 != 0:
                self.phone_scripts[i].append(self.temp[x])
    return self.phone_scripts

    def OnPhone(self):
        return self.index

    def ChangeScreen(self, var=0):
        self.callscreen = var

        self.ps = self.PhoneScript()
        if self.callscreen == 0:
            self.drawer = CreateText()
            self.drawer.AddText(self.ps[self.index][0],823, -50)
            self.drawer.AddText(self.ps[self.index][1])
            self.drawer.AddText("Yes.", 1250)
            self.drawer.AddText("No.", 1250, 64)
            self.drawer.ShowDisplayText()
        elif self.callscreen == 1:
            self.drawer1 = CreateText()
            self.drawer1.AddText(self.ps[self.index][0],823, -50)
            self.drawer1.AddText(self.ps[self.index][2])
            self.drawer1.AddText("Continue...", 1500, 64)
            self.drawer1.SetColor(0, 0, 0)
            self.drawer1.ShowDisplayText()
            pygame.display.flip()
        elif self.callscreen == 2:
            self.drawer2 = CreateText()
            self.drawer2.ClearDisplayText()
            self.drawer2.AddText(self.ps[self.index][0],823, -50)
            self.drawer2.AddText(self.ps[self.index][4])
            self.drawer2.DrawRegionSelect(self)
            self.drawer2.ShowDisplayText()
            pygame.display.flip()
        elif self.callscreen == 3:
            self.drawer3 = CreateText()
            self.drawer3.ClearDisplayText()
            self.drawer3.AddText(self.ps[self.index][0],823, -50)
            self.drawer3.AddText(self.ps[self.index][3])
            self.drawer3.AddText("Continue...", 1500, 64)
            self.drawer3.ShowDisplayText()
            pygame.display.flip()
            self.choice = "Cancel"
        elif self.callscreen == -1:
            self.drawer4 = CreateText()
            self.drawer4.ClearDisplayText()
            self.finalstring = (self.ps[self.index][5]
            + " " + self.choice + "... " + self.ps[self.index][6])
            self.drawer4.AddText("Continue...", 1500, 64)
            self.drawer4.AddText(self.finalstring)
            self.drawer4.ShowDisplayText()
            pygame.display.flip()


call = PhoneCall(currentcall)
call.ChangeScreen()

def CallTracking(var):
    if var.callscreen == 0:
        if MouseCheck(1387, 1500, 838, 870) == True:
#                    call.callscreen = 1
            var.ChangeScreen(1)

        elif MouseCheck(1387, 1400, 902, 934) == True:
#                    call.callscreen = 2
            var.ChangeScreen(3)


    elif var.callscreen == 1:
        if MouseCheck(1637, 1762, 902, 934) == True:
            var.ChangeScreen(2)

    elif var.callscreen == 2:
        if MouseCheck(1137, 1262, 838, 870) == True:
            var.choice = "Region 1"
            var.ChangeScreen(-1)
        elif MouseCheck(1387, 1512, 838, 870) == True:
            var.choice = "Region 2"
            var.ChangeScreen(-1)
        elif MouseCheck(1637, 1762, 838, 870) == True:
            var.choice = "Region 3"
            var.ChangeScreen(-1)
        elif MouseCheck(1137, 1262, 902, 934) == True:
            var.choice = "Region 4"
            var.ChangeScreen(-1)
        elif MouseCheck(1387, 1412, 902, 934) == True:
            var.choice = "Region 5"
            var.ChangeScreen(-1)
        elif MouseCheck(1637, 1762, 902, 934) == True:
            var.choice = "Region 6"
            var.ChangeScreen(-1)

    elif var.callscreen == 3:
        if MouseCheck(1637, 1762, 902, 934) == True:
            var.callscreen = None
#                   GO TO MAIN

    elif var.callscreen == -1:
        if MouseCheck(1637, 1762, 902, 934) == True:
            var.callscreen = None
#                   GO TO MAIN
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            CallTracking(call)

    pygame.display.flip()
pygame.quit()
