"""
    Napisz funkcje sprawdzajaca czy napis podany jako argument do niej
    jest palindromem. Palindrom to napis, ktory czytany od lewej
    do prawej brzmi tak samo jak czytany od prawej do lewej, np kajak.
    Dla ulatwienia zaloz, ze napis bedzie zawsze jednym slowem.
    Zakladamy, ze pusty string jest palindromem.
"""


def check_if_palindrome(string):
    """Sprawdza czy podany string (jedno slowo) jest palindromem.

    :param string: napis do sprawdzenia.
    :return: True jezeli napis jest palindromem,
         False w przeciwnym wypadku.


    """
    if string==string[::-1]:
        return "True"
    else:
        return "False"

if __name__=="__main__":
    print(check_if_palindrome("kajak"))
    print(check_if_palindrome("kaodak"))

