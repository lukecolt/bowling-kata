from Frame import Frame

class StrikeFrame(Frame):
    def __init__(self, throws):
        self.throws = throws
        self.startingThrow = len(throws)
        self.throws.append(10)
    
    def Score(self):
        return 10 + self.FirstBonusBall() + self.SecondBonusBall()
    
    def FrameSize(self):
        return 1
    