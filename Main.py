import pygame as pg, sys, math, time, os
from source import MainMenu, DetectMouse, FolderScreen

class Main():

    def __init__(self):
        # Game Clock
        self.clock = pg.time.Clock()

    def runGame(self):
        """Runs the Game"""
        # Starts the main menu
        self.main_menu = MainMenu.Main_Menu()
        self.main_menu.runScreen()
        # Init DetectMouse
        self.detect_mouse = DetectMouse.Detect_Mouse()
        self.folder_screen = FolderScreen.Folder()
        # Main Game Loop
        while True:
            self.clock.tick(5)
            # Handles exiting the window
            events = pg.event.get()
            key = pg.key.get_pressed()
            for event in events: #If X is clicked, don't crash the window.
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.detect_mouse.MouseCheck(179,407,335,685) == True:
                        # Detects a mouse click on the Newspaper
                        print ("Newspaper")
                    elif self.detect_mouse.MouseCheck(179,488,706,918) == True:
                        # Detects a mouse click on the File Folder
                        self.folder_screen.runScreen()
                    elif self.detect_mouse.MouseCheck(692,1226,345,814) == True:
                        # Detects a mouse click on the Computer
                        print ("Computer")
                    elif self.detect_mouse.MouseCheck(1464,1692,335,513) == True:
                        # Detects a mouse click on the Phone
                        print ("Phone")
                    elif self.detect_mouse.MouseCheck(1382,1552,570,813) == True:
                        # Detects a mouse click on the Contacts Book
                        print ("Contacts")
            if key[pg.K_ESCAPE]: #If Escape key is pressed, close window.
                sys.exit()
            # Detecting for clicks on main screen assets


def main():
    pg.init()
    while True:
        main = Main()
        main.runGame()

main()
