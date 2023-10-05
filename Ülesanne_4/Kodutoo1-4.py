def binaarne_otsing(sorteeritud_list, n):
    esimene_indeks = 0
    viimane_indeks = len(sorteeritud_list) - 1

    while esimene_indeks <= viimane_indeks:
        keskmine_indeks = (esimene_indeks + viimane_indeks) // 2

        if sorteeritud_list[keskmine_indeks] == n:
            return keskmine_indeks
        
        elif sorteeritud_list[keskmine_indeks] < n:
            esimene_indeks = keskmine_indeks + 1

        else:
            viimane_indeks = keskmine_indeks - 1
    return -1
    
list = [3,4,2,6,8,9]
sorteeritud_list = sorted(list)
print(sorteeritud_list)

n = 6

vastus = binaarne_otsing(sorteeritud_list, n)

if vastus != -1:
    print("Täisarvu indeks on:", sorteeritud_list.index(n))
else:
    print("Täisarvu", n, "ei ole loendis!")

