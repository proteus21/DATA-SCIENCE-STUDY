"""
    Stworz klase Ulamek reprezentujaca liczby ulamkowe.
    Kazdy obiekt typu Ulamek powinien miec dwa atrybuty: self.licznik oraz self.mianownik.
    Glownym celem zadania jest dorobienie imlementacji, dzieki ktorej mozliwe stanie sie
    dodawanie, mnozenie, dzielenie i odejmowanie od siebie dwoch obiektow typu Ulamek. W tym celu nalezy
    przeladowac operatory +, -, *, / (magiczne metody: __add__, __sub__, __mul__, __truediv__).
    Pamietac trzeba o tym, ze przed dodaniem ulamkow, nalezy je sprowadzic do wspolnego mianowanika!
    Dla uproszczenia: nie trzeba skracac ulamkow, czyli ulamka 10/20 nie trzeba bedzie sprowadzac do postaci 1/2.
    Takie dzialania powinny sie zakonczyc sukcesem:
    >> half = Ulamek(1, 2)
    >> print(half.licznik)
    1
    >> print(half.mianownik)
    2
    >> quarter = Ulamek(1, 4)
    >> print(quarter.licznik)
    1
    >> print(quarter.mianownik)
    4
    >> result = half + quarter  # 1/2 + 1/4
    >> print(result.licznik)
    6
    >> print(result.mianownik)
    8
    Zauwaz, ze nie chcemy w tym przypadku skracac ulamka do postaci 3/4. Algorytm zamienia 1/2 na 4/8 a 1/4 na 2/8
    (po prostu wymnaza liczby przez siebie).
"""


class Ulamek:
    pass
