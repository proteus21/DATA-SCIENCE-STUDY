"""
    Stworz prosty symulator gry karcianej wojna.
    Zadaniem Twojej funkcji jest wskazanie, ktora karta
    zwyciezy. Parametrami sa znaki card1 oraz card2.
    Moga one przyjmowac wartosci:
    <"1", "2", "3", ..., "10", "J", "D", "K", "A"> - wielkosc
    liter bedzie miala znaczenie (choc mozna przedstawic rozwiazanie,
    w ktorym nie bedzie znaczylo czy litera jest duza czy mala).
    Funkcja powinna zwracac liczbe 1, jezeli wygra gracz 1,
    2 - jezeli zwyciezy gracz 2 lub 0 jesli karty sa takie same.
    Przyklady:
    >> determine_the_winner("5", "2")
    1
    >> determine_the_winner("D", "A")
    2
    >> determine_the_winner("K", "8")
    1
    >> determine_the_winner("4", "4")
    0
"""
import random

def determine_the_winner(card1, card2):
    """Wskazuje zwyciezce potyczki w grze wojna.

    :param card1: litera (string) reprezentujaca karte gracza 1.
    :param card2: litera (string) reprezentujaca karte gracza 2.
    :return: 0 dla remisu, 1 jesli zwyciezy gracz 1, 2 dla zwyciestwa gracza 2.

    """
    results1=0
    results2=0
    if  card1[0]>card2[0]:
             results1=1
             print("Win person 1")
    elif card1 [0]<card2[0]:
             results2=1
             print("Win person 2")
    else:
       print("Draw")

    return results1, results2

if __name__=="__main__":
    i=0
    results1_sum=0
    results2_sum=0
    card_points = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J','D','K','A']
    # creating enumerate objects
    card_value=list(enumerate(card_points))
    print(card_value)
    print("Amount of shuffle: ")
    amount_shuffle=int(input())
    while i < amount_shuffle:
      card1= random.choice(card_value)
      card2 = random.choice(card_value)
      print("Show cards")
      print(card1[1],card2[1])
      results1, results2=determine_the_winner(card1, card2)
      results1_sum+=results1
      results2_sum+=results2
      i+=1

    if results1>results2:
        print(" Total Winner is person 1:","win: "+str(results1_sum))
    elif results2>results1:  
        print(" Total Winner is person 2","win: "+str(results2_sum))
    else:
        print("It is draw")