from Frame import Frame

class SpareFrame(Frame):
    def __init__(self, throws, firstThrow, secondThrow):
        self.throws = throws
        self.startingThrow = len(throws)
        self.throws.append(firstThrow)
        self.throws.append(secondThrow)
    
    def Score(self):
        return 10 + self.FirstBonusBall()

    def FrameSize(self):
        return 2
   