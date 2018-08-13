import pygame as pg, math, time

class Create_District:

    def __init__(self, name, rep=0, type=0, curPop=0, popMax=0):
        self.name = name
        self.rep = rep
        self.curPop = curPop
        self.popMax = popMax
        self.type = type

    def updateStats(self, newRep=0, newCurPop=0):
        '''Updates the district's Reputation and Current Population'''
        self.rep = self.rep + newRep
        self.curPop = self.curPop + newCurPop


    def getName(self):
        return self.name

    def getRep(self):
        '''Checks the current reputation and returns a title'''
        if self.rep < -100:
            return "Rebellious"
        elif self.rep >= -100 and self.rep < -50:
            return "Fearful"
        elif self.rep >= -50 and self.rep < -10:
            return "Scared"
        elif self.rep >= -10 and self.rep <= 10:
            return "Neutral"
        elif self.rep > 10 and self.rep <= 50:
            return "Liked"
        elif self.rep > 50:
            return "Favored"

    def getExactRep(self):
        return self.rep

    def getType(self):
        if self.type == 0:
            return "Urban"
        if self.type == 1:
            return "Residential"
        if self.type == 2:
            return "Rural"

    def getPop(self):
        '''Returns the current population of the district'''
        return self.curPop
    def getMaxPop(self):
        return self.popMax

    def checkPop(self):
        '''Checks if the current population is greater than the max population and returns a boolean'''
        if self.curPop > self.popMax:
            return True
        else:
            return False
