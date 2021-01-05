from classpgm import Family


class child(Family):
    num2 = 200

    def __init__(self):
        Family.__init__(self,2,10)

    def sample(self):
        return (self.num2 + self.num + self.sss())


obj1 = child()
print(obj1.sample())
