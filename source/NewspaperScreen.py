import pygame as pg, sys, math, time, os, ctypes, platform

class Newspaper_Screen:
    
    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height
        self.background = pg.image.load("assets/newspaper_zoomed.png")
        self.backButton = pg.image.load("assets/back_button.png")
        self.screen_color = (128, 0, 0)
    
    def runScreen(self):
        '''Starts the newspaper screen'''
        self.startscreen = pg.display.set_mode((self.screen_width, self.screen_height),pg.NOFRAME)
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.background, (0,0))
        self.startscreen.blit(self.backButton, (0,954))
        pg.display.update()