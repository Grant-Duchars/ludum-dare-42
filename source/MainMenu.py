import pygame as pg, sys, time, math

class Main_Menu:

    def __init__(self):
        # Screen Settings
        self.width = 1000
        self.height = 800
        self.startscreen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Ludum Dare 42")
        self.background = pg.Surface(self.startscreen.get_size())
        self.background = self.background.convert()
        self.screen_color = (128, 0, 0)
        self.clock = pg.time.Clock()

    def runScreen(self):
        '''Starts the main menu screen'''
        pg.init()
        self.startscreen.fill(self.screen_color)
        pg.display.update()
        while True:
            self.clock.tick(10)
            events = pg.event.get()
            key = pg.key.get_pressed()
            for event in events: #If X is clicked, don't crash the window.
                if event.type == pg.QUIT:
                    sys.exit()
            if key[pg.K_RETURN]: #If Return key is pressed, start game.
                break