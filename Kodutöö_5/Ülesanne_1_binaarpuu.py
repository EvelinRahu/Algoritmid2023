# Ülesanne: Rakenda binaarpuu andmestruktuur vabalt valitud programmeerimiskeeles.
# Kasutatud allikad: https://www.educative.io/answers/binary-trees-in-python ja ChatGPT

# Sõlme klassi loomine binaarpuu jaoks
class BinaarpuuS6lm:
    def __init__(self, v22rtus):
        self.v22rtus = v22rtus
        self.vasak_laps = None
        self.parem_laps = None

    # Funktsioon binaarpuule väärtuste lisamiseks
    def lisamine(self, v22rtus):

        # Võrdlen lisatava sõlme väärtust emasõlme (parent) väärtusega
        # Kui lisatava sõlme väärtus on väiksem kui emasõlm, siis liigub väärtus vasakusse alampuusse
        if v22rtus < self.v22rtus:
            #print("Sõlm:", v22rtus)
            #print("Emasõlm:", self.v22rtus)
            # Kontrollin, kas sõlmel on vasakut last (is not None)
            if self.vasak_laps:
                # Kui on, tuleb liikuda edasi mööda vasakut alampuud kuni jõuab leaf'ini (ehk sõlm, millel pole last)
                self.vasak_laps.lisamine(v22rtus)
            else:
                # Kui ei ole, luuakse uus sõlm ja väärtusest saab emasõlme vasak laps
                self.vasak_laps = BinaarpuuS6lm(v22rtus)

        # Kui lisatava sõlme väärtus on suurem kui emasõlm, siis liigub väärtus paremasse alampuusse
        else:
            if self.parem_laps:
                self.parem_laps.lisamine(v22rtus)
            else:
                self.parem_laps = BinaarpuuS6lm(v22rtus)
    
    # Funktsioon binaarpuust otsitava väärtuse leidmiseks
    def otsimine(self, otsitav_element):

        # Kontrollin, kas otsitav väärtus on võrdne juure väärtusega
        if otsitav_element == self.v22rtus:
           return self
        
        # Kui otsitav väärtus on väiksem kui emasõlm, otsi vasakust alampuust
        elif otsitav_element < self.v22rtus and self.vasak_laps:
            return self.vasak_laps.otsimine(otsitav_element)
        # Kui otsitav väärtus on suurem kui emasõlm, otsi paremast alampuust
        elif otsitav_element > self.v22rtus and self.parem_laps:
            return self.parem_laps.otsimine(otsitav_element)
        # Kui otsitavat väärtust ei leitud ja alampuusid enam pole, tagasta None
        else:
            return None
            
    # Funktsioon binaarpuu printimiseks, teeb seda inorder järjestusega
    def binaarpuu_printimine(self):
        if self.vasak_laps:
            # Esmalt väljastatakse vasak alampuu
            self.vasak_laps.binaarpuu_printimine()
        # Teiseks väljastatakse binaarpuu juur
        print(self.v22rtus, end=' ')
        # Kolmandaks väljastatakse parem alampuu
        if self.parem_laps:
            self.parem_laps.binaarpuu_printimine()

# Määran juure sõlme 
juur = BinaarpuuS6lm(12)

# Lisan binaarpuule väärtusi
juur.lisamine(6)
juur.lisamine(14)
juur.lisamine(3)

# Prindin binaarpuu
print("Binaarpuu:")
juur.binaarpuu_printimine()
print()

# Otsin otsitavat väärtust
otsitav_element = 12
leitud_s6lm = juur.otsimine(otsitav_element)
if leitud_s6lm:
    print("Otsitav sõlm väärtusega", otsitav_element, "on leitud!")
else:
    print("Sõlme väärtusega ", otsitav_element, "ei leitud!")