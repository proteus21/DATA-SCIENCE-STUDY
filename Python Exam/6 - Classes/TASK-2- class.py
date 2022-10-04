from itertools import product
import random
# we need two for loop as others case
class Card:
    VALUE = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] # always in capital letters
    SUITS = ['Heart', 'Diamonds', 'Spades', 'Clubs']


    def __init__(self, suit, value):
        self.suit= suit
        self. value= value

    def __repr__(self):
        return f"{self.suit} {self.value}"

class Deck:
    def __init__(self):
        self.cards= []
        for suit, value in product(Card.SUITS, Card.VALUE): # poniewaz dotyczy calej talii na stole
            self.cards.append(Card(suit, value))
    def deal(self):
        return self.cards. pop()

    def shuffle(self):
        if len(self.cards)==52:
         return random.shuffle(self.cards)

if __name__ == '__main__':
  #  deck=[]
  #  for suit, value in product(Card.SUITS, Card.VALUE):
  #      deck.append(Card(suit, value))
    d= Deck()
    print(d.cards)
    d.shuffle()
    print(d.cards)
    d.deal()