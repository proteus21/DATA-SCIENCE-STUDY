"""
    Napisz funkcje stwierdzajaca czy podana jako argument liczba
    jest liczba pierwsza czy nie. Liczba jest pierwsza, kiedy dzieli sie
    tylko przez siebie i przez 1. Jednym z algorytmow wyszukiwania liczb
    pierwszych jest sprawdzenie czy zadna z liczb od 2 do LICZBA-1
    (lub od 2 do pierwiastek z LICZBA) nie dzieli badanej liczby bez reszty.
    Uwaga: 0 i 1 nie sa zaliczane ani do liczb pierwszych, ani do zlozonych.
"""


def is_prime_number(n):
    """Sprawdza czy argument number jest liczba pierwsza.

    :param number: liczba typu int.
    :return: True jezeli liczba jest pierwsza,
             False jezeli jest zlozona.

    """
    prime_factors = []
    while (n % 2 == 0):
        n = n / 2
        prime_factors.append(2)
    for i in range(3, int(n ** 0.5 + 1), 2):
        while (n % i == 0):
            n = n / i
            prime_factors.append(i)
    if n > 2:
        prime_factors.append(int(n))
    if n in prime_factors:
        return True
    else:
        return False
if __name__=="__main__":
    number=int(input("Give the number:"))
    print(is_prime_number(number))


