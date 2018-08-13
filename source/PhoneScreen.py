import pygame as pg, sys, math, time, os, ctypes, platform
from source import DetectMouse, CreatePhoneText

class Phone_Screen:

    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height
        self.contacts = {
        "6084758252":"army",
        "3079842748":"mob",
        "2175477508":"police",
        "6621278932":"looters",
        "3156546988":"power",
        "6072352348":"landlord"
        }
        self.lastNum = ""
        self.callNum = ""
        self.currentCall = ""
        self.screen_color = (128, 0, 0)
        self.backButton = pg.image.load("assets/back_button.png")
        self.background = pg.image.load("assets/phone zoom screens/phone zoom.png")
        self.phone0 = pg.image.load("assets/phone zoom screens/phone zoom0.png")
        self.phone1 = pg.image.load("assets/phone zoom screens/phone zoom1.png")
        self.phone2 = pg.image.load("assets/phone zoom screens/phone zoom2.png")
        self.phone3 = pg.image.load("assets/phone zoom screens/phone zoom3.png")
        self.phone4 = pg.image.load("assets/phone zoom screens/phone zoom4.png")
        self.phone5 = pg.image.load("assets/phone zoom screens/phone zoom5.png")
        self.phone6 = pg.image.load("assets/phone zoom screens/phone zoom6.png")
        self.phone7 = pg.image.load("assets/phone zoom screens/phone zoom7.png")
        self.phone8 = pg.image.load("assets/phone zoom screens/phone zoom8.png")
        self.phone9 = pg.image.load("assets/phone zoom screens/phone zoom9.png")
        self.phoneHASH = pg.image.load("assets/phone zoom screens/phone zoom#.png")
        self.phonePOUND = pg.image.load("assets/phone zoom screens/phone zoomPOUND.png")
    
    def runScreen(self):
        '''Starts the phone screen'''
        self.startscreen = pg.display.set_mode((self.screen_width, self.screen_height),pg.NOFRAME)
        self.detect_mouse = DetectMouse.Detect_Mouse()
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.background, (0,0))
        self.startscreen.blit(self.backButton, (0,954))
        pg.display.update()

    def clickButton(self):
        if self.detect_mouse.MouseCheck(924, 1090, 104, 270):
            self.lastNum = "1"
            self.callNum += self.lastNum
            self.updateButton(self.phone1)
        elif self.detect_mouse.MouseCheck(1171,1336,104,270):
            self.lastNum = "2"
            self.callNum += self.lastNum
            self.updateButton(self.phone2)
        elif self.detect_mouse.MouseCheck(1415,1581,104,270):
            self.lastNum = "3"
            self.callNum += self.lastNum
            self.updateButton(self.phone3)
        elif self.detect_mouse.MouseCheck(924,1090,347,510):
            self.lastNum = "4"
            self.callNum += self.lastNum
            self.updateButton(self.phone4)
        elif self.detect_mouse.MouseCheck(1171,1336,347,510):
            self.lastNum = "5"
            self.callNum += self.lastNum
            self.updateButton(self.phone5)
        elif self.detect_mouse.MouseCheck(1415,1581,347,510):
            self.lastNum = "6"
            self.callNum += self.lastNum
            self.updateButton(self.phone6)
        elif self.detect_mouse.MouseCheck(924,1090,587,753):
            self.lastNum = "7"
            self.callNum += self.lastNum
            self.updateButton(self.phone7)
        elif self.detect_mouse.MouseCheck(1171,1336,587,753):
            self.lastNum = "8"
            self.callNum += self.lastNum
            self.updateButton(self.phone8)
        elif self.detect_mouse.MouseCheck(1415,1581,587,753):
            self.lastNum = "9"
            self.callNum += self.lastNum
            self.updateButton(self.phone9)
        elif self.detect_mouse.MouseCheck(924,1090,826,993):
            self.lastNum = "*"
            self.callNum += self.lastNum
            self.updateButton(self.phonePOUND)
        elif self.detect_mouse.MouseCheck(1171,1336,826,993):
            self.lastNum = "0"
            self.callNum += self.lastNum
            self.updateButton(self.phone0)
        elif self.detect_mouse.MouseCheck(1415,1581,826,993):
            self.lastNum = "#"
            self.callNum += self.lastNum
            self.updateButton(self.phoneHASH)
    
    def updateButton(self, butNum):
        self.startscreen.blit(butNum, (0,0))
        self.startscreen.blit(self.backButton, (0,954))
        pg.display.update()
        time.sleep(0.5)
        self.startscreen.blit(self.background, (0,0))
        self.startscreen.blit(self.backButton, (0,954))
        pg.display.update()
    
    def checkNum(self):
        if len(self.callNum) < 10:
            print(self.callNum)
        elif len(self.callNum) > 10:
            self.callNum = ""
            self.lastNum = ""
        elif len(self.callNum) == 10:
            print(self.callNum)
            if self.callNum in self.contacts:
                self.currentCall = self.contacts[self.callNum]
                print(self.currentCall)
        if self.currentCall != "":
            return True
        else:
            return False

    def phoneCallInit(self):
        print("Phone Call Started")
        self.callscreen = None
        if self.currentCall == "army":
            self.index = 0
        elif self.currentCall == "mob":
            self.index = 1
        elif self.currentCall == "police":
            self.index = 2
        elif self.currentCall == "looters":
            self.index = 3
        elif self.currentCall == "power":
            self.index = 4
        elif self.currentCall == "landlord":
            self.index = 5
        self.choice = None

    def PhoneScript(self):
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
            self.drawer = CreatePhoneText.CreateText(self.screen_width, self.screen_height, 137, 838)
            self.drawer.AddText(self.ps[self.index][0],823, -50)
            self.drawer.AddText(self.ps[self.index][1])
            self.drawer.AddText("Yes.", 1250)
            self.drawer.AddText("No.", 1250, 64)
            self.drawer.ShowDisplayText()
            pg.display.update()
        elif self.callscreen == 1:
            self.drawer1 = CreatePhoneText.CreateText(self.screen_width, self.screen_height, 137, 838)
            self.drawer1.AddText(self.ps[self.index][0],823, -50)
            self.drawer1.AddText(self.ps[self.index][2])
            self.drawer1.AddText("Continue...", 1500, 64)
            self.drawer1.SetColor(0, 0, 0)
            self.drawer1.ShowDisplayText()
            pg.display.flip()
        elif self.callscreen == 2:
            self.drawer2 = CreatePhoneText.CreateText(self.screen_width, self.screen_height,137, 838)
            self.drawer2.ClearDisplayText()
            self.drawer2.AddText(self.ps[self.index][0],823, -50)
            self.drawer2.AddText(self.ps[self.index][4])
            self.drawer2.DrawRegionSelect(self)
            self.drawer2.ShowDisplayText()
            pg.display.flip()
        elif self.callscreen == 3:
            self.drawer3 = CreatePhoneText.CreateText(self.screen_width, self.screen_height, 137, 838)
            self.drawer3.ClearDisplayText()
            self.drawer3.AddText(self.ps[self.index][0],823, -50)
            self.drawer3.AddText(self.ps[self.index][3])
            self.drawer3.AddText("Continue...", 1500, 64)
            self.drawer3.ShowDisplayText()
            pg.display.flip()
            self.choice = "Cancel"
        elif self.callscreen == -1:
            self.drawer4 = CreatePhoneText.CreateText(self.screen_width, self.screen_height, 137, 838)
            self.drawer4.ClearDisplayText()
            self.finalstring = (self.ps[self.index][5]
            + " " + self.choice + "... " + self.ps[self.index][6])
            self.drawer4.AddText("Continue...", 1500, 64)
            self.drawer4.AddText(self.finalstring)
            self.drawer4.ShowDisplayText()
            pg.display.flip()

    def CallTracking(self):
        if self.callscreen == 0:
            if self.detect_mouse.MouseCheck(1387, 1500, 838, 870) == True:
                return 1
            elif self.detect_mouse.MouseCheck(1387, 1400, 902, 934) == True:
                return 3
        elif self.callscreen == 1:
            if self.detect_mouse.MouseCheck(1637, 1762, 902, 934) == True:
                return 2
        elif self.callscreen == 2:
            if self.detect_mouse.MouseCheck(1137, 1262, 838, 870) == True:
                self.choice = "Region 1"
                return -1
            elif self.detect_mouse.MouseCheck(1387, 1512, 838, 870) == True:
                self.choice = "Region 2"
                return -1
            elif self.detect_mouse.MouseCheck(1637, 1762, 838, 870) == True:
                self.choice = "Region 3"
                return -1
            elif self.detect_mouse.MouseCheck(1137, 1262, 902, 934) == True:
                self.choice = "Region 4"
                return -1
            elif self.detect_mouse.MouseCheck(1387, 1412, 902, 934) == True:
                self.choice = "Region 5"
                return -1
            elif self.detect_mouse.MouseCheck(1637, 1762, 902, 934) == True:
                self.choice = "Region 6"
                return -1
        elif self.callscreen == 3:
            if self.detect_mouse.MouseCheck(1637, 1762, 902, 934) == True:
                return None
        elif self.callscreen == -1:
            if self.detect_mouse.MouseCheck(1637, 1762, 902, 934) == True:
                return None