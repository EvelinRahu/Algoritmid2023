"""Ülesande kirjeldus:
Antud on järgnevate arvude loend: [64, 34, 25, 12, 22, 11, 90]. 
Simuleeri samm-sammult Bubble Sort algoritmi. 
Iga läbimise järel kirjuta üles tulemuseks olev loend"""

def bubble_sort(arr):
    # Muutuja andmine massiivi pikkusele
    n = len(arr)

    # Esimene tsükkel käib läbi loendi elemendid kuni eelviimaseni, sest see on sorteeritud 
    # pärast esimest iteratsiooni
    for i in range(n):

        # Teine tsükkel käib läbi loendi elemendid nullist kuni viimase sortimata elemendini
        for j in range(0, n-i-1):
            
            # Võrdlen kõrvuti olevaid elemente kuni kogu loend on sorteeritud
            # Kui vasakpoolne element on suurem kui parempoolne, vahetatakse kohad
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)

loend = [64, 34, 25, 12, 22, 11, 90]

# Kutsun funktsiooni esile
bubble_sort(loend)