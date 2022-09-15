"""
    Napisz funkcje, ktorej zadaniem jest podwojenie kazdego znaku
    w napisie podanym jako parametr wejsciowy.
    Dla przykladu, wartoscia zwrocona z funkcji produce_double_sings
    przy argumencie "Python", powinno byc slowo "PPyytthhoonn".
    Kazda litera powinna byc podwojona zachowujac swoja wielkosc.
    Rozpatrujemy tylko napisy jednoslowowe.
"""


def produce_double_signs(string):
    """Tworzy nowy napis na podstawie podanego, podwajajac kazdy znak.

    :param string: napis, w ktorym znaki powinny byc podwojone
    :return: nowy napis z podwojonymi znakami.

    """
    s=[]
    for n in string:
        s.append(2*n)
    return (''.join(s))

def produce_double_signs1(string):
    """Tworzy nowy napis na podstawie podanego, podwajajac kazdy znak.

    :param string: napis, w ktorym znaki powinny byc podwojone
    :return: nowy napis z podwojonymi znakami.

    """
    s=[]
    for n in string:
        s.append(2*n)
    return "".join(2*n for n in string)
def produce_double_signs2(string):
    sign=""
    for n in string:
        sign+=n
        sign+=n
    return sign


if __name__=="__main__":
 print(produce_double_signs("Aneta"))
 print(produce_double_signs1("Aneta"))
 print(produce_double_signs2("Aneta"))