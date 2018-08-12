import pygame as pg, sys, math, time, os, ctypes, platform

class Folder:

    def __init__(self):
        if (platform.system() == "Windows") == True:
            ctypes.windll.user32.SetProcessDPIAware()
            self.width = ctypes.windll.user32.GetSystemMetrics(0)
            self.height = ctypes.windll.user32.GetSystemMetrics(0)
        else:
            self.width = 1920
            self.height = 1080
        self.background = pg.image.load("assets/background.png")
        self.folderOpen = pg.image.load("assets/File_Folder_Open.png")
        self.backButton = pg.image.load("assets/back_button.png")
        self.folderOpen = pg.transform.scale(self.folderOpen,(1720,880))
        self.screen_color = (128, 0, 0)

    def runScreen(self):
        '''Starts the folder screen'''
        self.startscreen = pg.display.set_mode((self.width, self.height),pg.NOFRAME)
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.background, (0,0))
        self.startscreen.blit(self.folderOpen, (100,100))
        self.startscreen.blit(self.backButton, (0,954))
        pg.display.update()
