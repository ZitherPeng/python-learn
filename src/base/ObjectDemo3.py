# coding = utf-8
class Human(object):
    gender = None

    def __init__(self, input_gender):
        self.gender = input_gender

    def printGender(self):
        print self.gender


lilei = Human('male')
print lilei.gender
lilei.printGender()
