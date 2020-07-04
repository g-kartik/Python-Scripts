class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x1 = self.x
        y1 = self.y
        x2 = other.x
        y2 = other.y
        d = ((x2-x1)**2 + (y2-y1)**2)**0.5
        return(d)
    def __str__(self):
        return("<" + str(self.x) + "," + str(self.y) + ">" )
    def __add__(self, other):
        sumx = self.x + other.x
        sumy = self.y + other.y
        return(Coordinate(sumx, sumy))
    def iscollinear(self, *args):
        x1 = self.x
        y1 = self.y
        x2 = args[0].x
        y2 = args[0].y
        m = (y2-y1)/(x2-x1)
        for obj in args:
            if abs((obj.y-y1)/(obj.x-x1)- m) > 1e-3:
                return(False)
        return(True)