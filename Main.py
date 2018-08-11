import pygame as pg, sys, math, time
from source import MainMenu

class Main():

    def __init__(self):
        # Initial Window Size
        self.width = 1000
        self.height = 1000
        # Game Clock
        self.clock = pg.time.Clock()

    def runGame(self):
        """Runs the Game"""
        # Starts the main menu
        self.main_menu = MainMenu.Main_Menu()
        self.main_menu.runScreen()
        # Sets the screen to game screen
        self.screen = pg.display.set_mode((math.floor(self.width* 3/2), self.height))

def main():
    pg.init()
    while True:
        main = Main()
        main.runGame()

main()