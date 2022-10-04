"""
    Stworz dekorator o nazwie twice, ktory wywola dwukrotnie funkcje opakowujaca.
    Przyklad, funkcja po opakowaniu wykona sie dwa razy:
    @twice
    def print_hello():
        print("hello")

    >> print_hello()
    hello
    hello

    @twice
    def print_bye():
        print("bye")

    >>print_bye()
    bye
    bye

    Przetestuj swoje rozwiazanie.
"""

from typing import Callable


def twice(function: Callable) -> Callable:  # typ obiektu, na ktorym mozemy uzyc operatora wywolania, czyli nawiasow ()
    pass


@twice
def print_hello():
    print("hello")


@twice
def print_bye():
    print("bye")
