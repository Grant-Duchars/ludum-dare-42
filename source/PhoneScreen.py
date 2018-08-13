import pygame as pg, sys, math, time, os, ctypes, platform
from source import DetectMouse

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
            self.updateButton(self.phone1)
        elif self.detect_mouse.MouseCheck(1171,1336,104,270):
            self.lastNum = "2"
            self.updateButton(self.phone2)
        elif self.detect_mouse.MouseCheck(1415,1581,104,270):
            self.lastNum = "3"
            self.updateButton(self.phone3)
        elif self.detect_mouse.MouseCheck(924,1090,347,510):
            self.lastNum = "4"
            self.updateButton(self.phone4)
        elif self.detect_mouse.MouseCheck(1171,1336,347,510):
            self.lastNum = "5"
            self.updateButton(self.phone5)
        elif self.detect_mouse.MouseCheck(1415,1581,347,510):
            self.lastNum = "6"
            self.updateButton(self.phone6)
        elif self.detect_mouse.MouseCheck(924,1090,587,753):
            self.lastNum = "7"
            self.updateButton(self.phone7)
        elif self.detect_mouse.MouseCheck(1171,1336,587,753):
            self.lastNum = "8"
            self.updateButton(self.phone8)
        elif self.detect_mouse.MouseCheck(1415,1581,587,753):
            self.lastNum = "9"
            self.updateButton(self.phone9)
        elif self.detect_mouse.MouseCheck(924,1090,826,993):
            self.lastNum = "*"
            self.updateButton(self.phonePOUND)
        elif self.detect_mouse.MouseCheck(1171,1336,826,993):
            self.lastNum = "0"
            self.updateButton(self.phone0)
        elif self.detect_mouse.MouseCheck(1415,1581,826,993):
            self.lastNum = "#"
            self.updateButton(self.phoneHASH)
    
    def updateButton(self, butNum):
        self.startscreen.blit(butNum, (0,0))
        self.startscreen.blit(self.backButton, (0,954))
        pg.display.update()
        time.sleep(0.5)
        self.startscreen.blit(self.background, (0,0))
        self.startscreen.blit(self.backButton, (0,954))
        pg.display.update()