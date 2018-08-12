import pygame as pg, sys, time, math, os, ctypes

class Main_Menu:

    def __init__(self, screen_width, screen_height):
        # Screen Settings
        ctypes.windll.user32.SetProcessDPIAware()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.winX = 0
        self.winY = 0
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (self.winX,self.winY)
        #self.startscreen = pg.display.set_mode((math.floor(self.screen_width), math.floor(self.screen_height)),pg.NOFRAME)
        self.startscreen = pg.display.set_mode((pg.display.Info().current_w, pg.display.Info().current_h),pg.NOFRAME)
        pg.display.set_caption("Ludum Dare 42")
        self.background = pg.Surface(self.startscreen.get_size())
        self.background = self.background.convert()
        self.screen_color = (128, 0, 0)
        self.background = pg.image.load("assets/background.png")
        self.background = pg.transform.scale(self.background,(1920*math.floor(self.screen_width/1920),1080*math.floor(self.screen_height/1080)))
        self.desk = pg.image.load("assets/desk.png")
        self.desk = pg.transform.scale(self.desk,(1626*math.floor(self.screen_width/1920),778*math.floor(self.screen_height/1080)))
        self.computer = pg.image.load("assets/computer.png")
        self.computer = pg.transform.scale(self.computer,(544*math.floor(self.screen_width/1920),565*math.floor(self.screen_height/1080)))
        self.fileFolder = pg.image.load("assets/file_folder.png")
        self.fileFolder = pg.transform.scale(self.fileFolder,(309*math.floor(self.screen_width/1920),214*math.floor(self.screen_height/1080)))
        self.phone = pg.image.load("assets/phone.png")
        self.phone = pg.transform.scale(self.phone,(228*math.floor(self.screen_width/1920),176*math.floor(self.screen_height/1080)))
        self.contacts = pg.image.load("assets/contact_book.png")
        self.contacts = pg.transform.scale(self.contacts,(179*math.floor(self.screen_width/1920),246*math.floor(self.screen_height/1080)))
        self.newspaper = pg.image.load("assets/newspaper.png")
        self.newspaper = pg.transform.scale(self.newspaper,(235*math.floor(self.screen_width/1920),352*math.floor(self.screen_height/1080)))

    def runScreen(self):
        '''Starts the main menu screen'''
        pg.init()
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.background, (0,0))
        self.startscreen.blit(self.desk, (147*math.floor(self.screen_width/1920),302*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.computer, (692*math.floor(self.screen_width/1920),345*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.fileFolder, (179*math.floor(self.screen_width/1920),706*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.phone, (1464*math.floor(self.screen_width/1920),335*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.contacts, (1382*math.floor(self.screen_width/1920),570*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.newspaper, (179*math.floor(self.screen_width/1920),335*math.floor(self.screen_height/1080)))
        pg.display.update()
