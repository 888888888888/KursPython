__author__ = 'Crejzer'

from itertools import izip, chain

list1 = ['orange', 'apple', 'banana']
list2 = ('carrot', 'potato', 'lettuce')
list3 = {'milk', 'sugar', 'butter', 'flour'}

"""Zadanie 3a"""
listCala = []

#tworzenie tablicy zlozonej z wszystkich wartosci poprzednich tablic
listCala = [x for x in chain(list1,list2,list3)]

#sprawdzanie czy ma te same znaki
def sprawdzanie(x):
    index = 0
    lista = []

    for all in x:
        lista.append(all)
    for i in range(len(lista)):
        if(lista[index]==lista[index-1]):
            print x
            index +=1
        else:
            index += 1

print("Zadanie 3a")
#wyswietlanie wyniku
for i in listCala:
    sprawdzanie(i)

"""Zadanie 3b"""
#tablica dlugosci elementow
listLen = []

#wpisywanie dlugosci do tablicy
for i in listCala:
    listLen.append(len(i))

print("Zadanie 3b")
#wyswietlanie wyniku i odpowiednie sortowanie tablic
Wynik = zip(sorted(listLen),sorted(listCala, None, lambda listCala: len(listCala)))
print(Wynik)

