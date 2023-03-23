from Frame import Frame
from OpenFrame import OpenFrame
from SpareFrame import SpareFrame
from StrikeFrame import StrikeFrame
from BonusRoll import BonusRoll

class BowlingGame:
    def __init__(self):
        self.throws = []
        self.frames = []
    
    def strike(self):
        self.frames.append(StrikeFrame(self.throws))

    def spare(self, firstThrow, secondThrow):
        self.frames.append(SpareFrame(self.throws,  firstThrow, secondThrow))

    def open(self, firstThrow, secondThrow):
        self.frames.append(OpenFrame(self.throws, firstThrow, secondThrow))

    def roll(self, roll):
        self.frames.append(BonusRoll(self.throws, roll))

    def score(self):
        number = 0
        for frame in self.frames :
            number += frame.Score()
        return number 
