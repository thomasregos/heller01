
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
        self.oszt.diakok.update({self.name: self})


class Tanar(Ember):
    def __init__(self, tantargyak, hetiora, oraber, ofo, name, birthy, gender, oszt=None):
        super().__init__(name, birthy, gender)
        self.tantargyak = tantargyak
        self.hetiora = hetiora
        self.oraber = oraber

        self.ofo = ofo
        if self.ofo:
            self.oszt = oszt
        else:
            self.oszt = None

    def fizu(self):
        print(self.hetiora*4*self.oraber)
        return self.hetiora*4*self.oraber


class evfolyam():
    def __init__(self):
        self.osztalyok = {}


class osztaly():
    def __init__(self, evfolyam, osztalynev):
        self.evfolyam = evfolyam
        self.osztalyn = osztalynev
        self.evfolyam.osztalyok.update({self.osztalyn: self})
        self.diakok = {}

evfolyam1 = evfolyam()
evfolyam2 = evfolyam()

osztaly1A = osztaly(evfolyam1, 'A')
osztaly1B = osztaly(evfolyam1, 'B')

osztaly2A = osztaly(evfolyam2, 'A')
osztaly2B = osztaly(evfolyam2, 'B')





Diak1 = Diak(osztaly1A, 3, "PJesus", "Jozsi", 1996, "Male")
Diak2 = Diak(osztaly1B, 3.45, "PMaria", "Jose", 1995, "Male")
Diak3 = Diak(osztaly2A, 2.11, "PKaroly", "Felicia", 1997, "Female")
Diak4 = Diak(osztaly2B, 3.14, "PEzio", "Napsugar", 1996, "Female")
Diak5 = Diak(osztaly1A, 4.5, "PAlma", "Mano", 1995, "Male")
# Diak6 = Diak(osztaly1A, 3, "Karoly", "Jozsi", 1996, "Male")
# Diak7 = Diak(osztaly1A, 3, "Karoly", "Jozsi", 1996, "Male")
# Diak8 = Diak(osztaly1A, 3, "Karoly", "Jozsi", 1996, "Male")

Diak1.age21()



# van ismetlodes körbe körbe mehetsz a oszt--diakok--diak--oszt
# de muszaj az evfolyamot is atadni mert kulonben nem lehet updatelni kezdjuk ott