import pygame as pg, sys, math, time, os, ctypes, platform

class Turns:

    def __init__(self, totalDays, curPop, popGoal):
        self.actions = 6
        self.totalDays = totalDays
        self.curPop = curPop
        self.popGoal = popGoal

    def spendAction(self, num):
        '''Spends (X) actions and returns false is incapable'''
        if self.actions - num < 0:
            return False
        else:
            self.actions = self.actions - num
            return True

    def endTurn(self, curPop):
        '''Returns a 2 for a win, a 3 for a lose, and a 1 for anything else'''
        self.actions = 6
        self.curPop = curPop
        self.totalDays = self.totalDays - 1
        if self.totalDays < 0 and self.popGoal < self.curPop:
            return 3
        elif self.totalDays < 0 and self.popGoal >= self.curPop:
            return 2
        else:
            return 1
        