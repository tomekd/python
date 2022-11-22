import csv
from pathlib import Path
import re
import pandas as pd
import statistics as st

with open(Path(__file__).parent / './dogs-data.csv', encoding='utf-8') as data_file:
    dog_data = csv.DictReader(data_file)
    dog_data = list(dog_data)

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

# a
breeds = sorted(set(map(lambda entry: re.sub(r'[^A-Za-z ]+', '', entry['Breed']), dog_data)))

# b
df = pd.DataFrame(dog_data)
the_most_popular_breed = df.groupby('OwnerAge')['Breed'].apply(list).to_dict()

for k, v in the_most_popular_breed.items():
    the_most_popular_breed[k] = st.mode(v)

# c
dogs_ages = list(map(lambda entry: int(entry['DogAge']), dog_data))

mode = st.mode(dogs_ages)
mean = st.mean(dogs_ages)
var = st.variance(dogs_ages)

# d
terriers = df.groupby('Breed')['DogAge'].count().to_dict()
terriers = dict(filter(lambda entry: 'terrier' in entry[0].lower(), terriers.items()))

with open(Path(__file__).parent / './terriers.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(terriers.items())
