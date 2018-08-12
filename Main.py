import pygame as pg, sys, math, time, os, ctypes
from source import MainMenu, DetectMouse, FolderScreen

class Main():

    def __init__(self):
        # Game Clock
        self.clock = pg.time.Clock()
#        self.sw=ctypes.windll.user32.GetSystemMetrics(0)
#        self.sh=ctypes.windll.user32.GetSystemMetrics(1)
#        if self.sw/self.sh > (16/9):
#            self.screen_height=math.floor(self.sh)
#            self.screen_width=math.floor(self.sh*(16/9))
#        else:
#            self.screen_width=math.floor(self.sw)
#            self.screen_height=math.floor(self.sw*(9/16))
#        print(ctypes.windll.user32.GetSystemMetrics(0))
        self.screen_width=3840
        self.screen_height=2160

    def runGame(self):
        """Runs the Game"""
        # Starts the main menu
        self.main_menu = MainMenu.Main_Menu(self.screen_width,self.screen_height)
        self.main_menu.runScreen()
        # Init DetectMouse
        self.detect_mouse = DetectMouse.Detect_Mouse()
        self.folder_screen = FolderScreen.Folder(self.screen_width,self.screen_height)
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
                    if self.detect_mouse.MouseCheck(179*math.floor(self.screen_width/1920),407*math.floor(self.screen_width/1920),335*math.floor(self.screen_height/1080),685*math.floor(self.screen_height/1080)) == True:
                        # Detects a mouse click on the Newspaper
                        print ("Newspaper")
                    elif self.detect_mouse.MouseCheck(179*math.floor(self.screen_width/1920),488*math.floor(self.screen_width/1920),706*math.floor(self.screen_height/1080),918*math.floor(self.screen_height/1080)) == True:
                        # Detects a mouse click on the File Folder
                        self.folder_screen.runScreen()
                    elif self.detect_mouse.MouseCheck(692*math.floor(self.screen_width/1920),1226*math.floor(self.screen_width/1920),345*math.floor(self.screen_height/1080),814*math.floor(self.screen_height/1080)) == True:
                        # Detects a mouse click on the Computer
                        print ("Computer")
                    elif self.detect_mouse.MouseCheck(1464*math.floor(self.screen_width/1920),1692*math.floor(self.screen_width/1920),335*math.floor(self.screen_height/1080),513*math.floor(self.screen_height/1080)) == True:
                        # Detects a mouse click on the Phone
                        print ("Phone")
                    elif self.detect_mouse.MouseCheck(1382*math.floor(self.screen_width/1920),1552*math.floor(self.screen_width/1920),570*math.floor(self.screen_height/1080),813*math.floor(self.screen_height/1080)) == True:
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
