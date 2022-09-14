"""
    Napisz funkcje, ktora na podstawie podanego slownika
    z zakupami jako kluczami oraz z krotka (tuple) z cena i podatkiem,
    wyliczy kwote brutto calych zakupow.
    Parametr grocery_list moze miec postac:
    {"mleko": (5.00, 10), "ser": (4.50, 15), "jogurt": (3, 25)}.
    Pierwsza wartosc w krotce to cena netto, druga to podatek (np. dla 10%
    podatku danego produktu i jego ceny brutto 10 pln, cena brutto bedzie
    wynosila 1.1*10). Nalezy zsumowac ceny brutto dla kazdego produktu
    i zwrocic wynik.
    Nalezy przyjac, ze uzytkownik nie poda blednych wartosci (czyli, ze
    cena nigdy nie bedzie ujemna, a podatek zawsze bedzie sie miescil
    w zbiorze <0; 100>.
"""
import math
import os

def calculate_brutto_prize(grocery_list):
    VAT=1
    suma=0
    for key, value in grocery_list.items():
        #print(grocery_list[key][1], grocery_list[key][0])
        suma=suma+((grocery_list[key][1]*int(VAT)/100*grocery_list[key][0])+grocery_list[key][0])
    return suma

def calculate_brutto_prize_1(grocery_list):
    price=0
    for value in grocery_list.values():
        price+=(float(value[1]*0.01*value[0])+value[0])
    return price

def calculate_brutto_prize_2(grocery_list):
    prize = 0
    for product in grocery_list:
        prize += grocery_list[product][0] + (grocery_list[product][0] * grocery_list[product][1] * 0.01)
    return prize

def calculate_brutto_prize_3(grocery_list):
    return sum(price+price *tax *0.01 for price, tax in grocery_list.values())

if __name__=="__main__":
    grocery_list={"mleko": (5.00, 10), "ser": (4.50, 15), "jogurt": (3, 25)}
    gross_sum=calculate_brutto_prize(grocery_list)
    print("Total gross price is:",gross_sum)
    gross_sum_1 = calculate_brutto_prize_1(grocery_list)
    print("Total gross price is:", gross_sum_1)
    gross_sum_2 = calculate_brutto_prize_2(grocery_list)
    print("Total gross price is:", gross_sum_2)
    gross_sum_3 = calculate_brutto_prize_3(grocery_list)
    print("Total gross price is:", gross_sum_3)