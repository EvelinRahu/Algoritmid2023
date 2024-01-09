# Ülesanne: Rakenda topelt räsimise algoritm.
# Kasutatud allikad: https://onecompiler.com/python/3wq9h743a, https://www.geeksforgeeks.org/double-hashing/ ja ChatGPD

class DoubleHashTable:
    # Konstruktor, loob räsitabeli määratud suurusega
    def __init__(self, suurus):
        self.suurus = suurus
        self.tabel = [None] * suurus

    # Esimene räsifunktsioon, määrab esialgsetele võtmetele indeksid
    def r2si_funktsioon1(self, v6ti):
        return hash(v6ti) % self.suurus
        
    
    # Teine räsifunktsioon, mis arvutab kokkupõrke korral indeksile uue aadressi
    def r2si_funktsioon2(self, v6ti):
        return (2 * hash(v6ti) + 1) % (self.suurus - 1)

    #  Funktsioon, mis lisab Võtme ja väärtuse räsitabelisse
    def insert(self, v6ti, v22rtus):
        v6tme_indeks = self.r2si_funktsioon1(v6ti)
        
        
        # Kui esimene indeks on vaba, sisesta otse sinna
        if self.tabel[v6tme_indeks] is None:
            self.tabel[v6tme_indeks] = (v6ti, v22rtus)
            #print(self.tabel[v6tme_indeks])
        else:
            # Kui esimene indeks on juba hõivatud, kasuta teist räsifunktsiooni
            i = 1
            while True:
                uus_v6tme_indeks = (v6tme_indeks + i * self.r2si_funktsioon2(v6ti)) % self.suurus
                 # Leiti vaba indeks, sisesta andmed
                if self.tabel[uus_v6tme_indeks] is None:
                    self.tabel[uus_v6tme_indeks] = (v6ti, v22rtus)
                    #print(self.tabel[uus_v6tme_indeks])
                    break
                i += 1
    
    # Funktsioon, mis otsib väärtust vastavalt võtmele
    def search(self, v6ti):
        v6tme_indeks = self.r2si_funktsioon1(v6ti)
        i = 0
        while self.tabel[(v6tme_indeks + i * self.r2si_funktsioon2(v6ti)) % self.suurus][0] != v6ti:
            i += 1
        return self.tabel[(v6tme_indeks + i * self.r2si_funktsioon2(v6ti)) % self.suurus][1]

# Näide kasutamisest
r2si_tabel = DoubleHashTable(10)
r2si_tabel.insert("a", 1)
r2si_tabel.insert("b", 2)
r2si_tabel.insert("c", 3)

print(r2si_tabel.search("a"))  
print(r2si_tabel.search("b"))   
print(r2si_tabel.search("c"))   


