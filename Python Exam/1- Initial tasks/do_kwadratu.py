"""
    Napisz program, który poprosi użytkownika o liczbę naturalną (N) i wypisze wszystkie liczby
    od 1 do N podniesione do kwadratu (pętla for).
"""
N= int(input("Give the integer number:"))
for i in range(1,N):
    print(i**2)