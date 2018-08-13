import pygame as pg, sys, math, time, os, ctypes, platform
from random import randint
from source import MainMenu, DetectMouse, FolderScreen, ContactBook, ComputerScreen, NewspaperScreen, District, Turns, PhoneScreen, CreateText

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
        self.startPop = 0
        self.popGoal = 0
        self.phoneActive = False
        self.callActive = False
        self.regionChoice = None
        self.lastContact = None

    def runGame(self):
        """Runs the Game"""
        # Starts the main menu
        self.main_menu = MainMenu.Main_Menu(self.screen_width, self.screen_height)
        self.main_menu.runScreen()
        # Init DetectMouse
        self.detect_mouse = DetectMouse.Detect_Mouse()
        # Create Districts
        self.district1 = District.Create_District("Shade", randint(-20,20), randint(0,2), randint(200000,250000),   300000) #(name, reputation, type startpop, maxpop)
        self.district2 = District.Create_District("Zen", randint(-20,20), randint(0,2), randint(200000,300000),   500000)
        self.district3 = District.Create_District("Venom", randint(-20,20), randint(0,2), randint(500000,700000),   1000000)
        self.district4 = District.Create_District("Glove", randint(-20,20), randint(0,2), randint(600000,1000000),  1250000)
        self.district5 = District.Create_District("Hacks", randint(-20,20), randint(0,2), randint(1500000,1750000), 2000000)
        self.district6 = District.Create_District("Data", randint(-20,20), randint(0,2), randint(800000,1000000),  1200000)
        self.district7 = District.Create_District("Mercury", randint(-20,20), randint(0,2), randint(500000,700000),   900000)
        self.district8 = District.Create_District("Circuit", randint(-20,20), randint(0,2), randint(500000,700000),   750000)
        self.government = self.district8 = District.Create_District("Government", 15)

        self.district_pops = [self.district1.getPop(), self.district2.getPop(),
        self.district3.getPop(), self.district4.getPop(), self.district5.getPop(),
        self.district6.getPop(), self.district7.getPop(), self.district8.getPop()]

        self.district_reps = [self.district1.getRep(), self.district2.getRep(),
        self.district3.getRep(), self.district4.getRep(), self.district5.getRep(),
        self.district6.getRep(), self.district7.getRep(), self.district8.getRep()]

        self.district_exact_reps = [self.district1.getExactRep(), self.district2.getExactRep(),
        self.district3.getExactRep(), self.district4.getExactRep(), self.district5.getExactRep(),
        self.district6.getExactRep(), self.district7.getExactRep(), self.district8.getExactRep()]

        self.district_max_pops = [self.district1.getMaxPop(), self.district2.getMaxPop(),
        self.district3.getMaxPop(), self.district4.getMaxPop(), self.district5.getMaxPop(),
        self.district6.getMaxPop(), self.district7.getMaxPop(), self.district8.getMaxPop()]

        self.district_types = [self.district1.getType(), self.district2.getType(),
        self.district3.getType(), self.district4.getType(), self.district5.getType(),
        self.district6.getType(), self.district7.getType(), self.district8.getType()]

        self.total_pop = 0
        self.total_rep = 0
        self.gov_rep = self.government.getRep()

        for x in range(len(self.district_pops)):
            self.total_pop += self.district_pops[x]

        for x in range(len(self.district_exact_reps)):
            self.total_rep += self.district_exact_reps[x]
            self.total_rep /= len(self.district_exact_reps)

        if self.total_rep < -100:
            self.total_rep = "Rebellious"
        elif self.total_rep >= -100 and self.total_rep < -50:
            self.total_rep = "Fearful"
        elif self.total_rep >= -50 and self.total_rep < -10:
            self.total_rep = "Scared"
        elif self.total_rep >= -10 and self.total_rep <= 10:
            self.total_rep = "Neutral"
        elif self.total_rep > 10 and self.total_rep <= 50:
            self.total_rep = "Liked"
        elif self.total_rep > 50:
            self.total_rep = "Favored"


        print(self.district_pops)
        print(self.district_reps)
        print(self.district_max_pops)
        print(self.district_types)

        #Create drawing object
        self.drawer = CreateText.CreateText(self.screen_width, self.screen_height)
        # Gets current pop
        self.startPop = self.district1.getPop() + self.district2.getPop() + self.district3.getPop() + self.district4.getPop() + self.district5.getPop() + self.district6.getPop() + self.district7.getPop() + self.district8.getPop()
        # Generates main goal
        self.popGoal = math.floor(self.startPop * (1/3))
        # Init Turns
        self.turnManager = Turns.Turns(21, self.startPop, self.popGoal)
        # Init Folder Screen
        self.folder_screen = FolderScreen.Folder(self.screen_width, self.screen_height, self.startPop, self.popGoal)
        # Init Contacts Screen
        self.contact_book = ContactBook.Contact_Book(self.screen_width, self.screen_height)
        # Init Computer Screen
        self.computer_screen = ComputerScreen.Computer_Screen(self.screen_width,
        self.screen_height, self.drawer,
        self.district_pops, self.district_reps,
        self.district_max_pops, self.district_types,
        self.total_pop, self.total_rep, self.gov_rep
        )
        # Init Newspaper Screen
        self.newspaper_screen = NewspaperScreen.Newspaper_Screen(self.screen_width, self.screen_height)
        # Init Phone Screen
        self.phone_screen = PhoneScreen.Phone_Screen(self.screen_width, self.screen_height)
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
                            self.phone_screen.runScreen()
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
                elif self.curScreen == 3: # COMPUTER
                    if event.type == pg.MOUSEBUTTONDOWN:

                        if self.detect_mouse.MouseCheck(0,122*math.floor(self.screen_width/1920),954*math.floor(self.screen_height/1080),1080*math.floor(self.screen_height/1080)) == True:
                            self.main_menu.runScreen()
                            self.curScreen = 0
                elif self.curScreen == 4:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if self.phoneActive == False:
                            self.phone_screen.clickButton()
                            if self.phone_screen.checkNum() == True:
                                self.phoneActive = True
                        elif self.phoneActive == True:
                            self.main_menu.runScreen()
                        if self.detect_mouse.MouseCheck(0,122*math.floor(self.screen_width/1920),954*math.floor(self.screen_height/1080),1080*math.floor(self.screen_height/1080)) == True:
                            self.main_menu.runScreen()
                            self.curScreen = 0
                    if self.phoneActive == True and self.callActive == False:
                        self.phone_screen.phoneCallInit()
                        self.phone_screen.ChangeScreen()
                        self.callActive = True
                    elif self.phoneActive == True and self.callActive == True:
                        if event.type == pg.MOUSEBUTTONDOWN:
                            if self.phone_screen.CallTracking() == 1:
                                self.phone_screen.ChangeScreen(1)
                            elif self.phone_screen.CallTracking() == 2:
                                self.phone_screen.ChangeScreen(2)
                            elif self.phone_screen.CallTracking() == 3:
                                self.phone_screen.ChangeScreen(3)
                            elif self.phone_screen.CallTracking() == -1:
                                self.phone_screen.ChangeScreen(-1)
                                self.regionChoice = self.phone_screen.getRegion()
                                self.lastContact = self.phone_screen.getContact()
                                self.phone_screen.lastNum = ""
                                self.phone_screen.callNum = ""
                                self.phone_screen.currentCall = ""
                                print ("-------------")
                                print (self.regionChoice)
                                print (self.lastContact)
                                print ("-------------")
                                if self.turnManager.spendAction(1) == 1:
                                    print ("Used one action")
                                elif self.turnManager.spendAction(1) == 2:
                                    print ("Used an action and ended turn")
                                else:
                                    print ("Out of actions, please end turn")
                                print (self.turnManager.actions)
                                self.phoneActive = False
                                self.callActive = False
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
