import pygame as pg, sys, math, time, os, ctypes
class Folder:
    def __init__(self, screen_width, screen_height):
        ctypes.windll.user32.SetProcessDPIAware()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background = pg.image.load("assets/background.png")
        self.background = pg.transform.scale(self.background,(1920*math.floor(self.screen_width/1920),1080*math.floor(self.screen_height/1080)))
        self.folderOpen = pg.image.load("assets/FileFolderOpen.png")
        self.folderOpen = pg.transform.scale(self.folderOpen,(1720*math.floor(self.screen_width/1920),880*math.floor(self.screen_height/1080)))
        self.screen_color = (128, 0, 0)
        self.clock = pg.time.Clock()
    def runScreen(self):
        '''Starts the folder screen'''
        self.startscreen = pg.display.set_mode((math.floor(self.screen_width), math.floor(self.screen_height)),pg.NOFRAME)
        pg.init()
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.background, (0,0))
        self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
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
