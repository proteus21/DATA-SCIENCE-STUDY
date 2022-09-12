"""
    Poproś użytkownika o podanie elementów dla dwóch list.
    W tym celu użytkownik najpierw dodaje do pierwszej listy, aż wpisze zero.
    Następnie dodaje do drugiej listy, aż znów wpisze zero.
    Twoim zadaniem jest wyświetlić posortowaną różnicę symetryczną zbiorów utworzonych z tych dwóch list.
"""
import math

def list():
 my_list=[]
 while True:
  odp=int(input("Give the number to the list. Zero stop all:"))
  if odp==0:
    break
  my_list.append(odp)
 return my_list

if __name__=="__main__":
  listA=[]
  listB=[]
  print("Give first list")
  listA=list()
  print("Give second list")
  listB=list()
  print("Show sorted difference symmetric set")
  set_dif = set(listA).symmetric_difference(set(listB)) # or set(listA)^set(listB)
  sorted(set_dif)
  print(set_dif)
