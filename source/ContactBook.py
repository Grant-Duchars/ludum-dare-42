import pygame as pg, sys, math, time, os, ctypes, platform

class Contact_Book:
    
    def __init__(self):
        if (platform.system() == "Windows") == True:
            ctypes.windll.user32.SetProcessDPIAware()
            self.width = ctypes.windll.user32.GetSystemMetrics(0)
            self.height = ctypes.windll.user32.GetSystemMetrics(0)
        else:
            self.width = 1920
            self.height = 1080
        self.background = pg.image.load("assets/contact_book_zoomed.png")
        self.backButton = pg.image.load("assets/back_button.png")
        self.screen_color = (128, 0, 0)
    
    def runScreen(self):
        '''Starts the contacts screen'''
        self.startscreen = pg.display.set_mode((self.width, self.height),pg.NOFRAME)
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.background, (0,0))
        self.startscreen.blit(self.backButton, (0,954))
        pg.display.update()