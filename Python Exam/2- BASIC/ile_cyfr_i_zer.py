"""
    Napisz dwie niezalezne funkcje rozwiazujace nastepujace problemy:
    a) count_digits powinno zliczac ilosc cyfr w liczbie calkowitej,
       ktora zostanie podana jako argument,
    b) count_zeros powinno zliczac ilosc zer w liczbie calkowitej, ktora zostanie
       podana jako argument.
    Przyklady:
    >> x = count_digits(1234)
    >> print(x)
    4
    >> x = count_zeros(1000)
    >> print(x)
    3
    Zadania mozna rozwiazac w sposob "matematyczny", ale rowniez
    wykorzystujac uproszczenia Pythona.
    Podpowiedz: a gdyby tak liczbe rzutowac na napis?
"""

def count_digits1(num):
    num
    count = 0

    while num != 0:
        num //= 10
        count += 1

    return str(count)

def count_digits(number):
    """Zlicza ilosc cyfr w liczbie.

    :param number: pewna liczba calkowita
    :return: ilosc cyfr w liczbie (int).

    """
    return len(str(number))


def count_zeros(number):
    """Zlicza zera w liczbie number.

    :param number: pewna liczba calkowita
    :return:
    """
    return str(number).count("0")


def digits(n):
    count = 0
    if n == 0:
        return 1

    if n < 0:
        n *= -1

    while (n >= 10 ** count):
        count += 1
        n += n % 10

    return count

if __name__=="__main__":
    print(count_digits1(123456))
    print(count_digits(123456))
    print(count_zeros(1000))
    print(digits(123456))
