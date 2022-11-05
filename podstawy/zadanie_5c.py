
"""
Poniżej znajdują się 2 słowniki z danymi o liczbie przejazdów rowerami miejskimi w Montrealu w 2018 z podziałem na miesiące (od kwietnia do listopada).
Pierwszy słownik zawiera informacje o przejazdach wykonanych przez posiadaczy abonamentu, a drugi przez ludzi, którzy
nie mają wykupionego abonamentu. Dane pochodzą ze strony https://montreal.bixi.com/en/open-data. 

a) Stwórz trzeci słownik `all_rides`, w którym zliczysz łączną liczbę przejazdów w każdym z podanych miesięcy.
b) Oblicz sumę zarejestrowanych przejazdów od kwietnia do listopada.
c) Wyswietl jaki procent wszystkich przejazdów odbyło się w sierpniu (August).

"""

members = {
    'April': 211819,
    'May': 682758,
    'June': 737011,
    'July': 779511,
    'August': 673790,
    'September': 673790,
    'October': 444177,
    'November': 136791,
}

occasionals = {
    'April': 32058,
    'May': 147898,
    'June': 171494,
    'July': 194316,
    'August': 206809,
    'September': 140492,
    'October': 53596,
    'November': 10516,
}
