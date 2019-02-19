class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @property
    def distance(self):
        if type(self.p1) == type(self.p2):
            if type(self.p1) == Point2D:
                return(round(((self.p2.x-self.p1.x)**2+(self.p2.y-self.p1.y)**2)**.5,3))
            if type(self.p1) == Point3D:
                return(round(((self.p2.x-self.p1.x)**2+(self.p2.y-self.p1.y)**2+(self.p2.z-self.p1.z)**2)**.5,3))
        return("Error - Points of different dimensions")

    @property
    def midpoint(self):
        if type(self.p1) == type(self.p2):
            if type(self.p1) == Point2D:
                return((round((self.p1.x+self.p2.x)/2, 2), round((self.p1.y+self.p2.y)/2,2)))
            if type(self.p1) == Point3D:
                return((round((self.p1.x+self.p2.x)/2, 2), round((self.p1.y+self.p2.y)/2, 2), round((self.p1.z+self.p2.z)/2, 2)))
        return("Error - Points of different dimensions")
