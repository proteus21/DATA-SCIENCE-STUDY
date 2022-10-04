"""
    Stwórz dekorator, który wykona funkcję opakowywaną lub
    nie, w zależności od wartości zmiennej globalnej
    SHOULD_BE_RUN (wartość True uruchamia funkcję,
    wartośc False oznacza, że powinien się pojawić tylko napis
    „Pomijam…”.

    Przyklad, funkcja po opakowaniu wykona sie lub nie:
    SHOULD_BE_RUN = True
    @run_or_not
    def print_hello():
        print("hello")

    >> print_hello()
    hello

    SHOULD_BE_RUN = False
    @run_or_not
    def print_hello():
        print("hello")

    >>print_hello()
    Pomijam...

    Przetestuj swoje rozwiazanie.
"""

from typing import Callable

SHOULD_BE_RUN = False


def run_or_not(func: Callable) -> Callable:
    ...


@run_or_not
def add(a, b):
    return a+b

print(add(1, 2))