class Human(object):
    laugh = 'hahahaha'

    def show_laugh(self):
        print self.laugh

    def laugh_10th(self):
        for i in range(10):
            self.show_laugh()


li_lei = Human()
li_lei.laugh_10th()
