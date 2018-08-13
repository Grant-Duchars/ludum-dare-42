import pygame as pg, sys, math, time, os, ctypes, platform


class Computer_Screen:

    def __init__(self, width, height, drawer, pops, reps, max_pops, types, total_pop, total_rep, gov_rep, map_updater):
        self.screen_width = width
        self.screen_height = height
        self.background = pg.image.load("assets/computer_zoomed.png")
        self.backButton = pg.image.load("assets/back_button.png")
        self.screen_color = (128, 0, 0)
        self.pops = pops
        self.reps = reps
        self.max_pops = max_pops
        self.types = types
        self.drawer = drawer
        self.total_pop = total_pop
        self.total_rep = total_rep
        self.gov_rep = gov_rep
        self.map_updater = map_updater
        print(total_pop)

    def MapUpdate(self, district):
        if self.map_updater != None:
            self.drawer.AddText(str(self.reps[district]), 1514, 910)
            self.drawer.AddText(str(self.types[district]), 1305, 910)
            self.drawer.AddText(str(self.pops[district]), 928, 910)
            self.drawer.ShowDisplayText()
            print(reps[district])
            pg.display.update()

    def runScreen(self):
        '''Starts the computer screen'''
        self.startscreen = pg.display.set_mode((self.screen_width, self.screen_height),pg.NOFRAME)
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.background, (0,0))
        self.startscreen.blit(self.backButton, (0,954))
        self.drawer.AddText(str(self.total_pop), 85, 820)
        self.drawer.AddText(str(self.total_rep), 85, 520)
        self.drawer.AddText(str(self.gov_rep), 85, 220)
        self.MapUpdate(0)
        self.drawer.ShowDisplayText()
        pg.display.update()
