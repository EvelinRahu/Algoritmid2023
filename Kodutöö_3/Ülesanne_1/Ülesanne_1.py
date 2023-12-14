# Ülesanne: Rakendage Linear Search algoritm vabalt valitud programmeerimiskeeles.

# Defineerin funktsiooni linear search 
def linear_search(list, otsitav):
    
    #For loop, mis läbib loendit, kuni leiab otsitava elemendi
    for i in range(0, len(list)):
        # Kontrollin IF-lausega, käin läbi kõik elemendid kuni otsitav element on leitud
        if list[i] == otsitav:
            # Kui otsitav element on loendist leitud, prindin välja selle väärtuse ja asukoha indeksi ning tagastan väärtuse TRUE
            print("Otsitav arv (", otsitav, ") asub indeksil:", i)
            return True
    # Kui otsitavat elementi loendist ei leitud, prindin teate ja tagastan väärtuse FALSE
    print("Otsitavat arvu ei leitud!")
    return False
        
# Määran loendi, mida läbitakse funktsioonis
list = [4, 5, 2, 10, 8]

# Määran otsitava elemendi muutuja ja annan sellele väärtuse 
otsitav = 8

# Kutsun funktsiooni linear search esile
tulemus = linear_search(list, otsitav)

