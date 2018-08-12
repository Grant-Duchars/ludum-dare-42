import pygame as pg, sys, time, math, os, platform, ctypes

class Main_Menu:

    def __init__(self):
        if (platform.system() == "Windows") == True:
            ctypes.windll.user32.SetProcessDPIAware()
            self.width = ctypes.windll.user32.GetSystemMetrics(0)
            self.height = ctypes.windll.user32.GetSystemMetrics(0)
        else:
            self.width = 1920
            self.height = 1080
        self.winX = 0
        self.winY = 0
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (self.winX,self.winY)
        self.startscreen = pg.display.set_mode((self.width, self.height),pg.NOFRAME)
        pg.display.set_caption("Ludum Dare 42")
        self.background = pg.Surface(self.startscreen.get_size())
        self.background = self.background.convert()
        self.screen_color = (128, 0, 0)
        self.background = pg.image.load("assets/background.png")
        self.desk = pg.image.load("assets/desk.png")
        self.computer = pg.image.load("assets/computer.png")
        self.fileFolder = pg.image.load("assets/file_folder.png")
        self.phone = pg.image.load("assets/phone.png")
        self.contacts = pg.image.load("assets/contact_book.png")
        self.newspaper = pg.image.load("assets/newspaper.png")

    def runScreen(self):
        '''Starts the main menu screen'''
        pg.init()
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.background, (0,0))
        self.startscreen.blit(self.desk, (147,302))
        self.startscreen.blit(self.computer, (692,345))
        self.startscreen.blit(self.fileFolder, (179,706))
        self.startscreen.blit(self.phone, (1464,335))
        self.startscreen.blit(self.contacts, (1382,570))
        self.startscreen.blit(self.newspaper, (179,335))
        pg.display.update()
