#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
zad. 2
Stwórz zmienną o nazwie `PI` i wartości 3.14. Wykorzystaj ją do obliczenia pola koła o promieniu 12.
Wynik wyświetl na ekran.
"""

"""
zad. 3
 * Stwórz dwie zmienne imie i nazwisko i przypisz do dowolne wartości (nie muszą
być prawdziwe).
 * wypisz obie zmienne na ekran.
 * Połącznie obie zmienne spacją i wynik zapisz do zmiennej dane.
"""

"""
zad. 4
Przekonwertuj wartość b na int, a następnie oblicz średnią z a, b i c.
"""
a = 314
b = "500"
c = 4.5

"""
zad. 6
Stwórz 3 elementową listę, która zawiera nazwy 3 Twoich ulubionych owoców.
Wynik przypisz do zmiennej `owoce`.
"""

"""
zad. 7
Dodaj do powyższej listy jako nowy element "pomidor".
"""

"""
zad. 8
Usuń z powyższej listy drugi element.
"""


"""
zad. 9
Rozszerz listę o tablice ['Jabłko', "Gruszka"].
"""

"""
zad. 10
Wyświetl listę owoce, ale bez pierwszego i ostatniego elementu.
"""

"""
zad. 11
Wyświetl co trzeci element z listy owoce.
"""

"""
zad. 7
Stwórz pusty słownik i przypisz go do zmiennej magazyn.
"""

"""
zad. 8
Dodaj do słownika magazyn owoce z listy owoce, tak, aby owoce były kluczami,
zaś wartościami były równe 5.
"""

"""
zad. 9
 * Stwórz listę składającą się z parzystych elementów listy l (l. parzystych)
 * Stwórz listę z elementów l o nieparzystych indeksach
"""
l = [4, 5, 8, 9, 0, 3]

"""
zad. 10
Lista `zad10` zawiera 2 elementy - listy. Stwórz nową listę `zad10_flat`,
która będzie składać się z elementów każdej z tych listy.
"""

zad10 = [[9, 8, 12, 7], [12, 33, 8, 7]]

"""
zad. 11
Stwórz listę zad11out, która powstanie z <zad11> poprzez usunięcie 
powtarzających się wartości.
"""

zad11 = [3, 2, 2, 6, 9, 10, 1, 3]

"""
zad. 12
Wyświetl sumę liczb od 1 do 256.
"""

"""
zad. 13
Wyświetl sumę liczb parzystych od 1 do 256.
"""

"""
zad. 14
Poniżej znajdują się 2 słowniki z danymi o liczbie przejazdów rowerami miejskimi w Montrealu w 2018 z podziałem na miesiące.
Pierwszy słownik zawiera informacje o przejazdach wykonanych przez posiadaczy abonamentu, a drugi przez ludzi, który
nie mają wykupionego abonamentu. Dane pochodzą ze strony https://montreal.bixi.com/en/open-data. 

a) Stwórz trzeci słownik `all_rides`, w którym zliczysz łączną liczbę przejazdów w każdym z miesięcy.
b) Wykorzystując listę `months` wyświetl ile w danym miesiącu odbyło się przejazdów. Załóż, że odbyło się 0 przejazdów 
w miesiącach, którycj brakuje w `all_rides`.
c) Oblicz jaki procent stanowią w ciągu roku przejazdy okazjonalne.
d) Czy obie grupy osiągają największą liczbę przejazdów w tym samym miesiącu? Spróbuj znaleźć odpowiedź bez patrzenia
na wartości w podanych słownikach.
"""

members = {'April': 211819, 'May': 682758, 'June': 737011, 'July': 779511, 'August': 673790,
           'September': 673790, 'October': 444177, 'November': 136791}

occasionals = {'April': 32058, 'May': 147898, 'June': 171494, 'July': 194316, 'August': 206809,
               'September': 140492, 'October': 53596, 'November': 10516}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

"""
zad. 15
 * Stwórz listę składającą się z dowolnych 100 elementów, np. może być
 to listę kwadratów liczb.
 * Sprawdź za pomocą funkcji len liczbę elementów tej listy.
 * Usuń trzeci, element.
 * Usuń przedostatni element.
 * Wyświetl pierwsze 10 elementów.
"""

"""
zad. 16
Znajdz najmniejsz element w poniższej liście.
"""
numbers = [0, 6, 9, -10, -5, 9, 8, -6]

"""
zad. 17
Wyświetl poniższy słownik, tak, aby każda para "klucz: wartość"
była w osobnej linii.
"""
s = {'Tomasz': [3, 4, 5, 4], 'Agata': [5, 5, 5, 4]}


"""
zad. 18
Poniżej jest podana lista liczby. Stwórz słownik <counter>, którego kluczami
będą wartości występujące w liście <liczby>, a wartościami ile dany element
wystąpił w liście <liczby>.
"""
liczby = [3, 4, 3, 3, 4, 7, 9]

"""
zad. 19
Poniższy słownik oceny dwóch osób. Stwórz nowy słownik z takimi samymi kluczami,
ale wartościami tego słownika będą średnie oceń.
"""
s = {'Tomasz': [3, 4, 5, 4], 'Agata': [5, 5, 5, 4]}


"""
zad. 20
Dla podanego poniże słownika S, stwórz nowy słownik, którego kluczami będą
wartości słownika S, a wartościami: odpowiadające im klucze z S.
"""
s = {'Klucz1': 'Wartosc1', 'Klucz2': 'Wartosc2', 'Klucz3': 'Wartosc3'}

"""
zad. 21
Napisz kod, który wypisze na ekran elementy, które występnują w obu poniżej
podanych funkcjach.
"""
l1 = [99, 8, 7, 55]
l2 = [55, 111, 11, 99, 8]

"""
zad. 22
Napisz kod, który znajdzie najdroższy produkt  w poniższym słowniku.
"""
zakupy = {'telefon': 1000, 'ładowarka': 35, 'chleb': 4.30, 'kawa': 55, 'gramofon': 240}

"""
zad. 23
Stwórz listę składającą się z wartości słownika zakupy.
"""
zakupy = {'telefon': 1000, 'ładowarka': 35, 'chleb': 4.30, 'kawa': 55, 'gramofon': 240}

"""
zad. 24
Wyświetl na ekranie poniższy wzór:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

"""
1. Napisz funckję, która zamieni stopnie Fahrenheita na Celcjusza zgodnie ze
wzorem:
    F = 32 + 9/5*C

Następnie dodaj kowałek kodu, który pozwoli na wczytanie temperatury z
klawiatury, a następnie wyświetli temperaturę w Fahrenheitach.

"""

"""
2. Poniższa słownik Letters zawiera informacje o literach w grze Scrubble,
dokładniej ile tabliczek z daną literą występuje w grze oraz wartość punktową
danej litery.

Napisz program, który wczyta z klawiatury słowo, a nastęnie zwróci ile dane
słowo jest warte punktów.

"""

Letters = {
        'a': { 'quantity' : 9, 'value': 1},
        'b': { 'quantity' : 2, 'value': 3},
        'c': { 'quantity' : 2, 'value': 3},
        'd': { 'quantity' : 4, 'value': 2},
        'e': { 'quantity' : 12, 'value': 1},
        'f': { 'quantity' : 2, 'value': 4},
        'g': { 'quantity' : 3, 'value': 2},
        'h': { 'quantity' : 2, 'value': 4},
        'i': { 'quantity' : 9, 'value': 1},
        'j': { 'quantity' : 1, 'value': 8},
        'k': { 'quantity' : 1, 'value': 5},
        'l': { 'quantity' : 4, 'value': 1},
        'm': { 'quantity' : 2, 'value': 3},
        'n': { 'quantity' : 6, 'value': 1},
        'o': { 'quantity' : 8, 'value': 1},
        'p': { 'quantity' : 2, 'value': 3},
        'q': { 'quantity' : 1, 'value': 10},
        'r': { 'quantity' : 6, 'value': 1},
        's': { 'quantity' : 4, 'value': 1},
        't': { 'quantity' : 6, 'value': 1},
        'u': { 'quantity' : 4, 'value': 1},
        'v': { 'quantity' : 2, 'value': 4},
        'w': { 'quantity' : 2, 'value': 4},
        'x': { 'quantity' : 1, 'value': 8},
        'y': { 'quantity' : 2, 'value': 4},
        'z': { 'quantity' : 1, 'value': 10},
        '*': { 'quantity' : 2, 'value': 0}
        }

"""
3. Oblicz ile wynosi suma wszystkich punktów na wszystkich kostkach w grze
Scrubble.
"""


"""
4. Korzystając z funkcji `permutations` z biblioteki `itertools` wypisz wszystkie
możliwe "słowa", które można ułożyć z liter z tablicy tiles.
"""

tiles = ['c','o','n','t','a','i','n']


"""
5. Napisz program, który wskaże, czy który gracz wygrał (Albo jest remis) w
poniższych grach "kołko i krzyżyk". Spacja oznacza wolne pole, które jeszcze
nie zostało zajęte.
"""

board_1 = [['x', 'x', ' '],
           ['x', 'o', ' '],
           ['x', 'o', 'o']]

board_2 = [['o', 'x', ' '],
           ['x', 'o', ' '],
           ['x', 'o', 'o']]

board_3 = [[' ', 'o', ' '],
           ['x', 'o', ' '],
           ['x', 'o', 'o']]

board_4 = [['o', 'x', ' '],
           ['x', 'o', ' '],
           ['x', 'o', 'x']]

board_5 = [['o', 'x', ' '],
           ['x', 'o', ' '],
           ['x', 'o', ' ']]
