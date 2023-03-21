from Frame import Frame

class OpenFrame(Frame):
    def __init__(self, throws, firstThrow, secondThrow):
        self.throws = throws
        self.startingThrow = len(throws)
        self.throws.append(firstThrow)
        self.throws.append(secondThrow)

    def Score(self):
        return self.throws[self.startingThrow] + self.throws[self.startingThrow + 1]
    
    def FrameSize():
        return 2
    