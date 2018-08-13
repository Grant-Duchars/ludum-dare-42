import pygame as pg, sys, math, time, os, ctypes, platform
from source import DetectMouse
from random import randint

class Folder:

    def __init__(self, width, height, curPop, popGoal):
        self.screen_width = width
        self.screen_height = height
        self.curPop = curPop
        self.popGoal = popGoal
        self.desk = pg.image.load("assets/Desk.png")
        self.desk = pg.transform.scale(self.desk,(7680*math.floor(self.screen_width/1920),4320*math.floor(self.screen_height/1080)))
        self.folderOpen = pg.image.load("assets/File_Folder_Open.png")
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
        self.pageFour = pg.image.load("assets/noTab.png")
        self.pageFour = pg.transform.scale(self.pageFour,(700*math.floor(self.screen_width/1920),800*math.floor(self.screen_height/1080)))
        self.backButton = pg.image.load("assets/back_button.png")
        self.backButton = pg.transform.scale(self.backButton,(124*math.floor(self.screen_width/1920),125*math.floor(self.screen_height/1080)))
        self.screen_color = (128, 0, 0)
        self.clock = pg.time.Clock()
        self.tabLoc = [0, 0, 0]





        #district Names
        self.dNames = ["D1","D2","D3","D4","D5","D6","D7","D8"]
        #max and min % for Goals
        self.urgeGoalMin = .75
        self.urgeGoalMax = .85
        #mission counters
        self.misCntMain = 1
        self.misCntUrge = 0
        self.misCntSide = 0
        self.misCntTot = self.misCntMain + self.misCntUrge + self.misCntSide
        #mission lists
        self.mainGoal = "Lower Nirvana's population from "+str(self.curPop)+" to "+str(self.popGoal)+"."
        self.urgeGoal = []


        self.urgeGoalPop = []
        self.urgeGoalDis = []
        self.urgeGoalTime = []

        #initiating fonts
        pg.font.init()
        self.titleFont = pg.font.SysFont('Times New Roman', 40*math.floor(self.screen_width/1920))
        self.subFont = pg.font.SysFont('Times New Roman', 30*math.floor(self.screen_width/1920))
        self.parFont = pg.font.SysFont('Times New Roman', 20*math.floor(self.screen_width/1920))

    def missionUpdate(self, curPop, d1Pop, d2Pop, d3Pop, d4Pop, d5Pop, d6Pop, d7Pop, d8Pop):
        self.curPop = curPop
        self.dPopList = [d1Pop, d2Pop, d3Pop, d4Pop, d5Pop, d6Pop, d7Pop, d8Pop]
        for i in range(0,math.floor(len(self.urgeGoal))):
            if self.urgeGoalDis[i] <= self.urgeGoalPop[i]:
                self.urgeGoalTime[i] = 0
                self.misCntUrge=self.misCntUrge-1

        self.misCntTot = self.misCntMain + self.misCntUrge + self.misCntSide


    def dailyMissionUpdate(self):
        for i in range(0,math.floor(len(self.urgeGoalTime))):
        #time will stay zero when complete and -1 when failed
            if self.urgeGoalTime[i] != 0 and self.urgeGoalTime[i] != -1:
                self.urgeGoalTime[i] = self.urgeGoalTime[i]-1
                if self.urgeGoalTime[i] == 0:
                    self.urgeGoalTime[i] = -1
        self.distSelect = randint(0,7)
        self.urgeGoalDis.append(self.dPopList[self.distSelect])
        self.urgeGoalPop.append(randint(math.floor(self.urgeGoalMin*self.dPopList[self.distSelect]),math.floor(self.urgeGoalMax*self.dPopList[self.distSelect])))
        self.urgeGoalTime.append(1)
        self.urgeGoal.append("Lower the population of "+str(self.dNames[self.distSelect])+ " to "+ str(self.urgeGoalPop[len(self.urgeGoalPop)-1])+" within "+ str(self.urgeGoalTime[len(self.urgeGoalTime)-1])+" day.")
        self.misCntUrge = self.misCntUrge+1

        self.misCntTot = self.misCntMain + self.misCntUrge + self.misCntSide

    def urgeBlit(self):
        for i in range(0,math.floor(len(self.urgeGoal))):
            print(i)
            self.urgeMis = self.parFont.render(self.urgeGoal[i], False, (0, 0, 0))
            self.startscreen.blit(self.urgeMis,(400*math.floor(self.screen_width/1920),(300+40*i)*math.floor(self.screen_height/1080)))
    def mainBlit(self):
        self.mainText = self.parFont.render(self.mainGoal, False, (0, 0, 0))
        self.startscreen.blit(self.mainText,(400*math.floor(self.screen_width/1920),300*math.floor(self.screen_height/1080)))

    def runScreen(self):
        '''Starts the folder screen'''
        self.startscreen = pg.display.set_mode((math.floor(self.screen_width), math.floor(self.screen_height)),pg.NOFRAME)
        pg.init()
        self.detect_mouse = DetectMouse.Detect_Mouse()
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageTwoR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageOneR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
        #text
        self.pageOneTitle = self.titleFont.render('MISSION FOLDER', False, (0, 0, 0))
        self.pageOneSub = self.subFont.render('Please Complete Your '+str(self.misCntTot)+' Missions in the', False, (0, 0, 0))
        self.pageOneSubB = self.subFont.render('Allotted Time', False, (0, 0, 0))
        self.startscreen.blit(self.pageOneTitle,(1080*math.floor(self.screen_width/1920),300*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageOneSub,(1000*math.floor(self.screen_width/1920),450*math.floor(self.screen_height/1080)))
        self.startscreen.blit(self.pageOneSubB,(1150*math.floor(self.screen_width/1920),500*math.floor(self.screen_height/1080)))
        pg.display.update()

    def clickTab(self):
        if self.detect_mouse.MouseCheck(330*math.floor(self.screen_width/1920),365*math.floor(self.screen_width/1920),200*math.floor(self.screen_height/1080),350*math.floor(self.screen_height/1080)) == True and self.tabLoc[0] == 1:
            self.tabLoc = [0, 0, 0]
            self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageTwoR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneTitle,(1080*math.floor(self.screen_width/1920),300*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneSub,(1000*math.floor(self.screen_width/1920),450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneSubB,(1150*math.floor(self.screen_width/1920),500*math.floor(self.screen_height/1080)))
        elif self.detect_mouse.MouseCheck(1550*math.floor(self.screen_width/1920),1585*math.floor(self.screen_width/1920),200*math.floor(self.screen_height/1080),350*math.floor(self.screen_height/1080)) == True and self.tabLoc[0] == 0:
            self.tabLoc = [1, 0, 0]
            self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageTwoR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
            self.mainBlit()
        #blue tab control
        elif self.detect_mouse.MouseCheck(330*math.floor(self.screen_width/1920),365*math.floor(self.screen_width/1920),370*math.floor(self.screen_height/1080),520*math.floor(self.screen_height/1080)) == True and self.tabLoc[1] == 1:
            self.tabLoc = [1, 0, 0]
            self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageTwoR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
            self.mainBlit()
        elif self.detect_mouse.MouseCheck(1550*math.floor(self.screen_width/1920),1585*math.floor(self.screen_width/1920),370*math.floor(self.screen_height/1080),520*math.floor(self.screen_height/1080)) == True and self.tabLoc[1] == 0:
            self.tabLoc = [1, 1, 0]
            self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageTwoL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
            self.urgeBlit()
        #green tab control
        elif self.detect_mouse.MouseCheck(330*math.floor(self.screen_width/1920),365*math.floor(self.screen_width/1920),550*math.floor(self.screen_height/1080),700*math.floor(self.screen_height/1080)) == True and self.tabLoc[2] == 1:
            self.tabLoc = [1, 1, 0]
            self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageThreeR, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageTwoL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
            self.urgeBlit()
        elif self.detect_mouse.MouseCheck(1550*math.floor(self.screen_width/1920),1585*math.floor(self.screen_width/1920),550*math.floor(self.screen_height/1080),700*math.floor(self.screen_height/1080)) == True and self.tabLoc[2] == 0:
            self.tabLoc = [1, 1, 1]
            self.startscreen.blit(self.desk, (0,-2450*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.folderOpen, (100*math.floor(self.screen_width/1920),100*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageOneL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageTwoL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageThreeL, (255*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.pageFour, (955*math.floor(self.screen_width/1920),145*math.floor(self.screen_height/1080)))
            self.startscreen.blit(self.backButton, (0,954*math.floor(self.screen_height/1080)))
        pg.display.update()
