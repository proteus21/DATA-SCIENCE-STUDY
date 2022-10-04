"""
    Na podstawie klasy abstrakcyjnej Wielokat, stworz 3 klasy dziedziczace: Kwadrat, Prostokat, Trojkat.
    Kazda z tych klas musi byc konkretna (a nie abstrakcyjna), powinna wiec nadpisywac wszystkie metody
    abstrakcyjne z klasy Wielokat. Kazda konkretna klasa powinna miec definicje konstruktora __init__
    (dla przykładu obiekt typu Kwadrat, powinien miec jeden atrybut self.bok, obiekt prostokat dwa atrybuty:
    self.bok1, self.bok2, a trojkat self.bok, self.wysokosc).
    Na koniec stworz funkcje zarzadzajaca obiektami stworzonych klas, ktora w petli bedzie obliczala pola
    dla kazdego obiektu.
"""

from abc import ABC, abstractmethod
from typing import Union


class Wielokat(ABC):

    @abstractmethod
    def oblicz_pole(self) -> Union[int, float]:  # Union sugeruje ze funkcja moze zwrocic inta albo floata
        """Metoda ma za zadanie obliczyc pole danego obiektu.

        Ze wzgledu na fakt, iz nie wiemy w tym momencie jaki to jest wielokat,
        nie potrafimy obliczyc jego pola. Do redefinicji w klasie dziedziczacej.

        :return: wartosc pola jako liczba calkowita lub wymierna.
        """
        ...


class Kwadrat(Wielokat):
    pass


class Prostokat(Wielokat):
    pass


class Trojkat(Wielokat):
    pass


def licz_pola(wielokaty: list) -> list:
    """Oblicza pola wszystkich wielokatow podanych w liscie.

    :param wielokaty: lista obiektow dziedziczacych po Wielokat.
    :return: lista obliczonych pol.

    """
    pass
