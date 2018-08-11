import pygame as pg, sys, time, math, os

class Main_Menu:

    def __init__(self):
        # Screen Settings
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
        self.fileFolder = pg.image.load("assets/file_folder_closed.png")
        self.phone = pg.image.load("assets/phone.png")
        self.contacts = pg.image.load("assets/contact_book.png")
        self.newspaper = pg.image.load("assets/newspaper.png")
        self.clock = pg.time.Clock()

    def runScreen(self):
        '''Starts the main menu screen'''
        pg.init()
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.background, (0,0))
        self.startscreen.blit(self.desk, (147, 302))
        pg.display.update()
        while True:
            self.clock.tick(10)
            events = pg.event.get()
            key = pg.key.get_pressed()
            for event in events: #If X is clicked, don't crash the window.
                if event.type == pg.QUIT:
                    sys.exit()
            if key[pg.K_ESCAPE]: #If Escape key is pressed, close window.
                sys.exit()