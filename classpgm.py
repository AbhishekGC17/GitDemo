class Family:
    def __init__(self, a, b):
        self.g = a
        self.h = b

    def member(self):
        print("hello every one")

    num = 100

    def sss(self):
        return self.g + self.h


a = 10
b = 20
obj = Family(a, b)
obj.member()
print(obj.sss())
