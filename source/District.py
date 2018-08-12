import pygame as pg, math, time

class Create_District:

    def __init__(self, name, rep, curPop, popMax):
        self.name = name
        self.rep = rep
        self.curPop = curPop
        self.popMax = popMax

    def updateStats(self, newRep, newCurPop):
        '''Updates the district's Reputation and Current Population'''
        self.rep = self.rep + newRep
        self.curPop = self.curPop + newCurPop

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

    def getPop(self):
        '''Returns the current population of the district'''
        return self.curPop

    def checkPop(self):
        '''Checks if the current population is greater than the max population and returns a boolean'''
        if self.curPop > self.popMax:
            return True
        else:
            return False