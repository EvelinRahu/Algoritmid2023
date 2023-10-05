import time

algus_aeg_1 = time.time()

lifo_stack = [] #Loon tühja listi, mis esindab LIFO andmestruktuuri

#Lisan elemendid listi/stacki
#lifo_stack.append(1)
#lifo_stack.append(2)
#lifo_stack.append(3)
for i in range(1,10001):
    lifo_stack.append(i)

l6pp_aeg_1 = time.time()

#Mõõdan aja, mis kulus elementide lisamisel listi
kulunud_aeg_1 = l6pp_aeg_1 - algus_aeg_1

print("Elementide lisamisele kulunud aeg:", kulunud_aeg_1)

algus_aeg_2 = time.time()

#Eemaldan viimase elemendi, sest Last in - First out
while lifo_stack:
    viimane_element = lifo_stack.pop()

l6pp_aeg_2 = time.time()

#Mõõdan aja, mis kulus elementide eemaldamisel listist
kulunud_aeg_2 = l6pp_aeg_2 - algus_aeg_2

print("Elementide eemaldamisele kulunud aeg:", kulunud_aeg_2)






