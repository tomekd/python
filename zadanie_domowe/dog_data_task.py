
import csv
from pathlib import Path

with open(Path(__file__).parent / './dogs-data.csv', encoding='utf-8') as data_file:
    dog_data = csv.DictReader(data_file)
    dog_data = list(dog_data)

print(dog_data[0])



"""
Zadanie 1

Do listy dog_data zostały wczytane dane o psach i ich właścicielach. Każdy element listy to słownik,
który ma 4 klucze 'OwnerAge', 'Gender', 'Breed', 'DogAge' oznaczające kolejno wiek właściciela (przedział wiekowy), 
płeć psa, rasę psa i wiek psa. 
Przykładowy element listy:
{'OwnerAge': 60, 'Gender': 'M', 'Breed': 'Welsh Terrier', 'DogAge': 3}

a) zapisz do zmiennej listę breeds listę wszystich ras psów zawartych w dog_data. Elementy
    listy powinny być unikatowe i posortowane afalbetycznie (A-Z).

b) Znajdź najpopularniejszą rasę psa dla każdego przedziały wiekowego (klucz `OwnerAge`) i 
    zapisz wynik jako słownik the_most_popular_breed, którego kluczami będą przedziały wiekowe,
    a wartością najpopularniejsza rasa psa (dla danego przedziału).
    
c) Biblioteka statistics (https://docs.python.org/3/library/statistics.html#) pozwala na
    obliczenie podstawowych funkcji statystycznych. Wykorzystaj odpowiednie funkcje i oblicz
    średnią, modę (mode) i wariancję wieku psów.

d)  Zapisz do plik `terriers.txt` nazwy wszystkich Terrierów wraz z ich liczebnością, które znajdują się w dog_data.
    Dane zapisz w formacie CSV. Wykorzystaj bibliotekę `csv` (https://docs.python.org/3.8/library/csv.html).

"""

