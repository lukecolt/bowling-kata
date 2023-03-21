from Frame import Frame

class BonusRoll(Frame):
    def __init__(self, throws, firstThrow):
        self.throws = throws
        self.startingThrow = len(throws)
        throws.append(firstThrow)

    def Score(self):
        return 0
    
    def FrameSize(self):
        return 0