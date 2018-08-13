import pygame as pg, sys, math, time, os, ctypes, platform
from source import DetectMouse

class Folder:
<<<<<<< Updated upstream

    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height
        self.desk = pg.image.load("assets/Desk.png")
        self.desk = pg.transform.scale(self.desk,(7680*math.floor(self.screen_width/1920),4320*math.floor(self.screen_height/1080)))
        self.folderOpen = pg.image.load("assets/File_Folder_Open.png")
        self.folderOpen = pg.transform.scale(self.folderOpen,(1720*math.floor(self.screen_width/1920),880*math.floor(self.screen_height/1080)))
        self.pageOneR = pg.image.load("assets/redTabR.png")
        self.pageOneR = pg.transform.scale(self.pageOneR,(700*math.floor(self.screen_width/1920),800*math.floor(self.screen_height/1080)))
        self.pageTwoR = pg.image.load("assets/blueTabR.png")
        self.pageTwoR = pg.transform.scale(self.pageTwoR,(700*math.floor(self.screen_width/1920),800*math.floor(self.screen_height/1080)))
        self.pageThreeR = pg.image.load("assets/greenTabR.png")
        self.pageThreeR = pg.transform.scale(self.pageThreeR,(700*math.floor(self.screen_width/1920),800*math.floor(self.screen_height/1080)))
        self.pageOneL = pg.image.load("assets/redTabL.png")
        self.pageOneL = pg.transform.scale(self.pageOneL,(700*math.floor(self.screen_width/1920),800*math.floor(self.screen_height/1080)))
        self.pageTwoL = pg.image.load("assets/blueTabL.png")
        self.pageTwoL = pg.transform.scale(self.pageTwoL,(700*math.floor(self.screen_width/1920),800*math.floor(self.screen_height/1080)))
        self.pageThreeL = pg.image.load("assets/greenTabL.png")
        self.pageThreeL = pg.transform.scale(self.pageThreeL,(700*math.floor(self.screen_width/1920),800*math.floor(self.screen_height/1080)))
        self.pageFour = pg.image.load("assets/noTab.png")
        self.pageFour = pg.transform.scale(self.pageFour,(700*math.floor(self.screen_width/1920),800*math.floor(self.screen_height/1080)))
        self.backButton = pg.image.load("assets/back_button.png")
        self.backButton = pg.transform.scale(self.backButton,(124*math.floor(self.screen_width/1920),125*math.floor(self.screen_height/1080)))
=======
    def __init__(self):
        if (platform.system() == "Windows") == True:
            ctypes.windll.user32.SetProcessDPIAware()
            self.width = ctypes.windll.user32.GetSystemMetrics(0)
            self.height = ctypes.windll.user32.GetSystemMetrics(0)
        else:
            self.width = 1920
            self.height = 1080

            
        self.background = pg.image.load("assets/background.png")
        self.folderOpen = pg.image.load("assets/FileFolderOpen.png")
        self.folderOpen = pg.transform.scale(self.folderOpen,(1720,880))
>>>>>>> Stashed changes
        self.screen_color = (128, 0, 0)
        self.clock = pg.time.Clock()
        self.tabLoc = [0, 0, 0]

    def runScreen(self):
        '''Starts the folder screen'''
        self.startscreen = pg.display.set_mode((math.floor(self.screen_width), math.floor(self.screen_height)),pg.NOFRAME)
        pg.init()
        self.detect_mouse = DetectMouse.Detect_Mouse()
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageTwoR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageOneR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
        pg.display.update()
    def clickTab(self):
        if self.detect_mouse.MouseCheck(330*math.floor(self.screen_width/1920),365*math.floor(self.screen_width/1920),200*math.floor(self.screen_height/1080),350*math.floor(self.screen_height/1080)) == True and self.tabLoc[0] == 1:
            self.tabLoc = [0, 0, 0]
            self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageTwoR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
        elif self.detect_mouse.MouseCheck(1550*math.floor(self.screen_width/1920),1585*math.floor(self.screen_width/1920),200*math.floor(self.screen_height/1080),350*math.floor(self.screen_height/1080)) == True and self.tabLoc[0] == 0:
            self.tabLoc = [1, 0, 0]
            self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageTwoR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
        #blue tab control
        elif self.detect_mouse.MouseCheck(330*math.floor(self.screen_width/1920),365*math.floor(self.screen_width/1920),370*math.floor(self.screen_height/1080),520*math.floor(self.screen_height/1080)) == True and self.tabLoc[1] == 1:
            self.tabLoc = [1, 0, 0]
            self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageTwoR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
        elif self.detect_mouse.MouseCheck(1550*math.floor(self.screen_width/1920),1585*math.floor(self.screen_width/1920),370*math.floor(self.screen_height/1080),520*math.floor(self.screen_height/1080)) == True and self.tabLoc[1] == 0:
            self.tabLoc = [1, 1, 0]
            self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageTwoL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
        #green tab control
        elif self.detect_mouse.MouseCheck(330*math.floor(self.screen_width/1920),365*math.floor(self.screen_width/1920),550*math.floor(self.screen_height/1080),700*math.floor(self.screen_height/1080)) == True and self.tabLoc[2] == 1:
            self.tabLoc = [1, 1, 0]
            self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageTwoL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
        elif self.detect_mouse.MouseCheck(1550*math.floor(self.screen_width/1920),1585*math.floor(self.screen_width/1920),550*math.floor(self.screen_height/1080),700*math.floor(self.screen_height/1080)) == True and self.tabLoc[2] == 0:
            self.tabLoc = [1, 1, 1]
            self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageTwoL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageThreeL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageFour, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
        pg.display.update()
