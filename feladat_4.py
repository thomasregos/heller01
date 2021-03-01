
class Ember:
    def __init__(self, name, birthy, gender):
        self.name = name
        self.birthy = birthy
        self.gender = gender

    def age21(self):
        print(2021-self.birthy)
        return 2021-self.birthy


class Tantargy:
    def __init__(self, name, descr, evf):
        self.name = name
        self.descr = descr
        self.evf = evf


class Diak(Ember):
    def __init__(self, oszt, atl, parent, name, birthy, gender):
        super().__init__(name, birthy, gender)
        self.oszt = oszt
        self.atl = atl
        self.parent = parent


class Tanar(Ember):
    def __init__(self, tantargyak, hetiora, oraber, ofo, name, birthy, gender, oszt=None):
        super().__init__(name, birthy, gender)
        self.tantargyak = tantargyak
        self.hetiora = hetiora
        self.oraber = oraber

        self.ofo = ofo
        if self.ofo:
            self.oszt = oszt

    def fizu(self):
        print(self.hetiora*4*self.oraber)
        return self.hetiora*4*self.oraber











aaa = Diak(12, 3, "Apa", "Jozsi", 1996, "Male")

aaa.age21()

