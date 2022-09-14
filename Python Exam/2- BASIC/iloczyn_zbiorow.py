"""
    Napisz funkcje przyjmujaca dwa zbiory (sety) jako parametry
    i znajdujaca liczby, ktore znajduja sie zarowno w jednym zbiorze,
    jak i w drugim.
    Funkcja powinna zwrocic set powtarzajacych sie liczb. Jezeli zadna
    liczba sie nie powtarza, funkcja powinna zwrocic pusty zbior.
    Uwaga: w Pythonie pusty set (zbior) deklaruje sie tak:
    >> pusty = set()
    a nie tak:
    >> pusty = {} # w taki sposob deklaruje sie slownik.
    Zadanie powinno zostac wykonane w inny sposob niz za pomoca
    uzycia skladni:
    >> set1 & set2
    ktore w skrocie ustala czesc wspolna obu zbiorow.
"""
def find_common_numbers_1(set1, set2):
    common_numbers =set()
    for number1 in set1:
        for number2 in set2:
            if number1==number2:
                common_numbers.add(number1)
    return common_numbers


def find_common_numbers(set1, set2):
        return set(set1).intersection(set(set2))

def find_common_numbers_2(set1,set2):
    common_numbers = set()
    for number1 in set1:
        if  number1 in set2:
            common_numbers.add(number1)
    return common_numbers

if __name__=="__main__":
 print("\nIntersection using '&' operator")
 print(find_common_numbers((1,2,3,4),(2,3,5,6)))
 print("\nIntersection using '&' operator")
 print(find_common_numbers_1((1,2,3,4),(2,3,5,6)))
 print("\nIntersection using '&' operator")
 print(find_common_numbers_2((1,2,3,4),(2,3,5,6)))