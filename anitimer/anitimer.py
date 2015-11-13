class AniTimer(object):
    def __init__(self, fps=25, startframe=0):
        self.fps = fps
        self.startframe = startframe
        self.breakpoints = {}
        self.endframe = 0

    def passframes(self, framesno):
        if framesno.__class__.__name__ == 'int':
            corrector = 0
            if self.startframe == 0:
                corrector = 1
            self.endframe += framesno - corrector
            return True
        else:
            return False

    def secstoframes(self, secondsno):
        if secondsno.__class__.__name__ == 'int' or secondsno.__class__.__name__ == 'float':
            return int(secondsno * self.fps)

    def passseconds(self, secondsno):
        if secondsno.__class__.__name__ == 'int' or secondsno.__class__.__name__ == 'float':
            self.passframes(self.secstoframes(secondsno))
            return True
        else:
            return False

    def setbreakpoint(self, breakname):
        if breakname.__class__.__name__ == 'str':
            if breakname not in self.breakpoints.keys():
                self.breakpoints[breakname] = self.endframe
                return True
            else:
                return False
        else:
            return False

    def getbreakpoint(self, breakname):
        if breakname.__class__.__name__ == 'str':
            if breakname in self.breakpoints.keys():
                return self.breakpoints[breakname]
            else:
                return False
        else:
            return False
