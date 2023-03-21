from Frame import Frame

class SpareFrame(Frame):
    def __init__(self, throws, firstThrow, secondThrow):
        throws.append(firstThrow)
        throws.append(secondThrow)
    
    def Score(self):
        return 10 + self.FirstBonusBall()

    def FrameSize():
        return 2
   