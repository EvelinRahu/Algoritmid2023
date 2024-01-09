# Ülesanne: Rakenda separate chaningut kasutades linked-liste.
# Kasutatud allikas: https://gist.github.com/tsungjenh/5b058659db48528d56725ea3b5f57b9a ja ChatGPD

# Node klassi konstruktor, mis loob uue sõlme
class Node:
    def __init__(self, v6ti, v22rtus):
        self.v6ti = v6ti
        self.v22rtus = v22rtus
        self.j2rgmine_v6ti = None


class SeparateChainingHashTable:
    # Initsialiseerib hajutustabeli suuruse ja loob tühjad ahelad
    def __init__(self, suurus):
        self.suurus = suurus
        self.tabel = [None] * suurus

    # Räsifunktsioon, võtab võtme ning tagastab indeksi 
    def hash_function(self, v6ti):
        return v6ti % self.suurus

    # Funktsioon, mis lisab võtme ja väärtuse tabelisse
    def insert(self, v6ti, v22rtus):
        index = self.hash_function(v6ti)

        new_node = Node(v6ti, v22rtus)
        
        # Kui ahel on tühi, lisab uue sõlme otse
        if self.tabel[index] is None:
            self.tabel[index] = new_node

        # Kui ahel on juba olemas, lisab uue sõlme ahela lõppu
        else:
            praegune_v6ti = self.tabel[index]
            while praegune_v6ti.j2rgmine_v6ti:
                praegune_v6ti = praegune_v6ti.j2rgmine_v6ti
            praegune_v6ti.j2rgmine_v6ti = new_node

    # Funktsioon, mis otsib väärtust vastavalt võtmele
    def search(self, v6ti):
        index = self.hash_function(v6ti)
        praegune_v6ti = self.tabel[index]

        # Otsib elementi linked-listist
        while praegune_v6ti:
            if praegune_v6ti.v6ti == v6ti:
                return praegune_v6ti.v22rtus
            praegune_v6ti = praegune_v6ti.j2rgmine_v6ti

        return None

# Näide kasutamisest
hash_table = SeparateChainingHashTable(10)

hash_table.insert(5, "Apple")
hash_table.insert(15, "Banana")
hash_table.insert(25, "Cherry")

print(hash_table.search(5))  # Väljastab: Apple
print(hash_table.search(15)) # Väljastab: Banana
print(hash_table.search(25)) # Väljastab: Cherry
print(hash_table.search(10)) # Väljastab: None (elementi ei leitud)
