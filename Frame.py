class Frame:
    def __init__(self):
        self.throws = []
        self.startingThrow = 0
        
    def __init__(self, throws):
        self.throws = throws
        self.startingThrow = len(self.throws)

    def FrameSize(self):
        pass

    def Score(self):
        pass

    def FirstBonusBall(self):
        return self.throws[self.startingThrow + self.FrameSize()]
    
    def SecondBonusBall(self):
        return self.throws[self.startingThrow + self.FrameSize() + 1]
