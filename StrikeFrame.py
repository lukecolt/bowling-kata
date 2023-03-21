from Frame import Frame

class StrikeFrame(Frame):
    def __init__(self, throws):
        throws.append(10)
    
    def Score(self):
        return 10 + self.FirstBonusBall() + self.SecondBonusBall()
    
    def FrameSize():
        return 1
    