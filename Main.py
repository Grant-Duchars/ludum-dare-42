import pygame as pg, sys, math, time, os, ctypes, platform
from source import MainMenu, DetectMouse, FolderScreen, ContactBook, ComputerScreen, NewspaperScreen

class Main():

    def __init__(self):
        # Game Clock
        self.clock = pg.time.Clock()
        # Determines Computer's OS
        if platform.system() == "Windows":
            self.os_is_windows = True
        else:
            self.os_is_windows = False
        if (platform.system() == "Windows") == True:
            ctypes.windll.user32.SetProcessDPIAware()
            self.width = pg.display.Info().current_w
            self.height = pg.display.Info().current_h
        else:
            self.width = 1920
            self.height = 1080
        self.screen_width = self.width
        self.screen_height = self.height
        # Saves current screen
        self.curScreen = 0
        # Desk = 0, Newspaper = 1, Folder = 2,
        # Computer = 3, Phone = 4, Contacts = 5.

    def runGame(self):
        """Runs the Game"""
        # Starts the main menu
        self.main_menu = MainMenu.Main_Menu(self.screen_width, self.screen_height)
        self.main_menu.runScreen()
        # Init DetectMouse
        self.detect_mouse = DetectMouse.Detect_Mouse()
        # Init Folder Screen
        self.folder_screen = FolderScreen.Folder(self.screen_width, self.screen_height)
        # Init Contacts Screen
        self.contact_book = ContactBook.Contact_Book()
        # Init Computer Screen
        self.computer_screen = ComputerScreen.Computer_Screen()
        # Init Newspaper Screen
        self.newspaper_screen = NewspaperScreen.Newspaper_Screen()

        # Main Game Loop
        while True:
            self.clock.tick(10)
            # Handles exiting the window
            events = pg.event.get()
            key = pg.key.get_pressed()
            for event in events: #If X is clicked, don't crash the window.
                if event.type == pg.QUIT:
                    sys.exit()
                if self.curScreen == 0:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if self.detect_mouse.MouseCheck(179*math.floor(self.screen_width/1920),407*math.floor(self.screen_width/1920),335*math.floor(self.screen_height/1080),685*math.floor(self.screen_height/1080)) == True:
                            self.newspaper_screen.runScreen()
                            self.curScreen = 1
                        elif self.detect_mouse.MouseCheck(179*math.floor(self.screen_width/1920),488*math.floor(self.screen_width/1920),706*math.floor(self.screen_height/1080),918*math.floor(self.screen_height/1080)) == True:
                            self.folder_screen.runScreen()
                            self.curScreen = 2
                        elif self.detect_mouse.MouseCheck(692*math.floor(self.screen_width/1920),1226*math.floor(self.screen_width/1920),345*math.floor(self.screen_height/1080),814*math.floor(self.screen_height/1080)) == True:
                            self.computer_screen.runScreen()
                            self.curScreen = 3
                        elif self.detect_mouse.MouseCheck(1464*math.floor(self.screen_width/1920),1692*math.floor(self.screen_width/1920),335*math.floor(self.screen_height/1080),513*math.floor(self.screen_height/1080)) == True:
                            self.curScreen = 4
                        elif self.detect_mouse.MouseCheck(1382*math.floor(self.screen_width/1920),1552*math.floor(self.screen_width/1920),570*math.floor(self.screen_height/1080),813*math.floor(self.screen_height/1080)) == True:
                            self.contact_book.runScreen()
                            self.curScreen = 5
                elif self.curScreen == 1:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if self.detect_mouse.MouseCheck(0,122*math.floor(self.screen_width/1920),954*math.floor(self.screen_height/1080),1080*math.floor(self.screen_height/1080)) == True:
                            self.main_menu.runScreen()
                            self.curScreen = 0
                elif self.curScreen == 2:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        self.folder_screen.clickTab()
                        if self.detect_mouse.MouseCheck(0,122*math.floor(self.screen_width/1920),954*math.floor(self.screen_height/1080),1080*math.floor(self.screen_height/1080)) == True:
                            self.main_menu.runScreen()
                            self.curScreen = 0
                elif self.curScreen == 3:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if self.detect_mouse.MouseCheck(0,122*math.floor(self.screen_width/1920),954*math.floor(self.screen_height/1080),1080*math.floor(self.screen_height/1080)) == True:
                            self.main_menu.runScreen()
                            self.curScreen = 0
                elif self.curScreen == 5:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if self.detect_mouse.MouseCheck(0,122*math.floor(self.screen_width/1920),954*math.floor(self.screen_height/1080),1080*math.floor(self.screen_height/1080)) == True:
                            self.main_menu.runScreen()
                            self.curScreen = 0

            if key[pg.K_ESCAPE]: #If Escape key is pressed, close window.
                sys.exit()

def main():
    pg.init()
    while True:
        main = Main()
        main.runGame()

main()
