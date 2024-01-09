# Ülesanne: Rakenda Index Mapping algoritmi (triviaalne räsimine) kasutades massiive või järjendeid/liste.
# Algoritmi rakendamise inspo võetud loengust nr 7

# Loo massiiv, mille suurus on võrdne maksimaalse võimaliku võtme väärtusega
max_key_value = 3

# Algväärtusta kõik elemendid NULL-iks
indexed_massiiv = [None] * (max_key_value + 1)

# Võtme-väärtuse paari sisestamiseks aseta väärtus indeksisse,
# mis võrdub võtmega
def insert_value(key, value):
    indexed_massiiv[key] = value

# Lisan massiivi võtme-väärtuse paare
insert_value(1, "Apelsin")
insert_value(2, "Banaan")
insert_value(3, "Dattel")

# Väärtuse saamine indeksi kaudu ja väljastamine võtme järgi
print(indexed_massiiv[1])
print(indexed_massiiv[2])
print(indexed_massiiv[3])