import pygame as pg, sys, math, time, os
from source import MainMenu, FolderScreen

class Main():

    def __init__(self):
        # Game Clock
        self.clock = pg.time.Clock()

    def runGame(self):
        """Runs the Game"""
        # Starts the main menu
        self.main_menu = MainMenu.Main_Menu()
        self.folder_screen = FolderScreen.Folder()
        self.folder_screen.runScreen()
        # Sets the screen to game screen
        self.screen = pg.display.set_mode((math.floor(self.width* 3/2), self.height))

def main():
    pg.init()
    while True:
        main = Main()
        main.runGame()

main()
