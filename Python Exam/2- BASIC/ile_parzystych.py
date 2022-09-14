"""
    Zadanie polega na napisaniu funkcji zliczajacej ilosc
    parzystych liczb w liscie liczb podanej jako parametr funkcji.
    Funkcja nazywa sie count_even_number, natomiast parametr wejsciowy
    jest lista liczb o nazwie numbers.
    Napisz rozwiazanie, ktore przebada liste w poszukiwaniu liczb parzystych
    i przy kazdym znalezieniu takowej zwiekszy licznik zmiennej pomocniczej.
    Funkcja powinna zwracac ilosc liczb parzystych w podanej liscie.
    Zakladamy, ze lista bedzie dostarczana z programu, nie przez uzytkownika
    z wykorzystaniem funkcji input().
    Przyklad:
    >> list_of_numbers = [1, 2, 3, 4, 5, 6] -> 3 liczby parzyste: 2, 4, 6
    >> x = count_even_numbers(list_of_numbers)
    x powinno wynosic 3.
    Uwaga: 0 jest liczba parzysta.
"""


def count_even_numbers(numbers):
    """Zlicza liczby parzyste w liscie podanej jako argument.

    :param numbers: lista liczb.
    :return: ilosc liczb parzystych w podanej liscie, typ wartosci
        zwracanej to int.

    """
    even_numbers=[]
    n=0
    for i in numbers:
        if i%2==0:
            even_numbers.append(i)
            n+=1
    return even_numbers, n



if __name__=="__main__":
  list_of_numbers = [1, 2, 3, 4, 5, 6]
  print("Show even numbers:",count_even_numbers(list_of_numbers)[0],"number of even numbers:", count_even_numbers(list_of_numbers)[1])

