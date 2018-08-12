import pygame as pg, sys, math, time, os, ctypes
class Folder:
    def __init__(self):
        ctypes.windll.user32.SetProcessDPIAware()
        self.width = ctypes.windll.user32.GetSystemMetrics(0)
        self.height = ctypes.windll.user32.GetSystemMetrics(0)
        self.background = pg.image.load("assets/background.png")
        self.folderOpen = pg.image.load("assets/FileFolderOpen.png")
        self.folderOpen = pg.transform.scale(self.folderOpen,(1720,880))
        self.screen_color = (128, 0, 0)
        self.clock = pg.time.Clock()
    def runScreen(self):
        '''Starts the folder screen'''
        self.startscreen = pg.display.set_mode((self.width, self.height),pg.NOFRAME)
        pg.init()
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.background, (0,0))
        self.startscreen.blit(self.folderOpen, (100,100))
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
