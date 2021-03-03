from statistics import mean

# for each 'Tantargy' which students learn it
# for reach teacher you know who she/he teaches
# ...


class Ember:
    def __init__(self, name, birthy, gender):
        self.name = name
        self.birthy = birthy
        self.gender = gender

    def age21(self):
        print(2021-self.birthy)
        return 2021-self.birthy


class Tantargy:
    def __init__(self, name, leiras, evf):
        self.name = name
        self.leiras = leiras

        self.evfolyam = {}
        self.diakok = {}
        for evfoly in evf:
            self.evfolyam.update({evfoly.name: evfoly})
            self.diakok.update(evfoly.diakok)






class Diak(Ember):
    def __init__(self, oszt, atl, parent, name, birthy, gender):
        super().__init__(name, birthy, gender)
        self.oszt = oszt
        self.atl = atl
        self.parent = parent
        self.oszt.diakok.update({self.name: self})
        self.oszt.evfolyam.diakok.update({self.name: self})


class Tanar(Ember):
    def __init__(self, name, birthy, gender, tantargyak, hetiora, oraber, ofo, oszt=None):
        super().__init__(name, birthy, gender)
        self.hetiora = hetiora
        self.oraber = oraber
        self.birthy = birthy
        self.gender = gender
        self.name = name

        self.tantargyak = {}
        self.diakok = {}
        for tantargy in tantargyak:
            self.tantargyak.update({tantargy.name: tantargy})
            self.diakok.update(tantargy.diakok)

        self.ofo = ofo
        if self.ofo:
            self.oszt = oszt
            self.oszt.ofo = self
        else:
            self.oszt = None


    def fizu(self):
        print(self.hetiora*4*self.oraber)
        return self.hetiora*4*self.oraber

    def atlag_osztaly(self):
        # returns the mean of the own class of the teacher (if she/he has one)
        if not self.ofo:
            return None

        atlag_l = []
        for diak in self.oszt.diakok.keys():
            atlag_l.append(self.oszt.diakok[diak].atl)

        # TODO: list comprehension

        return mean(atlag_l)

    def atlag_tantargy(self):
        # returns the mean of the subjects the teacher teaches

        # atlag_l = [i.atl for i in self.diakok.items()]
        atlag_l = []
        for diak in self.diakok.keys():
            atlag_l.append(self.diakok[diak].atl)

        return mean(atlag_l)




class Evfolyam():
    def __init__(self, name):
        self.name = name
        self.osztalyok = {}
        self.diakok = {}


class Osztaly():
    def __init__(self, evfolyam, osztalynev):
        self.evfolyam = evfolyam
        self.osztalyn = osztalynev
        self.evfolyam.osztalyok.update({self.osztalyn: self})
        self.diakok = {}
        self.ofo = None


class Igazgato(Tanar):
    def __init__(self, bonus, name, birthy, gender, tantargyak, hetiora, oraber, ofo, oszt=None):
        super().__init__(name, birthy, gender, tantargyak, hetiora, oraber, ofo, oszt=None)
        self.hetiora = hetiora
        self.oraber = oraber
        self.birthy = birthy
        self.gender = gender
        self.name = name
        self.bonusz = bonus

    def fizuu(self):
        normal = self.fizu()
        print(normal+self.bonusz)
        return normal+self.bonusz


evfolyam1 = Evfolyam('11')
evfolyam2 = Evfolyam('12')

osztaly1A = Osztaly(evfolyam1, 'A')
osztaly1B = Osztaly(evfolyam1, 'B')
osztaly2A = Osztaly(evfolyam2, 'A')
osztaly2B = Osztaly(evfolyam2, 'B')

Diak1 = Diak(osztaly1A, 3, "PJesus", "Jozsi", 1996, "Male")
Diak2 = Diak(osztaly1B, 3.45, "PMaria", "Jose", 1995, "Male")
Diak3 = Diak(osztaly2A, 2.11, "PKaroly", "Felicia", 1997, "Female")
Diak4 = Diak(osztaly2B, 3.14, "PEzio", "Napsugar", 1996, "Female")
Diak5 = Diak(osztaly1A, 4.5, "PAlma", "Mano", 1995, "Male")
Diak6 = Diak(osztaly1B, 2.11, "PLaura", "Pizzi", 1998, "Male")
Diak7 = Diak(osztaly2A, 4.98, "PBorcini", "Bernard", 1996, "Male")
Diak8 = Diak(osztaly2B, 3.78, "PPedro", "Carlos", 1994, "Male")
Diak9 = Diak(osztaly1A, 2.01, "PVicenzo", "Juanita", 1998, "Female")
Diak10 = Diak(osztaly1B, 4.21, "PBernini", "Carla", 1998, "Female")

Tantargy1 = Tantargy('Matek', 'You wont have a calculator in your pocket', [evfolyam1, evfolyam2])
Tantargy2 = Tantargy('Spanyol', 'The very essence of life is beginner spanish', [evfolyam1])
Tantargy3 = Tantargy('Info', 'Google: Stackoverflow', [evfolyam2])

Tanar1 = Tanar('Eva', 1980, 'Female', [Tantargy1], 40, 1100, True, osztaly1A)
Tanar2 = Tanar('Gyuri', 1969, 'Male', [Tantargy3], 50, 1150, True, osztaly2B)
Tanar3 = Tanar('Anita', 1975, 'Female', [Tantargy2], 40, 950, False)

igazgato = Igazgato(88000, 'Eva', 1983, 'Female', [], 55, 1400, False)

igazgato.fizuu()

aaa=Tanar1.atlag_osztaly()
print(aaa)

aaa = Tanar2.atlag_tantargy()
print(aaa)


Diak1.age21()













# van ismetlodes körbe körbe mehetsz a oszt--diakok--diak--oszt
# de muszaj az evfolyamot is atadni mert kulonben nem lehet updatelni kezdjuk ott

# attributomokat nem lehet valahogy atadni a parent classbol hogy ugyanugy bekerje es ugyanazt csinalja vele?