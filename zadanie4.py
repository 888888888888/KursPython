__author__ = 'Crejzer'

"""Zadanie 4"""

#tablica wypelniona wartosciami z danych zadania
A = (-5,-3,-1,0,3,6)

def absDistinct ( A ):
    #warunek zadania liczba musi byc z zakresu od 1 do 1000000
    if len(A)>100000 or len(A)<1:
        raise ValueError("Array length not in range [1..100,000]")
    #wykonywanie funkcji abs(kotra zwraca wartosci bezwzgledne) dla wszystkich elementow
    A=[abs(x) for x in A]
    #niwelowanie powtorzen
    A=set(A)
    #zwracanie dlugosci tablicy (czyli liczby elementow)
    return len(A)

#sprawdzenie poprawnosci dzialania funkcji abdDistinct
print("Zadanie 4");
print(absDistinct(A));