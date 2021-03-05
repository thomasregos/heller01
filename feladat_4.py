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
        # print(self.hetiora*4*self.oraber)
        return self.hetiora*4*self.oraber

    def atlag_osztaly(self):
        # returns the mean of the own class of the teacher (if she/he has one)
        if not self.ofo:
            return None

        atlag_l = [self.oszt.diakok[diak].atl for diak in self.oszt.diakok.keys()]

        return mean(atlag_l)

    def atlag_tantargy(self):
        # returns the mean of the subjects the teacher teaches
        # atlag_l = [self.diakok[i].atl for i in self.diakok.keys()]
        atlag_l = []
        for tantargy, t_value in self.tantargyak.items():
            for evfolyam, e_value in t_value.evfolyam.items():
                for diak, d_value in e_value.diakok.items():
                    atlag_l.append(d_value.atl)

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
        # self.tantargyak = {}
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
        # print(normal+self.bonusz)
        return normal+self.bonusz


class Iskola():
    def __init__(self, tanarok, diakok, igazgato):
        self.tanarok = {}
        self.diakok = {}
        self.igazgato = igazgato

        # Tanarok
        for tanar in tanarok:
            self.tanarok.update({tanar.name: tanar})

        # Diakok
        for diak in diakok:
            self.diakok.update({diak.name: diak})

    def sum_salary(self):
        salary = 0
        for tanar in self.tanarok:
            salary += self.tanarok[tanar].fizu()

        salary += self.igazgato.fizuu()

        return salary

    def tantargy_atlagok(self):
        # Tanarok altal tanitott targyakat tanulo diakok atlagai
        # Dict ahol a kulcsok a tanár nevei az érték pedig az általuk tanított diákok átlagainak átlaga
        atlagok = {tanar: self.tanarok[tanar].atlag_tantargy() for tanar in self.tanarok.keys()}

        return atlagok

    def best_studs(self):
        # legjobb diakokat tanito tanar
        atlagok = self.tantargy_atlagok()

        return max(atlagok, key=atlagok.get)

    def worst_stud(self):

        atlagok = {diak: values.atl for (diak, values) in self.diakok.items()}

        return min(atlagok, key=atlagok.get)


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

Iskola = Iskola([Tanar1, Tanar2, Tanar3], [Diak1, Diak2, Diak3, Diak4, Diak5,
                                           Diak6, Diak7, Diak8, Diak9, Diak10], igazgato)


# salaries
for tanar, values in Iskola.tanarok.items():
    print("{tnr} receives {sal} Ft monthly".format(tnr=tanar, sal=values.fizu()))

print("The head master is stacked as f*ck monthly: {sal} Ft".format(sal=Iskola.igazgato.fizuu()))
print("The full salaries paid by the school monthly is {sal} Ft".format(sal=Iskola.sum_salary()))

# academic results
best_teacher = Iskola.best_studs()
print("{tch} has the best students with an average of {avg}".format(tch=best_teacher,
                                                                    avg=Iskola.tanarok[best_teacher].atlag_tantargy()))
print("{std} needs the most practice".format(std=Iskola.worst_stud()))

print("\nNew year new people:")

# Newcomers
Diak11 = Diak(osztaly2A, 1.8, "PMichael", "Puccini", 1996, "Male")
# this will lower Guyri's avg and also he will be the worst student to see if the Iskola is really updated
Diak12 = Diak(osztaly2B, 3.2, "PKaffka", "Amelia", 1998, "Female")
Diak13 = Diak(osztaly1A, 4.95, "PHaydn", "Bach", 1997, "Male")
Diak14 = Diak(osztaly1B, 4.1, "PVivaldi", "Katalin", 1995, "Female")

Tanar4 = Tanar('Dora', 1980, 'Female', [Tantargy2, Tantargy3], 40, 1080, False)

Iskola.diakok.update({Diak11.name: Diak11})
Iskola.diakok.update({Diak12.name: Diak12})
Iskola.diakok.update({Diak13.name: Diak13})
Iskola.diakok.update({Diak14.name: Diak14})

Iskola.tanarok.update({Tanar4.name: Tanar4})

# salaries
for tanar, values in Iskola.tanarok.items():
    print("{tnr} receives {sal} Ft monthly".format(tnr=tanar, sal=values.fizu()))

print("The head master is stacked as f*ck monthly: {sal} Ft".format(sal=Iskola.igazgato.fizuu()))
print("The full salaries paid by the school monthly is {sal} Ft".format(sal=Iskola.sum_salary()))

# academic results
best_teacher = Iskola.best_studs()
print("{tch} has the best students with an average of {avg}".format(tch=best_teacher,
                                                                    avg=Iskola.tanarok[best_teacher].atlag_tantargy()))
print("{std} needs the most practice".format(std=Iskola.worst_stud()))





# attributomokat nem lehet valahogy atadni a parent classbol hogy ugyanugy bekerje es ugyanazt csinalja vele?
