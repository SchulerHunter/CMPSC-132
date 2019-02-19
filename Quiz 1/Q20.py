import random
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__id=self.__createID()+self.age

    def __createID(self):
        return random.randint(10, 500)

    def __str__(self):
        return "Subject #{}: {}, {} year(s) old".format(self.__id, self.name, self.age)

rocky = Dog('Rocky', 8)
print(rocky)
rocky._id = 900
print(rocky)
