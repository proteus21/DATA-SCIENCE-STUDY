"""
    Stwórz klasę Notebook, która będzie zawierała pola: producenta, cenę netto oraz pamięć RAM.
    Dopisz metody do obliczenia ceny brutto (+23% VAT) oraz zwiększenia ilości RAM-u.
"""
import math
import sys

class Notebook:
    manufacturer= "Polish"
    netto_price=12
    memory_Ram=0
    def __init__(self, manufacturer, netto_price,memory_Ram):
        self.manufacturer=manufacturer
        self.netto_price=netto_price
        self.memory_Ram=memory_Ram
    def gross_amout(self):
        amount=int(self.netto_price)+(0.23*int(self.netto_price))
        return int(amount)
    def increase_memory(self, extra_ram):
       self.memory_Ram+=int(extra_ram)

if __name__=='__main__':
    my_notebook = Notebook('msi', 3300, 16)
    print('Your notebook made by {} costed {} and has {} GB Ram'.format(my_notebook.manufacturer,str(my_notebook.gross_amout()), my_notebook.memory_Ram))
    expand_memory=input("Add extra memory in GB:")
    my_notebook.increase_memory(expand_memory)
    print('Your notebook made by {} is expanded about {} GB Ram'.format(my_notebook.manufacturer,str(my_notebook.memory_Ram)))