import pygame as pg, sys, math, time, os, ctypes
class Folder:
    def __init__(self, screen_width, screen_height):
        ctypes.windll.user32.SetProcessDPIAware()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.desk = pg.image.load("assets/Desk.png")
        self.desk = pg.transform.scale(self.desk,(7680*math.floor(self.screen_width/1920),4320*math.floor(self.screen_height/1080)))
        self.folderOpen = pg.image.load("assets/FileFolderOpen.png")
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
        self.screen_color = (128, 0, 0)
        self.clock = pg.time.Clock()
    def runScreen(self):
        '''Starts the folder screen'''
        self.startscreen = pg.display.set_mode((math.floor(self.screen_width), math.floor(self.screen_height)),pg.NOFRAME)
        pg.init()
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageTwoR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageOneR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))

        self.startscreen.blit(self.pageOneL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageTwoL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageThreeL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
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
