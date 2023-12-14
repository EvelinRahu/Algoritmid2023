# Ülesanne: Kirjutage programm, mis teostab Binary Search'i sorteeritud täisarvude massiivil.

# Defineerin funktsiooni binary search
def binary_search(list, otsitav):

    # Initsialiseerin esialgse otsinguparameetri elemendid
    vasak_element = 0
    parem_element = len(list) - 1
    

    # Kahendotsingu algoritmi peamine osa, otsing toimub tingimusel:
    # vasakpoolseim element on parempoolseimast elemendist väiksem või sellega võrdne
    while vasak_element <= parem_element:

        # Arvutan keskmise elemendi indeksi
        keskmine_element = (vasak_element + parem_element) // 2

        # Kontrollin kas keskmine element on otsitav element
        if list[keskmine_element] == otsitav:
            # Kui on, siis väljastan otsitava elemendi asukoha indeksi ja tagastan väärtuse 
            print("Otsitav arv asub indeksil:", keskmine_element)
            return keskmine_element
        
        # Kui esimese IF-lause tingimus ei vasta tõele,
        # siis kontrollin kas keskmine element on otsitavast elemendist väiksem
        elif list[keskmine_element] < otsitav:
            # Kui on, siis annan vasakpoolseimale elemendile uue väärtuse
            # ja välistan otsitava elemendi leidmise vasakpoolsest listi osast
            vasak_element = keskmine_element + 1
        
        # Kui kaks eelmist IF-lauset ei vasta tingimustele ehk keskmine element on otsitavast suurem,
        # siis annan parempoolseimale elemendile uue väärtuse ja välistan otsitava elemendi leidmise parempoolsest listi osast
        else:
            parem_element = keskmine_element - 1
        
    # Väljastan teate, kui otsitavat elementi listist ei leitud ja tagastan väärtuse FALSE
    print("Otsitavat arvu ei leitud!")
    return False

# Määran loendi
list = [2, 5, 6, 1, 9]
# Sorteerin loendi
list.sort()
print("Sorteeritud list:", list)

# Defineerin otsitava elemendi 
otsitav = 6
print("Otsitav arv:", otsitav)

# Kutsun binary search funktsiooni esile
tulemus = binary_search(list, otsitav)