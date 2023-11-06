""" Ülesande kirjeldus:
Antud on osaliselt sorteeritud loend: [12, 11, 13, 5, 6, 7]. 
Rakenda Insertion Sort algoritmi """

def insertion_sort(arr):
    # Muutuja andmine massiivi pikkusele
    n = len(arr) 

    # Alustan loendi sorteerimist elemendist indeksil 1, element indeksil 0 on automaatselt "sorteeritud"
    for i in range(1, n):

        # Muutuva väärtusega praegune element, mida hakkan liigutama õigesse kohta
        current_element = arr[i] 

        # Elemendi indeks, mis asub "praegusest elemendist" vasakul ja millega hakkan võrdlema
        j = i - 1 
       
        # Liigutan elemente vasakule, tingimusel et "praegune element" on väiksem kui võrreldav element, 
        # kuni leitakse sobiv koht ja antakse uus väärtus "praegusele elemendile" ühe koha võrra paremal 
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = current_element

loend = [12, 11 , 13, 5, 6, 7]

# Kutsun funktsiooni esile
insertion_sort(loend)
print("Sorteeritud loend:", loend)