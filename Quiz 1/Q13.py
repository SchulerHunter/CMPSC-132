class Exam:
    def __init__(self):
        self.x = 1
        self.__y = 1

    def getY(self):
        return self.__y

a = Exam()
a.x = 45
print(a.x)
